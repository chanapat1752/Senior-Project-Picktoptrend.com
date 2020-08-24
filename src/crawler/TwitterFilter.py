# In[]:
# -*- coding: utf-8 -*-
import io
import json
import smtplib
import pymongo
from pymongo import MongoClient
from TwitterAPI import TwitterAPI
import datetime as dt
import requests
from urllib3.exceptions import ProtocolError
import DataCleansing
import time

# In[]:
# client = MongoClient('mongodb://localhost:27017/University')
client = MongoClient('mongodb://superadmin:4rFV5tGB@0.0.0.0:27017/University?authSource=admin')
db = client.University

#In[]:
#ประกาศ API ที่ใช้งาน
api = []
with io.open("filterAPI.json",encoding="utf-8") as json_file:
    apiData = json.load(json_file)

for allApi,token in apiData.items():
    api.append(TwitterAPI(token['consumer_key'], token['consumer_secret'], token['access_token_key'], token['access_token_secret']))

# In[]:
with io.open("keywordFilter.json", encoding="utf-8") as json_file:
    twData = json.load(json_file)
    
# In[]:
TRACK_TERM = "มหิดล","ลูกพระบิดา","#ทีมMU","#มหิดล","#ทีมมหิดล","#มหาวิทยาลัยมหิดล","ม.มหิดล","#Mahidol","#WeMahidol","#โควตามหิดล","จุฬา","มหาลัยสีชมพู","มหาลัยแถวสามย่าน","เด็กสามย่าน","ลูกพระเกี้ยว","ลูกจามจุรี","ทีมCU","ทีมฬ","#จุฬา","#มหาลัยสีชมพู","#เด็กสามย่าน","#ลูกพระเกี้ยว","#ลูกจามจุรี","#ทีมCU","#ทีมcu","#ทีมฬ","#ทีมจุฬา","#cutep","ม.จุฬา","ลูกพระพิรุณ","มเกษตร","เกษตรศาสตร์","#ทีมมก","#ทีมku","เกษตรบางเขน","#ลูกพระพิรุณ","#มเกษตร","#เกษตรศาสตร์","#มก","#ทีมเกษตร","#เกษตรบางเขน","#เกษตรกำแพงแสน","#ทีมเกษตรศาสตร์","#Kasetsart","#ทีมเกษตรกําแพงแสน","ม.เกษตร","#มหาวิทยาลัยเกษตรศาสตร์","#มช","มเชียงใหม่","#ทีมมช","ทีมCMU","#มเชียงใหม่","ม.เชียงใหม่","#ทีมCMU","#มหาวิทยาลัยเชียงใหม่","#มข","ลูกเจ้าพ่อมอดินแดง","มขอนแก่น","#ทีมมข","ทีมKKU","#ทีมKKU","#ลูกเจ้าพ่อมอดินแดง","#มขอนแก่น","ม.ขอนแก่น","#มหาวิทยาลัยขอนแก่น","มหาวิทยาลัยขอนแก่น","ธรรมศาสตร์","ลูกแม่โดม","พ่อปรีดี","ศิษย์อาจารย์ป๋วย","#มธ","#ทีมมธ","#ทีมTU","#ทีมTu","#ทีมtu","#ธรรมศาสตร์","#ลูกแม่โดม","#พ่อปรีดี","#ศิษย์อาจารย์ป๋วย","#มหาวิทยาลัยธรรมศาสตร์","ม.ธรรมศาสตร์","มธ","มธ.","มศว","ทีมSWU","มหาวิทยาลัยศรีนครินทรวิโรฒ","#มศว","#ทีมSWU","#มหาวิทยาลัยศรีนครินทรวิโรฒ","#ทีมมศว","มมส","ทีมMSU","#มมส","#ทีมMSU","#มหาวิทยาลัยมหาสารคาม","มบูร","ทีมบูรพา","ทีมBUU","#มบูร","#ทีมบูรพา","#ทีมBUU","#มหาวิทยาลัยบูรพา","มอบู","#มอบู","มฟล","เด็กดอยแง่ม","มแม่ฟ้าหลวง","ทีมMFU","#มฟล","#มแม่ฟ้าหลวง","#ทีมMFU","#ทีมมฟล","#ทีมแม่ฟ้าหลวง","#แม่ฟ้าหลวง","ม.แม่ฟ้าหลวง"


# In[]:
def getRawTwitter():
    for i in range(len(api)):
        try:
            print('API ',i+1)
            r = api[i].request('statuses/filter', {'track': TRACK_TERM,'extended_tweet':'full_text'})
            for item in r:
                tweet = item['text']
                university = 'empty'
                keyword = 'empty'
                rt = "",tweet[0],tweet[1]
                if not("R" == rt[1] and "T" == rt[2]):
                        if "extended_tweet" in item:
                            for key, value in twData.items():
                                for kw in value:
                                    if kw.lower() in item['extended_tweet']['full_text']:
                                        university = key
                                        keyword = kw
                            if university != 'empty':
                                db.tweetFilter_raw_data.delete_many({'addData':'incomplete'})
                                db.tweetFilter_raw_data.insert_one(
                                        {
                                            'university':university,
                                            'keyword':keyword,
                                            'id_str': item['id_str'],
                                            'data':item,
                                            'timeUpdate':dt.datetime.today(),
                                            'addData':'incomplete'
                                        })
                                print(university ,' add Extend Tweet')
                        else:
                            for key, value in twData.items():
                                for kw in value:
                                    if kw.lower() in item['text']:
                                        university = key
                                        keyword = kw
                            if university != 'empty':
                                db.tweetFilter_raw_data.delete_many({'addData':'incomplete'})
                                db.tweetFilter_raw_data.insert_one(
                                        {
                                            'university':university,
                                            'keyword':keyword,
                                            'id_str': item['id_str'],
                                            'data':item,
                                            'timeUpdate':dt.datetime.today(),
                                            'addData':'incomplete'
                                        })
                                print(university ,' add Tweet')
                        DataCleansing.tweetFilterCleansing()
                else:
                        if "extended_tweet" in item['retweeted_status']:
                            for key, value in twData.items():
                                for kw in value:
                                    if kw.lower() in item['retweeted_status']['extended_tweet']['full_text']:
                                        university = key
                                        keyword = kw
                            if university != 'empty':
                                db.retweet_raw_data.insert_one(
                                        {
                                            'university':university,
                                            'keyword':keyword,
                                            'id_str': item['id_str'],
                                            'data':item,
                                            'timeUpdate':dt.datetime.today(),
                                            'addData':'incomplete'
                                        })
                                print(university ,' add Reweet')
                        else:
                            for key, value in twData.items():
                                for kw in value:
                                    if kw.lower() in item['retweeted_status']['text']:
                                        university = key
                                        keyword = kw
                            if university != 'empty':
                                db.retweet_raw_data.insert_one(
                                        {
                                            'university':university,
                                            'keyword':keyword,
                                            'id_str': item['id_str'],
                                            'data':item,
                                            'timeUpdate':dt.datetime.today(),
                                            'addData':'incomplete'
                                        })
                                print(university ,' add Reweet')
                        DataCleansing.retweetFilterCleansing()
        except:
            next     


# In[ ]:
if __name__ == '__main__':
    while True: 
        try:
            getRawTwitter()
        except:
            time.sleep(30)