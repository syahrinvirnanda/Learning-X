from pymongo import MongoClient
client = MongoClient('mongodb+srv://syahrinvirnanda:syahrin123@cluster0.ar4suzr.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta  

doc = {
    'name': 'syahrin',
    'age': 16
}

db.users.insert_one(doc)