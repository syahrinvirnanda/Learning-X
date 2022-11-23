from pymongo import MongoClient

client = MongoClient('mongodb+srv://syahrinvirnanda:syahrin123@cluster0.ar4suzr.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta  

# doc1 = {'name': 'syahrin','age': 16 }
# doc2 = {'name': 'naja','age': 17 }
# doc3 = {'name': 'daus','age': 18 }

# db.users.insert_one(doc1)
# db.users.insert_one(doc2)
# db.users.insert_one(doc3)

# all_users = list(db.users.find({}, {'_id': False}))

# # print(all_users)
# # print(all_users[0]['name'])
# for user in all_users:
#     print(user)
# user = db.users.find_one({ 'name': 'syahrin' })

# print(user)
# db.users.update_one({'name': 'syahrin'}, {'$set': {'age': 17}})

# user = db.users.find_one({'name': 'syahrin'})
# print(user)

# db.users.delete_one({'name': 'syahrin'})

user = db.users.find_one({'name': 'syahrin'})
print(user)