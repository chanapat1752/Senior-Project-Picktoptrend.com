# In[ ]:
# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import datetime as dt
import time
import json
from time import gmtime, strftime

import GetWordclouds


#In[]:
# client = MongoClient('mongodb://localhost:27017/University')
client = MongoClient('mongodb://superadmin:4rFV5tGB@45.32.105.145:27017/University?authSource=admin')
db = client.University


#In[]:

from random import seed
from random import randint
seed(1)
def test():
    timestamp = 1587168000000
    chulaPM = []
    thammasatPM = []
    mahidolPM = []
    kasetsartPM = []
    chiangMaiPM = []
    khonKaenPM = []
    srinakharinwirotPM = []
    MahasarakhamPM = []
    BuraphaPM = []
    maeFahLuangPM = []

    chula = 0
    thammasat = 0
    mahidol = 0
    kasetsart = 0
    chiangMai = 0
    khonKaen = 0
    srinakharinwirot = 0
    Mahasarakham = 0
    Burapha = 0
    maeFahLuang = 0

    for i in range(144):
        chula += randint(50, 150)
        thammasat += randint(0, 50)
        mahidol += randint(30, 40)
        kasetsart += randint(70, 100)
        chiangMai += randint(20, 50)
        khonKaen += randint(30, 50)
        srinakharinwirot += randint(0, 10)
        Mahasarakham += randint(2, 5)
        Burapha += randint(0, 20)
        maeFahLuang += randint(0, 10)
        chulaPM.append([timestamp,chula])
        thammasatPM.append([timestamp,thammasat])
        mahidolPM.append([timestamp,mahidol])
        kasetsartPM.append([timestamp,kasetsart])
        chiangMaiPM.append([timestamp,chiangMai])
        khonKaenPM.append([timestamp,khonKaen])
        srinakharinwirotPM.append([timestamp,srinakharinwirot])
        MahasarakhamPM.append([timestamp,Mahasarakham])
        BuraphaPM.append([timestamp,Burapha])
        maeFahLuangPM.append([timestamp,maeFahLuang])
        timestamp+= 600000
    db.graph_retweet_UI.delete_many({})
    db.graph_retweet_UI.insert_one({
        "name":"จุฬาลงกรณ์มหาวิทยาลัย",
        "data":chulaPM
    })
    db.graph_retweet_UI.insert_one({
        "name":"มหาวิทยาลัยธรรมศาสตร์",
        "data":thammasatPM
    })
    db.graph_retweet_UI.insert_one({
        "name":"มหาวิทยาลัยมหิดล",
        "data":mahidolPM
    })
    db.graph_retweet_UI.insert_one({
        "name":"มหาวิทยาลัยเกษตรศาสตร์",
        "data":kasetsartPM
    })
    db.graph_retweet_UI.insert_one({
        "name":"มหาวิทยาลัยเชียงใหม่",
        "data":chiangMaiPM
    })
    db.graph_retweet_UI.insert_one({
        "name":"มหาวิทยาลัยขอนแก่น",
        "data":khonKaenPM
    })
    db.graph_retweet_UI.insert_one({
        "name":"มหาวิทยาลัยศรีนครินทรวิโรฒ",
        "data":srinakharinwirotPM
    })
    db.graph_retweet_UI.insert_one({
        "name":"มหาวิทยาลัยมหาสารคาม",
        "data":MahasarakhamPM
    })
    db.graph_retweet_UI.insert_one({
        "name":"มหาวิทยาลัยบูรพา",
        "data":BuraphaPM
    })
    db.graph_retweet_UI.insert_one({
        "name":"มหาวิทยาลัยแม่ฟ้าหลวง",
        "data":maeFahLuangPM
    })

def sort_by_retweet(d):
    return d['retweet']

def test2():
    tweetTrends = []
    updateTrend = []
    removeTrend = []
    # thistime = dt.datetime.today()
    dataB = db.retweet_permin_data.aggregate([
                            {"$match": {"timeUpdate":{"$gte":thistime - dt.timedelta(minutes=120)}}},
                            { "$group": {
                                "_id": "$id_str",
                                "retweetNow": { 
                                "$sum": { 
                                    "$cond": [
                                        { "$gte": [ "$timeUpdate", thistime - dt.timedelta(minutes=120) ] },
                                        "$retweet", 
                                        0
                                    ]
                                }
                            },
                            }},
                        ])
    for item in dataB:
        tweetTrends.append({'id':item['_id'],'retweet':item['retweetNow']})
    tweetTrends.sort(key=sort_by_retweet, reverse=True)
    dataA = db.master_data.find({'trend':{"$gte":1}})
    for i in range(10):
        print(tweetTrends[i]['id'])
        print(tweetTrends[i]['retweet'])
    for i in dataA:
        removeTrend.append((pymongo.UpdateOne(
                {
                    'id_str':i['id_str']
                },
                {
                    '$set': {
                        "trend": 0
                    }
                },upsert=True)))
    if(len(removeTrend)>0):
        db.master_data.bulk_write(removeTrend,ordered=False)
    for i in range(10):
        updateTrend.append((pymongo.UpdateOne(
                {
                    'id_str':tweetTrends[i]['id']
                },
                {
                    '$set': {
                        "trend": i+1
                    }
                },upsert=True)))
    if(len(updateTrend)>0):
        db.master_data.bulk_write(updateTrend,ordered=False)

