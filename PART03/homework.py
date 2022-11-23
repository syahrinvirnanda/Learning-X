from pymongo import MongoClient
client = MongoClient('mongodb+srv://syahrinvirnanda:syahrin123@cluster0.ar4suzr.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta  

db.books.insert_one({
    'title': 'Harry Potter', 
    'author': 'J.K. Rowling',
    'rating': 90
})

db.books.insert_one({
    'title': 'The Fisherman and the Fish', 
    'author': 'Joseph Choi',
    'rating': 10
})

db.books.insert_one({
    'title': 'Fire in the Water', 
    'author': 'Some Dude',
    'rating': 57
})

db.books.update_one(
    { 'title': 'The Fisherman and the Fish'},
    {'$set': {'author': 'Jimmy Kim'}}
)

db.books.delete_one({'rating': 90})

