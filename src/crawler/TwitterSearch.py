# In[ ]:
import io
from TwitterAPI import TwitterAPI
import pymongo
from pymongo import MongoClient
import json
import datetime as dt
import time
import DataCleansing

#In[]:
#เรียกใช้ database ใน mongo
client = MongoClient('mongodb://localhost:27017/University')
# client = MongoClient('mongodb://superadmin:4rFV5tGB@0.0.0.0:27017/University?authSource=admin')
db = client.University
#สร้างดัชนี (Index) ให้กับ data
db.tweet_raw_data.create_index([('id_str', pymongo.ASCENDING)], unique=True)

#In[]:
#ดึงข้อมูล keyword ที่อยู่ใน json
with io.open("keywordSearch.json",encoding="utf-8") as json_file:
    twData = json.load(json_file)

#In[]:
#ประกาศ API ที่ใช้งาน
api = []
with io.open("searchAPI.json",encoding="utf-8") as json_file:
    apiData = json.load(json_file)

for allApi,token in apiData.items():
    api.append(TwitterAPI(token['consumer_key'], token['consumer_secret'], token['access_token_key'], token['access_token_secret']))

#In[]:
def getRawTwitter():
    rawData = []
    for i in range(len(api)):
        try:
            t0 = time.time()
            for key, value in twData.items():
                for val in value:
                    kw = val +" -filter:retweets"
                    r = api[i].request('search/tweets', {'q':kw,'lang':'th','tweet_mode':'extended','count':'100'})
                    for item in r:
                        try:
                            db.tweet_raw_data.insert_one(
                                {
                                    'university':key,
                                    'keyword':val,
                                    'id_str': item['id_str'],
                                    'data':item,
                                    'timeUpdate':dt.datetime.today(),
                                    'addData':'incomplete'
                                })
                        except pymongo.errors.DuplicateKeyError:
                            rawData.append((pymongo.UpdateOne(
                                {
                                    'id_str':item['id_str']
                                },
                                {
                                    '$set': {
                                        'data':item,
                                        'timeUpdate':dt.datetime.today(),
                                        'addData':'incomplete'
                                    }
                                },upsert=True)))
            if(len(rawData)>0):
                db.tweet_raw_data.bulk_write(rawData,ordered=False)
                rawData = []
            DataCleansing.tweetSearchCleansing()
            time.sleep(20)
            t1 = time.time()
            print('API-',i+1,': %f'%(t1-t0))
        except:
            print('Next API')
            next

# In[ ]:
if __name__ == '__main__':
    while True:
        getRawTwitter()         
