# In[ ]:
# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import datetime as dt
import time
import json
from time import gmtime, strftime


#In[]:
# client = MongoClient('mongodb://localhost:27017/University')
client = MongoClient('mongodb://superadmin:4rFV5tGB@0.0.0.0:27017/University?authSource=admin')
db = client.University


#In[]:

def retweetUI(glo_time,timestamp):
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

    if glo_time.hour == 0 and glo_time.minute == 0:
        db.graph_retweet_UI.delete_many({})
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
    else:
        dataA = db.retweet_permin_data.aggregate([
                            {"$match": {"timeUpdate":{"$gte":dt.datetime(glo_time.year, glo_time.month, glo_time.day, 0, 0, 0, 0)}}},
                            { "$group": {
                                "_id": "$university",
                                "retweetNow": { 
                                "$sum": { 
                                    "$cond": [
                                        { "$gte": [ "$timeUpdate", dt.datetime(glo_time.year, glo_time.month, glo_time.day, 0, 0, 0, 0) ] },
                                        "$retweet", 
                                        0
                                    ]
                                }
                            },
                            }},
                        ])
        for i in dataA:
            if i['_id'] == 'Thammasat':
                thammasat = i['retweetNow']
            if i['_id'] == 'Chula':
                chula = i['retweetNow']
            if i['_id'] == 'Mahidol':
                mahidol = i['retweetNow']
            if i['_id'] == 'Kasetsart':
                kasetsart = i['retweetNow']
            if i['_id'] == 'Chiang Mai':
                chiangMai = i['retweetNow']
            if i['_id'] == 'Khon Kaen':
                khonKaen = i['retweetNow']
            if i['_id'] == 'Srinakharinwirot':
                srinakharinwirot = i['retweetNow']
            if i['_id'] == 'Mahasarakham':
                Mahasarakham = i['retweetNow']
            if i['_id'] == 'Burapha':
                Burapha = i['retweetNow']
            if i['_id'] == 'Mae Fah Luang':
                maeFahLuang = i['retweetNow']

        dataA = db.graph_retweet_UI.find()
        for i in dataA:
            if i['name'] == 'จุฬาลงกรณ์มหาวิทยาลัย':
                chulaPM = i['data']
            if i['name'] == 'มหาวิทยาลัยธรรมศาสตร์':
                thammasatPM = i['data']
            if i['name'] == 'มหาวิทยาลัยมหิดล':
                mahidolPM = i['data']
            if i['name'] == 'มหาวิทยาลัยเกษตรศาสตร์':
                kasetsartPM = i['data']
            if i['name'] == 'มหาวิทยาลัยเชียงใหม่':
                chiangMaiPM = i['data']
            if i['name'] == 'มหาวิทยาลัยขอนแก่น':
                khonKaenPM = i['data']
            if i['name'] == 'มหาวิทยาลัยศรีนครินทรวิโรฒ':
                srinakharinwirotPM = i['data']
            if i['name'] == 'มหาวิทยาลัยมหาสารคาม':
                MahasarakhamPM = i['data']
            if i['name'] == 'มหาวิทยาลัยบูรพา':
                BuraphaPM = i['data']
            if i['name'] == 'มหาวิทยาลัยแม่ฟ้าหลวง':
                maeFahLuangPM = i['data']

        db.graph_retweet_UI.delete_many({})

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

