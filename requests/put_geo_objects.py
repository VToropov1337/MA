import requests
import json
from tqdm import tqdm

arr = list()
arr2 = list()

with open('go2.txt','r') as f:
    for line in f.readlines():
        arr.append(line.strip().split(','))
		
with open('go.txt','r') as f:
    for line in f.readlines():
        arr.append(line.strip().split(','))


    
token = 'token'
base_url = 'https://***/api/***/***/***/***'
params = {'Content-Type': 'application/json; charset=utf-8',
           'X-Authentication-Token': token }


for i in tqdm(arr):

    all = '/geo_objects/{}'.format(i[0])
    r = requests.put(base_url + all, headers=params,
	                  data=json.dumps({"geo_object": {"id": "{}".format(i[0]),"local_coefficient":"{}".format(i[1])}}))
    print(r)
	

for i in tqdm(arr2):

    all = '/geo_objects/{}'.format(i[0])
    r = requests.put(base_url + all, headers=params,
	                  data=json.dumps({"geo_object": {"id": "{}".format(i[0]),"regional_category_id":"{}".format(i[1])}}))
    print(r)