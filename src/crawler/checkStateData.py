# In[ ]:
# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import datetime as dt
import time
import json
from time import gmtime, strftime

#In[]:
#client = MongoClient('mongodb://localhost:27017/University')
client = MongoClient('mongodb://superadmin:4rFV5tGB@0.0.0.0:27017/University?authSource=admin')
db = client.University

# state_check = [1,2,3]
# time_query = [1800,3600,21600,86400]
# state_rt = [100,300,1000,1000]
# state_multiple = [1.10,1.25,1.50,1.75]
# state_count = [5,3,2]
#In[]:
def checkState(thistime):
    stateData = []
    dataA = db.retweet_update_data.find({'timeUpdate':{'$gte':thistime - dt.timedelta(minutes=30)}})
    for item in dataA:
        try:
            if item['state_check'] == 1:
                db.retweet_state_data.insert_one(
                {
                    'university':item['university'],
                    'id_str':item['id_str'],
                    'retweet_count':item['state_rt'],
                    'favorite_count':item['favorite_count'],
                    'timeUpdate':thistime - dt.timedelta(minutes=1)
                }
            )
            stateData.append((pymongo.UpdateOne(
                    {
                        'id_str':item['id_str']
                    },
                    {
                        '$set': {
                            'state_check':0,
                        }
                    },upsert=True)))
        except:
            next
    dataB = db.retweet_update_data.find({'state_check':0,'timeUpdate':{'$lt':thistime - dt.timedelta(minutes=30)}})
    for item in dataB:
        stateData.append((pymongo.UpdateOne(
                {
                    'id_str':item['id_str']
                },
                {
                    '$set': {
                        'state_check':1,
                        'state_rt':item['retweet_count']
                    }
                },upsert=True)))
    if(len(stateData)>0):
        db.retweet_update_data.bulk_write(stateData,ordered=False)
    # dataA = db.retweet_update_data.find({'state_check':0,'timeUpdate':{'$lte':thistime - dt.timedelta(seconds=time_query[0])}})
    # for item in dataA:
    #     if(item['retweet_count']>=state_rt[0] and item['state_rt']*state_multiple[0]<item['retweet_count']):
    #         stateData.append((pymongo.UpdateOne(
    #             {
    #                 'id_str':item['id_str']
    #             },
    #             {
    #                 '$set': {
    #                     'state_rt':item['retweet_count'],
    #                     'timeUpdate':thistime
    #                 }
    #             },upsert=True)))
    #     else:
    #         stateData.append((pymongo.UpdateOne(
    #             {
    #                 'id_str':item['id_str']
    #             },
    #             {
    #                 '$set': {
    #                     'state_check':1,
    #                     'state_count':0,
    #                     'state_rt':item['retweet_count'],
    #                     'timeUpdate':thistime
    #                 }
    #             },upsert=True)))
    #         stateData2.append((pymongo.UpdateOne(
    #             {
    #                 'id_str':item['id_str']
    #             },
    #             {
    #                 '$set': {
    #                     'state':1,
    #                 }
    #             },upsert=True)))
    # for i in range(len(state_check)):
    #     dataA = db.retweet_update_data.find({'state_check':state_check[i],'timeUpdate':{'$lte':thistime - dt.timedelta(seconds=time_query[i+1])}})
    #     for item in dataA:
    #         if(item['retweet_count']>=state_rt[i+1] and item['state_rt']*state_multiple[i+1]<item['retweet_count']):
    #             stateData.append((pymongo.UpdateOne(
    #             {
    #                 'id_str':item['id_str']
    #             },
    #             {
    #                 '$set': {
    #                     'state_check':0,
    #                     'state_count':0,
    #                     'state_rt':item['retweet_count'],
    #                     'timeUpdate':thistime
    #                 }
    #             },upsert=True)))
    #             db.retweet_state_data.insert_one({
    #                 'university':item['university'],
    #                 'id_str':item['id_str'],
    #                 'retweet_count':item['retweet_count'],
    #                 'favorite_count':item['favorite_count'],
    #                 'state':0,
    #                 'timeCreate':thistime,
    #                 'timeUpdate':thistime - dt.timedelta(seconds=60)
    #             })
    #         else:
    #             if(item['state_count'] == state_count[i]):
    #                 stateData.append((pymongo.UpdateOne(
    #                 {
    #                     'id_str':item['id_str']
    #                 },
    #                 {
    #                     '$set': {
    #                         'state_check':state_check[i]+1,
    #                         'state_count':0,
    #                         'state_rt':item['retweet_count'],
    #                         'timeUpdate':thistime
    #                     }
    #                 },upsert=True)))
    #             else:
    #                 stateData.append((pymongo.UpdateOne(
    #                 {
    #                     'id_str':item['id_str']
    #                 },
    #                 {
    #                     '$set': {
    #                         'state_count':item['state_count']+1,
    #                         'state_rt':item['retweet_count'],
    #                         'timeUpdate':thistime
    #                     }
    #                 },upsert=True)))
    
    # if(len(stateData)>0):
    #     db.retweet_update_data.bulk_write(stateData,ordered=False)
    # if(len(stateData2)>0):
    #     db.retweet_state_data.bulk_write(stateData2,ordered=False)

        