def tweetUI(glo_time,timestamp):
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

    if glo_time.hour == 0 and glo_time.minute == 0:
        db.graph_tweet_UI.delete_many({})
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

        db.graph_tweet_UI.insert_one({
            "name":"จุฬาลงกรณ์มหาวิทยาลัย",
            "data":chulaPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยธรรมศาสตร์",
            "data":thammasatPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยมหิดล",
            "data":mahidolPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยเกษตรศาสตร์",
            "data":kasetsartPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยเชียงใหม่",
            "data":chiangMaiPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยขอนแก่น",
            "data":khonKaenPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยศรีนครินทรวิโรฒ",
            "data":srinakharinwirotPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยมหาสารคาม",
            "data":MahasarakhamPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยบูรพา",
            "data":BuraphaPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยแม่ฟ้าหลวง",
            "data":maeFahLuangPM
        })
    else:
        dataA = db.master_data.find({'timeCreate':{'$gte':dt.datetime(glo_time.year, glo_time.month, glo_time.day, 0, 0, 0, 0)}})
        for i in dataA:
            if i['university'] == 'Chula':
                chula = chula+1
            elif i['university'] == 'Thammasat':
                thammasat = thammasat+1
            elif i['university'] == 'Mahidol':
                mahidol = mahidol+1
            elif i['university'] == 'Kasetsart':
                kasetsart = kasetsart+1
            elif i['university'] == 'Chiang Mai':
                chiangMai = chiangMai+1
            elif i['university'] == 'Khon Kaen':
                khonKaen = khonKaen+1
            elif i['university'] == 'Srinakharinwirot':
                srinakharinwirot = srinakharinwirot+1
            elif i['university'] == 'Mahasarakham':
                Mahasarakham = Mahasarakham+1
            elif i['university'] == 'Burapha':
                Burapha = Burapha+1
            elif i['university'] == 'Mae Fah Luang':
                maeFahLuang = maeFahLuang+1

        dataA = db.graph_tweet_UI.find()
        for i in dataA:
            if i['name'] == 'จุฬาลงกรณ์มหาวิทยาลัย':
                chulaPM = i['data']
            if i['name'] == 'มหาวิทยาลัยธรรมศาสตร์':
                thammasatPM = i['data']
            if i['name'] == 'มหาวิทยาลัยมหิดล':
                mahidolPM = i['data']
            if i['name'] == 'มหาวิทยาลัยเกษตรศาสตร์':
                kasetsartPM = i['data']
            if i['name'] == 'มหาวิทยาลัยเชียงใหม่':
                chiangMaiPM = i['data']
            if i['name'] == 'มหาวิทยาลัยขอนแก่น':
                khonKaenPM = i['data']
            if i['name'] == 'มหาวิทยาลัยศรีนครินทรวิโรฒ':
                srinakharinwirotPM = i['data']
            if i['name'] == 'มหาวิทยาลัยมหาสารคาม':
                MahasarakhamPM = i['data']
            if i['name'] == 'มหาวิทยาลัยบูรพา':
                BuraphaPM = i['data']
            if i['name'] == 'มหาวิทยาลัยแม่ฟ้าหลวง':
                maeFahLuangPM = i['data']

        db.graph_tweet_UI.delete_many({})

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

        db.graph_tweet_UI.insert_one({
            "name":"จุฬาลงกรณ์มหาวิทยาลัย",
            "data":chulaPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยธรรมศาสตร์",
            "data":thammasatPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยมหิดล",
            "data":mahidolPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยเกษตรศาสตร์",
            "data":kasetsartPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยเชียงใหม่",
            "data":chiangMaiPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยขอนแก่น",
            "data":khonKaenPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยศรีนครินทรวิโรฒ",
            "data":srinakharinwirotPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยมหาสารคาม",
            "data":MahasarakhamPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยบูรพา",
            "data":BuraphaPM
        })
        db.graph_tweet_UI.insert_one({
            "name":"มหาวิทยาลัยแม่ฟ้าหลวง",
            "data":maeFahLuangPM
        })

