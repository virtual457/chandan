import pymongo
client = pymongo.MongoClient("127.0.0.1",27017)
db=client.miniproject
def insert(key,value):
    db.keyvalue.insert_one({"KEY":key,"VALUE":value})