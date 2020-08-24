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

def wordcloudUI(thistime):
    db.wordCloud_UI.delete_many({})
    count = 0
    wordcloud = []
    wordcloudTweet = []
    idData = []
    tweetCount = []
    weightTweet = 0
    weightRetweet = 1
    dataB = db.retweet_permin_data.aggregate([
                            {"$match": {"timeUpdate":{"$gte":thistime - dt.timedelta(minutes=180)}}},
                            { "$group": {
                                "_id": "$id_str",
                                "retweetNow": { 
                                "$sum": { 
                                    "$cond": [
                                        { "$gte": [ "$timeUpdate", thistime - dt.timedelta(minutes=180) ] },
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
                for j in i['hashtags']:
                    wordcloudTweet.append(j['text'])
                    count+=1
                    for l in range(k[1]):
                        wordcloud.append(j['text'])
                        count+=1
    C = Counter(wordcloudTweet)
    for k,v in C.items():
        db.wordCloud_UI.insert_one({
            "text": k,
            "retweet": 0,
            "tweet": v,
            "value": 0
        })
    D = Counter(wordcloud)
    updateCountRetweet = []
    updateCountValue = []
    for k,v in D.items():
        updateCountRetweet.append((pymongo.UpdateOne(
                {
                    'text':k
                },
                {
                    '$set': {
                        "retweet": v
                    }
                },upsert=True)))
    if(len(updateCountRetweet)>0):
        db.wordCloud_UI.bulk_write(updateCountRetweet,ordered=False)
    
    dataA = db.wordCloud_UI.find({})
    for i in dataA:
        retweet = i['retweet']*weightRetweet
        tweet = i['tweet']*weightTweet
        updateCountValue.append((pymongo.UpdateOne(
                {
                    'text':i['text']
                },
                {
                    '$set': {
                        "value": retweet+tweet
                    }
                },upsert=True)))
    if(len(updateCountValue)>0):
        db.wordCloud_UI.bulk_write(updateCountValue,ordered=False)

def checkDirty():
    toxic = 'เย็ด'
    delete = []
    dataA = db.wordCloud_UI.find()
    for i in dataA:
        if toxic in i['text']:
            delete.append(i['text'])
    db.wordCloud_UI.delete_many({"text": {"$in": delete}})