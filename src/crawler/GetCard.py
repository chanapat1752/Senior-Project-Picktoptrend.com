import pymongo
from pymongo import MongoClient
from collections import Counter
import datetime as dt
import time
import json
from time import gmtime, strftime


# client = MongoClient('mongodb://localhost:27017/University')
client = MongoClient('mongodb://superadmin:4rFV5tGB@0.0.0.0:27017/University?authSource=admin')
db = client.University

def sort_by_retweet(d):
    return d['retweet']

def card(thistime):
    db.card_UI.delete_many({})
    university = []
    topHashtags = ''
    topHashtagsCount = 0
    thammasatRetweet = 0
    thammasatTweet = 0
    hashtagsPerTweet = []
    hashtagsPerRetweet = []
    countTweet = 0
    countRetweet = 0
    idData = []
    tweetCount = []
    

    #การ์ดมหาวิทยาลัย
    dataA = db.retweet_permin_data.aggregate([
                            {"$match": {"timeUpdate":{"$gte":dt.datetime(thistime.year, thistime.month, thistime.day, 0, 0, 0, 0)}}},
                            { "$group": {
                                "_id": "$university",
                                "retweetNow": { 
                                "$sum": { 
                                    "$cond": [
                                        { "$gte": [ "$timeUpdate", dt.datetime(thistime.year, thistime.month, thistime.day, 0, 0, 0, 0) ] },
                                        "$retweet", 
                                        0
                                    ]
                                }
                            },
                            }},
                        ])
    for i in dataA:
        if i['_id'] == 'Thammasat':
            university.append({'university': 'ม.ธรรมศาสตร์','retweet': i['retweetNow']})
            thammasatRetweet = i['retweetNow']
        if i['_id'] == 'Chula':
            university.append({'university': 'จุฬาลงกรณ์มหาวิทยาลัย','retweet': i['retweetNow']})
        if i['_id'] == 'Mahidol':
            university.append({'university': 'ม.มหิดล','retweet': i['retweetNow']})
        if i['_id'] == 'Kasetsart':
            university.append({'university': 'ม.เกษตรศาสตร์','retweet': i['retweetNow']})
        if i['_id'] == 'Chiang Mai':
            university.append({'university': 'ม.เชียงใหม่','retweet': i['retweetNow']})
        if i['_id'] == 'Khon Kaen':
            university.append({'university': 'ม.ขอนแก่น','retweet': i['retweetNow']})
        if i['_id'] == 'Srinakharinwirot':
            university.append({'university': 'ม.ศรีนครินทรวิโรฒ','retweet': i['retweetNow']})
        if i['_id'] == 'Mahasarakham':
            university.append({'university': 'ม.มหาสารคาม','retweet': i['retweetNow']})
        if i['_id'] == 'Burapha':
            university.append({'university': 'ม.บูรพา','retweet': i['retweetNow']})
        if i['_id'] == 'Mae Fah Luang':
            university.append({'university': 'ม.แม่ฟ้าหลวง','retweet': i['retweetNow']})
    
    university.sort(key=sort_by_retweet, reverse=True)

    #การ์ดแฮชแท็ก รีทวีต และ ทวีต
    dataB = db.retweet_permin_data.aggregate([
                            {"$match": {"timeUpdate":{"$gte":dt.datetime(thistime.year, thistime.month, thistime.day, 0, 0, 0, 0)}}},
                            { "$group": {
                                "_id": "$id_str",
                                "retweetNow": { 
                                "$sum": { 
                                    "$cond": [
                                        { "$gte": [ "$timeUpdate", dt.datetime(thistime.year, thistime.month, thistime.day, 0, 0, 0, 0) ] },
                                        "$retweet", 
                                        0
                                    ]
                                }
                            },
                            }},
                        ])

    for item in dataB:
        idData.append(item['_id'])
        tweetCount.append([item['_id'],item['retweetNow']])
    dataA = db.master_data.find({"id_str": {"$in": idData}})
    for i in dataA:
        for k in tweetCount:
            if(k[0] == i['id_str']):
                countRetweet+=k[1]
                for j in i['hashtags']:
                    hashtagsPerTweet.append(j['text'])
                    for l in range(k[1]):
                        hashtagsPerRetweet.append(j['text'])

    dataC = db.master_data.find({'timeCreate':{'$gte':dt.datetime(thistime.year, thistime.month, thistime.day, 0, 0, 0, 0)}})
    for i in dataC:
        if i['university'] == 'Thammasat':
            thammasatTweet += 1
        countTweet+=1
        

    C = Counter(hashtagsPerRetweet)
    for k,v in C.most_common(1):
        topHashtags = k
        topHashtagsCount = v

    db.card_UI.insert_one({
        'university':university[0]['university'],
        'retweet':university[0]['retweet'],
        'hashtag':topHashtags,
        'hashtagCount':topHashtagsCount,
        'tweetInThisDay':countTweet,
        'retweetInThisDay':countRetweet,
        'thammasatRetweet':thammasatRetweet,
        'thammasatTweet':thammasatTweet,
        'date': str(thistime.day)+'/'+str(thistime.month)+'/'+str(thistime.year)
    })