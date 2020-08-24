# In[ ]:
# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import datetime as dt
import time

#In[]:
# client = MongoClient('mongodb://localhost:27017/University')
# client = MongoClient('mongodb://superadmin:4rFV5tGB@0.0.0.0:27017/University?authSource=admin')
client = MongoClient('mongodb://superadmin:4rFV5tGB@45.32.105.145:27017/Covid?authSource=admin')
db = client.University
university =["Mahidol","Chula","Kasetsart","Chiang Mai","Khon Kaen","Thammasat","Srinakharinwirot","Mahasarakham","Burapha","Mae Fah Luang"]
#In[]:
def dataAnalytic():
    thistime = dt.datetime.today()
    for i in university:
        dataA = db.uni_count_permin_data.find({'university':i,'timeUpdate':{'$gte':thistime - dt.timedelta(minutes=15)}})
        if dataA.count() == 15:
            print(i)
            slope = []
            slidingWindow = []
            shiftRight = 2
            countOfSlope = 5
            state = 0
            for j in dataA:
                slope.append(j['retweet'])
            for k in range(6):
                slidingWindow.append(slope[state]+slope[state+1]+slope[state+2]+slope[state+3]+slope[state+4]/countOfSlope)
                state = state + shiftRight
                print(k,'+',slidingWindow[k])
            meanOfSliding = (slidingWindow[2]+slidingWindow[3]+slidingWindow[4]+slidingWindow[5]) / 4
            if slidingWindow[0]*1.5<slidingWindow[1] and slidingWindow[1]>= 4 and meanOfSliding > slidingWindow[1] :
                print('Alert +',i)
                dataB = db.retweet_permin_data.aggregate([
                            {"$match": {"$and" : [{"university": i},{"timeUpdate":{"$gte":thistime - dt.timedelta(minutes=15)}}]}},
                            { "$group": {
                                "_id": "$id_str",
                                "retweetNow": { 
                                "$sum": { 
                                    "$cond": [
                                        { "$gte": [ "$timeUpdate", thistime - dt.timedelta(minutes=15) ] },
                                        "$retweet", 
                                        0
                                    ]
                                }
                            },
                            }},
                        ])
                for item in dataB:
                    if(item['retweetNow']>=meanOfSliding):
                        db.master_data.update_one({"id_str": item['_id']},{"$set": { "trends": True }})  
    
    
    
            
                
                
# In[ ]:
if __name__ == '__main__':
    state = 0
    past_min = dt.datetime.now().minute
    while True:
        curr_datetime = dt.datetime.now()
        curr_min = curr_datetime.minute
        if(past_min != curr_min):
            state = 0
        if(curr_min % 2 == 0 and state == 0 and curr_datetime.second == 15):
            t0 = time.time()
            dataAnalytic()
            t1 = time.time()
            t2 = t1-t0
            print(t2)
            state = 1
            past_min = curr_min