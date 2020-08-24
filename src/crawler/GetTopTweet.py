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
client = MongoClient('mongodb://superadmin:4rFV5tGB@0.0.0.0:27017/University?authSource=admin')
db = client.University

def sort_by_retweet(d):
    return d['retweet']

def toptrend(thistime):
    tweetTrends = []
    updateTrend = []
    removeTrend = []
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
                        "trend": i+1,
                        "retweet_30min":tweetTrends[i]['retweet']
                    }
                },upsert=True)))
    if(len(updateTrend)>0):
        db.master_data.bulk_write(updateTrend,ordered=False)

def getTopTrendInOneDay(thistime):
    tweetTrends = []
    updateTrend = []
    removeTrend = []
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
        tweetTrends.append({'id':item['_id'],'retweet':item['retweetNow']})
    tweetTrends.sort(key=sort_by_retweet, reverse=True)
    dataA = db.master_data.find({'trendInDay':{"$gte":1}})
    for i in dataA:
        removeTrend.append((pymongo.UpdateOne(
                {
                    'id_str':i['id_str']
                },
                {
                    '$set': {
                        "trendInDay": 0
                    }
                },upsert=True)))
    if(len(removeTrend)>0):
        db.master_data.bulk_write(removeTrend,ordered=False)
    for i in range(len(tweetTrends)):
        updateTrend.append((pymongo.UpdateOne(
                {
                    'id_str':tweetTrends[i]['id']
                },
                {
                    '$set': {
                        "trendInDay": i+1,
                        "retweet_1Day":tweetTrends[i]['retweet']
                    }
                },upsert=True)))
    if(len(updateTrend)>0):
        db.master_data.bulk_write(updateTrend,ordered=False)
