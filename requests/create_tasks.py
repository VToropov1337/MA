import requests
import json
import pandas as pd


token = '***'

params = {'Content-Type': 'application/json; charset=utf-8',
          'X-Authentication-Token': token}

base_url = 'https://***/***/api/***/***/***/'

# создание 1 таска
create = '/tasks'

arr = [16545,
 16544,
 10100,
 16546,
 9029,
 3190,
 14997,
 1138,
 1122,
 11859,
 16468,
 16540,
 16539,
 16542,
 16541,
 16466,
 16459,
 16460,
 16465,
 16467,
 2456,
 4202,
 606,
 16543,
 607,
 16462,
 16461,
 16464,
 16463,
 10239,
 3401]


for i in arr:
    r = requests.post(base_url + create, headers=params,
                 data = json.dumps({"task":{"project_id":82,
                                    "state":"active",
                                    "priority":0,
                                    "title":"Сбор данных о кассах",
                                    "description":"В данном задании вам необходимо посчитать количество всех касс в указанной торговой точке.",
                                    "reports_per_worker":1,
                                    "geo_object_id":i,
                                    "temp":{"payment_project_id":12}
                                    }}))

    print(r)