def retweetPerMinUI(glo_time , timestamp):
    chulaPM2 = []
    thammasatPM2 = []
    mahidolPM2 = []
    kasetsartPM2 = []
    chiangMaiPM2 = []
    khonKaenPM2 = []
    srinakharinwirotPM2 = []
    MahasarakhamPM2 = []
    BuraphaPM2 = []
    maeFahLuangPM2 = []
    
    dataA = db.graph_retweetpermin_UI.find()
    for i in dataA:
        if i['name'] == 'จุฬาลงกรณ์มหาวิทยาลัย':
            chulaPM2 = i['data']
        if i['name'] == 'มหาวิทยาลัยธรรมศาสตร์':
            thammasatPM2 = i['data']
        if i['name'] == 'มหาวิทยาลัยมหิดล':
            mahidolPM2 = i['data']
        if i['name'] == 'มหาวิทยาลัยเกษตรศาสตร์':
            kasetsartPM2 = i['data']
        if i['name'] == 'มหาวิทยาลัยเชียงใหม่':
            chiangMaiPM2 = i['data']
        if i['name'] == 'มหาวิทยาลัยขอนแก่น':
            khonKaenPM2 = i['data']
        if i['name'] == 'มหาวิทยาลัยศรีนครินทรวิโรฒ':
            srinakharinwirotPM2 = i['data']
        if i['name'] == 'มหาวิทยาลัยมหาสารคาม':
            MahasarakhamPM2 = i['data']
        if i['name'] == 'มหาวิทยาลัยบูรพา':
            BuraphaPM2 = i['data']
        if i['name'] == 'มหาวิทยาลัยแม่ฟ้าหลวง':
            maeFahLuangPM2 = i['data']

    chulaPM2.pop(0)
    thammasatPM2.pop(0)
    mahidolPM2.pop(0)
    kasetsartPM2.pop(0)
    chiangMaiPM2.pop(0)
    khonKaenPM2.pop(0)
    srinakharinwirotPM2.pop(0)
    MahasarakhamPM2.pop(0)
    BuraphaPM2.pop(0)
    maeFahLuangPM2.pop(0)

    dataA = db.uni_count_permin_data.find_one({'timeUpdate':{'$gte':glo_time - dt.timedelta(seconds=30)}})

    chulaPM2.append([timestamp,dataA['จุฬาลงกรณ์มหาวิทยาลัย']])
    thammasatPM2.append([timestamp,dataA['มหาวิทยาลัยธรรมศาสตร์']])
    mahidolPM2.append([timestamp,dataA['มหาวิทยาลัยมหิดล']])
    kasetsartPM2.append([timestamp,dataA['มหาวิทยาลัยเกษตรศาสตร์']])
    chiangMaiPM2.append([timestamp,dataA['มหาวิทยาลัยเชียงใหม่']])
    khonKaenPM2.append([timestamp,dataA['มหาวิทยาลัยขอนแก่น']])
    srinakharinwirotPM2.append([timestamp,dataA['มหาวิทยาลัยศรีนครินทรวิโรฒ']])
    MahasarakhamPM2.append([timestamp,dataA['มหาวิทยาลัยมหาสารคาม']])
    BuraphaPM2.append([timestamp,dataA['มหาวิทยาลัยบูรพา']])
    maeFahLuangPM2.append([timestamp,dataA['มหาวิทยาลัยแม่ฟ้าหลวง']])

    db.graph_retweetpermin_UI.delete_many({})
    db.graph_retweetpermin_UI.insert_one({
        "name":"จุฬาลงกรณ์มหาวิทยาลัย",
        "data":chulaPM2
    })
    db.graph_retweetpermin_UI.insert_one({
        "name":"มหาวิทยาลัยธรรมศาสตร์",
        "data":thammasatPM2
    })
    db.graph_retweetpermin_UI.insert_one({
        "name":"มหาวิทยาลัยมหิดล",
        "data":mahidolPM2
    })
    db.graph_retweetpermin_UI.insert_one({
        "name":"มหาวิทยาลัยเกษตรศาสตร์",
        "data":kasetsartPM2
    })
    db.graph_retweetpermin_UI.insert_one({
        "name":"มหาวิทยาลัยเชียงใหม่",
        "data":chiangMaiPM2
    })
    db.graph_retweetpermin_UI.insert_one({
        "name":"มหาวิทยาลัยขอนแก่น",
        "data":khonKaenPM2
    })
    db.graph_retweetpermin_UI.insert_one({
        "name":"มหาวิทยาลัยศรีนครินทรวิโรฒ",
        "data":srinakharinwirotPM2
    })
    db.graph_retweetpermin_UI.insert_one({
        "name":"มหาวิทยาลัยมหาสารคาม",
        "data":MahasarakhamPM2
    })
    db.graph_retweetpermin_UI.insert_one({
        "name":"มหาวิทยาลัยบูรพา",
        "data":BuraphaPM2
    })
    db.graph_retweetpermin_UI.insert_one({
        "name":"มหาวิทยาลัยแม่ฟ้าหลวง",
        "data":maeFahLuangPM2
    })

def sort_by_y(d):
    '''a helper function for sorting'''
    return d['value']

def sort_by_re(d):
    '''a helper function for sorting'''
    return d['y']

