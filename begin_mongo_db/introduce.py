
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

#insers a value
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))



#find a data
posts.find_one({'author': 'Scott'})



#insert a many values
post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}
new_result = posts.insert_many([post_1, post_2, post_3])
print('Multiple posts: {0}'.format(new_result.inserted_ids))

#find a data
bills_post = posts.find_one({'author': 'Bill'})
print(bills_post)


#this is a cursor object
scotts_posts = posts.find({'author': 'Scott'})
print(scotts_posts)

#iteration 
for post in scotts_posts:
    print(post)

