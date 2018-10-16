import pymongo
        
client = pymongo.MongoClient("127.0.0.1",27018)
db=client.project
def insert(question,options,answer,explanation):
    db.questions.insert_one({"Q":question,"O":options,"A":answer,"E":explanation})
insert("who is the great person",["chandan","vinay","dheemanth","all of the above"],1000,"because he is a legend")
a=list(db.questions.find())
print(a)


