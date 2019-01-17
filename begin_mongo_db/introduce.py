
'''start a mongo
in shell enter: mongod
'''


import requests, json , pymongo
from pymongo import MongoClient



client = MongoClient()

#or
client = MongoClient('localhost', 27017)

#or
client = MongoClient('mongodb://localhost:27017')

#create a db
db = client.pymongo_test

#or
db = client['pymongo_test']


#create a collection
posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}


result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))



#find a data
posts.find_one({'author': 'Scott'})