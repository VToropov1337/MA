import pandas as pd
import requests
import tqdm
import json

df = pd.read_csv('file.csv',sep=';')

print(len(df))
zz = ()

for i in range(len(df)):
    zz += (df.iloc[i]['id'],)


true = True

token = 'token'
base_url = 'https://path'
method='/method'


headerz = {'Content-Type': 'application/json; charset=utf-8',
           'X-TOKEN': token }


for i in tqdm.tqdm(zz):
    r = requests.post(base_url+method, headers=headerz,
    data=json.dumps({"policies": {"18":true, "21":true}, "user_id": int(i)}))
    print(r.text)
