import pymongo
from pymongo import MongoClient
import datetime as dt
import time
import json
from time import gmtime, strftime

import GetGraph
import GetWordclouds
import GetAutoComplete
import GetCard
import GetTopTweet
import retweetPerMinCollection
import BackupData
import checkStateData


if __name__ == "__main__":
    timestamp = 1591093200000 #PerHour
    while True:
        curr_datetime = dt.datetime.now()
        if(curr_datetime.second == 0):
                t0 = time.time()
                print('checkstate')
                checkStateData.checkState(curr_datetime)
                time.sleep(1)
                print('updateretweetPermin')
                retweetPerMinCollection.getRetweetPerMinute(curr_datetime)
                time.sleep(1)
                if(curr_datetime.minute%10==5):
                    print('GenCard')
                    GetCard.card(curr_datetime)
                    print('GenWordCloud')
                    GetWordclouds.wordcloudUI(curr_datetime)
                    GetWordclouds.checkDirty()
                    print('GenSearch')
                    GetAutoComplete.autoSearch()
                if(curr_datetime.minute%10==0):
                    print('GenUI')
                    GetGraph.retweetUI(curr_datetime ,timestamp)
                    GetGraph.tweetUI(curr_datetime ,timestamp)
                    print('GenBarGraph')
                    GetGraph.barCountUI(curr_datetime)
                    time.sleep(1)
                    print('GenTopTweetIn60Min')
                    GetTopTweet.toptrend(curr_datetime)
                    timestamp += 600000
                if(curr_datetime.minute%10==2):
                    print('GenTopTweetIn1Day')
                    GetTopTweet.getTopTrendInOneDay(curr_datetime)
                t1 = time.time()
                t2 = t1-t0
                print(t2)
        if(curr_datetime.second == 30 and curr_datetime.minute == 0 and curr_datetime.hour == 0):
            print('backup')
            glo_time = dt.datetime.today()
            BackupData.BackupDataMaster(glo_time)
            BackupData.deleteRaw(glo_time)
            time.sleep(1)
    