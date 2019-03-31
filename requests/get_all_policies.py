import requests
import json
import psycopg2
import tqdm




connect = psycopg2.connect(database='***', user='***', host='***', port='***', password='***')
cursor = connect.cursor()

cursor.execute("select id, phone\
               from users\
               where id not in (\
               select user_id \
               from policies\
                   where action_id = 1)\
               ")


users_ids = list()

for i in cursor:
    users_ids.append(i)


true = True


token = '***'
base_url = 'https://office.millionagents.com'
method='/api/auth/update_user_policies'
hdrs = {'Content-Type': 'application/json; charset=utf-8',
           'X-TOKEN': token }


for i in tqdm.tqdm(users_ids):
    r = requests.post(base_url+method, headers=hdrs,
    data=json.dumps({"policies": {"1":true,"18":true, "21":true}, "user_id": int(i[0])}))
    print(r.text)