# def test3():
#     count = 0
#     dataA = db.retweet_permin_data.find({'id_str':'1255532245437214720'})
#     for i in dataA:
#         count+=i['retweet']
#     print(count)

def test3():
    updateTrend = []
    dataA = db.master_data.find({})
    for i in dataA:
        updateTrend.append((pymongo.UpdateOne(
                {
                    'id_str':i['id_str']
                },
                {
                    '$set': {
                        "retweet_1Day":0
                    }
                },upsert=True)))
    if(len(updateTrend)>0):
        db.master_data.bulk_write(updateTrend,ordered=False)

def sort_by_re(d):
    '''a helper function for sorting'''
    return d['y']

def test4():
    checkRetweet = []
    chula2 = 0
    thammasat2 = 0
    mahidol2 = 0
    kasetsart2 = 0
    chiangMai2 = 0
    khonKaen2 = 0
    srinakharinwirot2 = 0
    Mahasarakham2 = 0
    Burapha2 = 0
    maeFahLuang2 = 0

    dataA = db.retweet_permin_data.aggregate([
                            {"$match": {"timeUpdate":{"$gte":dt.datetime(2020, 6, 2, 0, 0, 0, 0)}}},
                            { "$group": {
                                "_id": "$university",
                                "retweetNow": { 
                                "$sum": { 
                                    "$cond": [
                                        { "$gte": [ "$timeUpdate", dt.datetime(2020, 6, 2, 0, 0, 0, 0) ] },
                                        "$retweet", 
                                        0
                                    ]
                                }
                            },
                            }},
                        ])
    for i in dataA:
        if i['_id'] == 'Thammasat':
            thammasat2 = i['retweetNow']
        if i['_id'] == 'Chula':
            chula2 = i['retweetNow']
        if i['_id'] == 'Mahidol':
            mahidol2 = i['retweetNow']
        if i['_id'] == 'Kasetsart':
            kasetsart2 = i['retweetNow']
        if i['_id'] == 'Chiang Mai':
            chiangMai2 = i['retweetNow']
        if i['_id'] == 'Khon Kaen':
            khonKaen2 = i['retweetNow']
        if i['_id'] == 'Srinakharinwirot':
            srinakharinwirot2 = i['retweetNow']
        if i['_id'] == 'Mahasarakham':
            Mahasarakham2 = i['retweetNow']
        if i['_id'] == 'Burapha':
            Burapha2 = i['retweetNow']
        if i['_id'] == 'Mae Fah Luang':
            maeFahLuang2 = i['retweetNow']
    
    checkRetweet.append({"x":"1",
        "y":chula2})
    checkRetweet.append({"x":"2",
        "y":thammasat2})
    checkRetweet.append({"x":"3",
        "y":mahidol2})
    checkRetweet.append({"x":"4",
        "y":kasetsart2})
    checkRetweet.append({"x":"5",
        "y":chiangMai2})
    checkRetweet.append({"x":"6",
        "y":khonKaen2})
    checkRetweet.append({"x":"7",
        "y":srinakharinwirot2})
    checkRetweet.append({"x":"8",
        "y":Mahasarakham2})
    checkRetweet.append({"x":"9",
        "y":Burapha2})
    checkRetweet.append({"x":"10",
        "y":maeFahLuang2})
    checkRetweet.sort(key=sort_by_re, reverse=True)

def test5():
    toxic = 'เย็ด'
    delete = []
    dataA = db.wordCloud_UI.find()
    for i in dataA:
        if toxic in i['text']:
            delete.append(i['text'])
    db.wordCloud_UI.delete_many({"text": {"$in": delete}})

if __name__ == "__main__":
    thistime = dt.datetime.today() 
    t1 = time.time()
    # test5()
    # GetWordclouds.wordcloudUI(thistime)
    t2 = time.time()
    t3 = t2 - t1
    print(t3)