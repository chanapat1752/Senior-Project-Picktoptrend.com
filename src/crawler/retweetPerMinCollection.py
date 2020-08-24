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


#In[]:
def getRetweetPerMinute(thistime):
    time.sleep(2)
    dataA = db.retweet_update_data.find({'state_check':0})
    for item in dataA:
        db.retweet_state_data.insert_one(
            {
                'university':item['university'],
                'id_str':item['id_str'],
                'retweet_count':item['retweet_count'],
                'favorite_count':item['favorite_count'],
                'timeUpdate':thistime
            }
        )
    dataB = db.retweet_state_data.aggregate([
            { "$group": {
                "_id": "$id_str",
                "retweetNow": { 
                    "$sum": { 
                        "$cond": [
                            { "$gte": [ "$timeUpdate", thistime - dt.timedelta(seconds=30) ] },
                            "$retweet_count", 
                            0
                        ]
                    }
                },
                "retweetPrevious": { 
                    "$sum": { 
                        "$cond": [
                            { "$lte": [ "$timeUpdate", thistime - dt.timedelta(seconds=30)] },
                            "$retweet_count", 
                            0
                        ]
                    }
                },
                "favouriteNow": { 
                    "$sum": { 
                        "$cond": [
                            { "$gte": [ "$timeUpdate", thistime - dt.timedelta(seconds=30) ] },
                            "$favorite_count", 
                            0
                        ]
                    }
                },
                "favouritePrevious": { 
                    "$sum": { 
                        "$cond": [
                            { "$lte": [ "$timeUpdate", thistime - dt.timedelta(seconds=30)] },
                            "$favorite_count", 
                            0
                        ]
                    }
                }
            }},
            { "$project": {
                "retweetInThisMin": { "$subtract": [ "$retweetNow", "$retweetPrevious" ] },
                "favouriteInThisMin": { "$subtract": [ "$favouriteNow", "$favouritePrevious" ] }
            }}
        ])
    dataC = db.retweet_state_data.aggregate([
            { "$group": {
                "_id": "$university",
                "retweetNow": { 
                    "$sum": { 
                        "$cond": [
                            { "$gte": [ "$timeUpdate", thistime - dt.timedelta(seconds=30) ] },
                            "$retweet_count", 
                            0
                        ]
                    }
                },
                "retweetPrevious": { 
                    "$sum": { 
                        "$cond": [
                            { "$lte": [ "$timeUpdate", thistime - dt.timedelta(seconds=30)] },
                            "$retweet_count", 
                            0
                        ]
                    }
                },
            }},
            { "$project": {
                "retweetInThisMin": { "$subtract": [ "$retweetNow", "$retweetPrevious" ] }
            }}
        ])
    db.retweet_state_data.delete_many({'timeUpdate':{'$lte':thistime - dt.timedelta(seconds=30)}})
    for item in dataB:
        k = db.retweet_update_data.find_one({'id_str':item['_id']})
        retweet = item['retweetInThisMin']
        favorite = item['favouriteInThisMin']
        if(retweet<0):
            retweet = 0
        if(favorite<0):
            favorite = 0
        db.retweet_permin_data.insert_one(
                {
                'university':k['university'],
                'id_str':item['_id'],
                'retweet':retweet,
                'favourite':favorite,
                'timeUpdate':thistime
                }
            )

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

    for item in dataC:
        retweet = item['retweetInThisMin']
        if(retweet<0):
            retweet = 0
        if item['_id']=='Chula':
            chula = retweet
        elif item['_id']=='Mahidol':
            mahidol = retweet
        elif item['_id']=='Kasetsart':
            kasetsart = retweet
        elif item['_id']=='Chiang Mai':
            chiangMai = retweet
        elif item['_id']=='Khon Kaen':
            khonKaen = retweet
        elif item['_id']=='Thammasat':
            thammasat = retweet
        elif item['_id']=='Srinakharinwirot':
            srinakharinwirot = retweet
        elif item['_id']=='Mahasarakham':
            Mahasarakham = retweet
        elif item['_id']=='Burapha':
            Burapha = retweet
        elif item['_id']=='Mae Fah Luang':
            maeFahLuang = retweet

    db.uni_count_permin_data.insert_one(
            {
                "Time":str(thistime.day)+'-'+str(thistime.month)+'-'+str(thistime.year)+'-'+str(thistime.hour)+'-'+str(thistime.minute),
                "มหาวิทยาลัยธรรมศาสตร์":thammasat,
                "จุฬาลงกรณ์มหาวิทยาลัย":chula,
                "มหาวิทยาลัยมหิดล":mahidol,
                "มหาวิทยาลัยเกษตรศาสตร์":kasetsart,
                "มหาวิทยาลัยเชียงใหม่":chiangMai,
                "มหาวิทยาลัยขอนแก่น":khonKaen,
                "มหาวิทยาลัยศรีนครินทรวิโรฒ":srinakharinwirot,
                "มหาวิทยาลัยมหาสารคาม":Mahasarakham,
                "มหาวิทยาลัยบูรพา":Burapha,
                "มหาวิทยาลัยแม่ฟ้าหลวง":maeFahLuang,
                "timeUpdate":thistime
            }
        )     
    

