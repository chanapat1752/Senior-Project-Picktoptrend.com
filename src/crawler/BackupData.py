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
client = MongoClient('mongodb://superadmin:4rFV5tGB@45.32.105.145:27017/University?authSource=admin')
db = client.University

#In[]:
def BackupDataMaster(glo_time):
    backup = []
    backup2 = []
    backup3 = []
    idData=[]
    current_date = strftime("%Y-%m-%d", gmtime())
    # dataA = db.master_data.find({'timeUpdate': {'$lte': glo_time - dt.timedelta(hours=72)}})
    # for i in dataA:
    #     idData.append(i['id_str'])
    #     i['_id'] = str(i['_id'])
    #     backup.append(i) 
    # filename=current_date+' backup university.json'
    # with open(filename, 'w', encoding='utf-8') as f:
    #     json.dump(backup, f, ensure_ascii=False, indent=4,default=str)
    # db.master_data.delete_many({"id_str": {"$in": idData}})
    # db.retweet_update_data.delete_many({"id_str": {"$in": idData}})

    dataB = db.retweet_permin_data.find({'timeUpdate': {'$lte': glo_time - dt.timedelta(hours=24)}})
    for i in dataB:
        i['_id'] = str(i['_id'])
        backup2.append(i)
    filename2=current_date+' backup tweet_per_minute.json'
    with open(filename2, 'w', encoding='utf-8') as f:
        json.dump(backup2, f, ensure_ascii=False, indent=4,default=str)

    dataC = db.uni_count_permin_data.find({'timeUpdate': {'$lte': glo_time - dt.timedelta(hours=24)}})
    for i in dataC:
        i['_id'] = str(i['_id'])
        backup3.append(i)
    filename3=current_date+' backup Uni_per_minute.json'
    with open(filename3, 'w', encoding='utf-8') as f:
        json.dump(backup3, f, ensure_ascii=False, indent=4,default=str)
    db.retweet_permin_data.delete_many({'timeUpdate': {'$lte': glo_time - dt.timedelta(hours=24)}})
    db.uni_count_permin_data.delete_many({'timeUpdate': {'$lte': glo_time - dt.timedelta(hours=24)}})

def deleteRaw(glo_time):
    db.tweet_raw_data.delete_many({'timeUpdate': {'$lte': glo_time - dt.timedelta(hours=72)}})
    db.retweet_raw_data.delete_many({'timeUpdate': {'$lte': glo_time - dt.timedelta(hours=72)}})
    db.tweetFilter_raw_data.delete_many({'timeUpdate': {'$lte': glo_time - dt.timedelta(hours=72)}})

if __name__ == "__main__":
    deleteRaw(dt.datetime(2020, 5, 10, 0, 0, 0, 0))