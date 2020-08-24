import pymongo
from pymongo import MongoClient
import datetime as dt
import time
import json
from time import gmtime, strftime


# client = MongoClient('mongodb://localhost:27017/University')
client = MongoClient('mongodb://superadmin:4rFV5tGB@0.0.0.0:27017/University?authSource=admin')
db = client.University

def autoSearch():
    db.autocomplete_search.delete_many({})
    uni = ['มหาวิทยาลัยธรรมศาสตร์','จุฬาลงกรณ์มหาวิทยาลัย','มหาวิทยาลัยมหิดล','มหาวิทยาลัยเกษตรศาสตร์','มหาวิทยาลัยเชียงใหม่','มหาวิทยาลัยขอนแก่น'
    ,'มหาวิทยาลัยศรีนครินทรวิโรฒ','มหาวิทยาลัยมหาสารคาม','มหาวิทยาลัยบูรพา','มหาวิทยาลัยแม่ฟ้าหลวง']
    for i in uni:
        db.autocomplete_search.insert_one({
            "name": i
        })
    dataA = db.wordCloud_UI.find({})
    for i in dataA:
        db.autocomplete_search.insert_one({
            "name":'#'+i['text']
        })