def barCountUI(glo_time):
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

    dataTweet = []
    dataRetweet = []
    dataTweet2 = []
    dataRetweet2 = []

    checkRetweet = []
    moreCount = 0.9
    checkCount = 0
    check = False

    db.graph_barcount_UI.delete_many({})

    dataA = db.retweet_permin_data.aggregate([
                            {"$match": {"timeUpdate":{"$gte":dt.datetime(glo_time.year, glo_time.month, glo_time.day, 0, 0, 0, 0)}}},
                            { "$group": {
                                "_id": "$university",
                                "retweetNow": { 
                                "$sum": { 
                                    "$cond": [
                                        { "$gte": [ "$timeUpdate", dt.datetime(glo_time.year, glo_time.month, glo_time.day, 0, 0, 0, 0) ] },
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

    checkCount = checkRetweet[0]['y'] - checkRetweet[0]['y']*moreCount

    dataA = db.master_data.find({'timeCreate':{'$gte':dt.datetime(glo_time.year, glo_time.month, glo_time.day, 0, 0, 0, 0)}})
    for i in dataA:
        if i['university'] == 'Chula':
            chula = chula+1
        if i['university'] == 'Thammasat':
            thammasat = thammasat+1
        if i['university'] == 'Mahidol':
            mahidol = mahidol+1
        if i['university'] == 'Kasetsart':
            kasetsart = kasetsart+1
        if i['university'] == 'Chiang Mai':
            chiangMai = chiangMai+1
        if i['university'] == 'Khon Kaen':
            khonKaen = khonKaen+1
        if i['university'] == 'Srinakharinwirot':
            srinakharinwirot = srinakharinwirot+1
        if i['university'] == 'Mahasarakham':
            Mahasarakham = Mahasarakham+1
        if i['university'] == 'Burapha':
            Burapha = Burapha+1
        if i['university'] == 'Mae Fah Luang':
            maeFahLuang = maeFahLuang+1
    
    if(chula2>checkCount):
        dataRetweet2.append({"x":"จุฬาฯ",
        "y":chula2,"value":chula2+chula})
        dataTweet2.append({"x":"จุฬาฯ",
        "y":chula,"value":chula2+chula})
        check = True
    else:
        dataRetweet.append({"x":"จุฬาฯ",
        "y":chula2,"value":chula2+chula})
        dataTweet.append({"x":"จุฬาฯ",
        "y":chula,"value":chula2+chula})

    if(thammasat2>checkCount):
        dataRetweet2.append({"x":"ม.ธรรมศาสตร์",
        "y":thammasat2,"value":thammasat2+thammasat})
        dataTweet2.append({"x":"ม.ธรรมศาสตร์",
        "y":thammasat,"value":thammasat2+thammasat})
        check = True
    else:
        dataRetweet.append({"x":"ม.ธรรมศาสตร์",
        "y":thammasat2,"value":thammasat2+thammasat})
        dataTweet.append({"x":"ม.ธรรมศาสตร์",
        "y":thammasat,"value":thammasat2+thammasat})

    if(mahidol2>checkCount):
        dataRetweet2.append({"x":"ม.มหิดล",
        "y":mahidol2,"value":mahidol2+mahidol})
        dataTweet2.append({"x":"ม.มหิดล",
        "y":mahidol,"value":mahidol2+mahidol})
        check = True
    else:
        dataRetweet.append({"x":"ม.มหิดล",
        "y":mahidol2,"value":mahidol2+mahidol})
        dataTweet.append({"x":"ม.มหิดล",
        "y":mahidol,"value":mahidol2+mahidol})

    if(kasetsart2>checkCount):
        dataRetweet2.append({"x":"ม.เกษตรศาสตร์",
        "y":kasetsart2,"value":kasetsart2+kasetsart})
        dataTweet2.append({"x":"ม.เกษตรศาสตร์",
        "y":kasetsart,"value":kasetsart2+kasetsart})
        check = True
    else:
        dataRetweet.append({"x":"ม.เกษตรศาสตร์",
        "y":kasetsart2,"value":kasetsart2+kasetsart})
        dataTweet.append({"x":"ม.เกษตรศาสตร์",
        "y":kasetsart,"value":kasetsart2+kasetsart})

    if(chiangMai2>checkCount):
        dataRetweet2.append({"x":"ม.เชียงใหม่",
        "y":chiangMai2,"value":chiangMai2+chiangMai})
        dataTweet2.append({"x":"ม.เชียงใหม่",
        "y":chiangMai,"value":chiangMai2+chiangMai})
        check = True
    else:
        dataRetweet.append({"x":"ม.เชียงใหม่",
        "y":chiangMai2,"value":chiangMai2+chiangMai})
        dataTweet.append({"x":"ม.เชียงใหม่",
        "y":chiangMai,"value":chiangMai2+chiangMai})

    if(khonKaen2>checkCount):
        dataRetweet2.append({"x":"ม.ขอนแก่น",
        "y":khonKaen2,"value":khonKaen2+khonKaen})
        dataTweet2.append({"x":"ม.ขอนแก่น",
        "y":khonKaen,"value":khonKaen2+khonKaen})
        check = True
    else:
        dataRetweet.append({"x":"ม.ขอนแก่น",
        "y":khonKaen2,"value":khonKaen2+khonKaen})
        dataTweet.append({"x":"ม.ขอนแก่น",
        "y":khonKaen,"value":khonKaen2+khonKaen})

    if(srinakharinwirot2>checkCount):
        dataRetweet2.append({"x":"ม.ศรีนครินทรวิโรฒ",
        "y":srinakharinwirot2,"value":srinakharinwirot2+srinakharinwirot})
        dataTweet2.append({"x":"ม.ศรีนครินทรวิโรฒ",
        "y":srinakharinwirot,"value":srinakharinwirot2+srinakharinwirot})
        check = True
    else:
        dataRetweet.append({"x":"ม.ศรีนครินทรวิโรฒ",
        "y":srinakharinwirot2,"value":srinakharinwirot2+srinakharinwirot})
        dataTweet.append({"x":"ม.ศรีนครินทรวิโรฒ",
        "y":srinakharinwirot,"value":srinakharinwirot2+srinakharinwirot})

    if(Mahasarakham2>checkCount):
        dataRetweet2.append({"x":"ม.มหาสารคาม",
        "y":Mahasarakham2,"value":Mahasarakham2+Mahasarakham})
        dataTweet2.append({"x":"ม.มหาสารคาม",
        "y":Mahasarakham,"value":Mahasarakham2+Mahasarakham})
        check = True
    else:
        dataRetweet.append({"x":"ม.มหาสารคาม",
        "y":Mahasarakham2,"value":Mahasarakham2+Mahasarakham})
        dataTweet.append({"x":"ม.มหาสารคาม",
        "y":Mahasarakham,"value":Mahasarakham2+Mahasarakham})

    if(Burapha2>checkCount):
        dataRetweet2.append({"x":"ม.บูรพา",
        "y":Burapha2,"value":Burapha2+Burapha})
        dataTweet2.append({"x":"ม.บูรพา",
        "y":Burapha,"value":Burapha2+Burapha})
        check = True
    else:
        dataRetweet.append({"x":"ม.บูรพา",
        "y":Burapha2,"value":Burapha2+Burapha})
        dataTweet.append({"x":"ม.บูรพา",
        "y":Burapha,"value":Burapha2+Burapha})

    if(maeFahLuang2>checkCount):
        dataRetweet2.append({"x":"ม.แม่ฟ้าหลวง",
        "y":maeFahLuang2,"value":maeFahLuang2+maeFahLuang})
        dataTweet2.append({"x":"ม.แม่ฟ้าหลวง",
        "y":maeFahLuang,"value":maeFahLuang2+maeFahLuang})
        check = True
    else:
        dataRetweet.append({"x":"ม.แม่ฟ้าหลวง",
        "y":maeFahLuang2,"value":maeFahLuang2+maeFahLuang})
        dataTweet.append({"x":"ม.แม่ฟ้าหลวง",
        "y":maeFahLuang,"value":maeFahLuang2+maeFahLuang})


    dataRetweet.sort(key=sort_by_y, reverse=True)
    dataRetweet2.sort(key=sort_by_y, reverse=True)
    dataTweet.sort(key=sort_by_y, reverse=True)
    dataTweet2.sort(key=sort_by_y, reverse=True)
    
    db.graph_barcount_UI.insert_one({
        "typeOfGraph":1,
        "count":len(dataRetweet),
        "name":"จำนวนรีทวีต",
        "data":dataRetweet,
        "check":check
    })

    db.graph_barcount_UI.insert_one({
        "typeOfGraph":1,
        "count":len(dataTweet),
        "name":"จำนวนทวีต",
        "data":dataTweet,
        "check":check
    })

    db.graph_barcount_UI.insert_one({
        "typeOfGraph":2,
        "count":len(dataRetweet2),
        "name":"จำนวนรีทวีต",
        "data":dataRetweet2,
        "check":check
    })

    db.graph_barcount_UI.insert_one({
        "typeOfGraph":2,
        "count":len(dataTweet2),
        "name":"จำนวนทวีต",
        "data":dataTweet2,
        "check":check
    })
