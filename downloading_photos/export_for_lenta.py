import psycopg2
import requests
import os

connect = psycopg2.connect(database='***', user='***', host='***', port='***', password='***')
cursor = connect.cursor()


cursor.execute("SELECT  reports.id as report_id,CONCAT_WS('','https://***.com/***/***/image/', answer_files.id, '/', file) as url,answers.key,answer_files.id, geo_objects.title, geo_objects.id FROM m10.reports \
JOIN m10.tasks \
ON reports.task_id = tasks.id \
JOIN m10.geo_objects \
ON tasks.geo_object_id = geo_objects.id \
JOIN m10.answers \
ON answers.report_id = reports.id \
JOIN m10.answer_files \
ON answers.id = answer_files.answer_id \
WHERE tasks.project_id = 6\
AND tasks.wave = 'lm_5118_fs_dim'\
AND tasks.geo_object_id IN (223,632,603,633,634)\
AND reports.state = 'pending'\
")

arr = list()
arr2 = list()

c = 0
for i in cursor:
    arr.append(i)
    c+=1

KEYS = {'photo_overview':'фасад_магазина',
        'photo_overview_oil':'весь отдел',
        'photo_overview_olive_oil':'весь отдел',
        'photo_detailed_oil':'выкладка',
        'photo_detailed_olive_oil':'выкладка',
        'photo_additional_oil':'доп.выкладка',
        'photo_additional_oil':'доп.выкладка',
        'photo_promo_oil': 'Промо-материалы',
        'photo_promo_olive_oil': 'Промо-материалы',
        'photo_floor_tile':'Фото плитки',
        'photo_lenght_olive_oil':'Замеры оборудования',
        'photo_lenght_oil':'Замеры оборудования'
        }

SHOPS = list()

for i in arr:
    if i[4] not in SHOPS:
        SHOPS.append(i[4])
    hh = dict()
    if i[2] in KEYS:
        hh['url'] = i[1]
        hh['key'] = i[2]
        hh['title'] = i[4]
        arr2.append(hh)

path = os.getcwd()
for i in SHOPS:
    os.mkdir(i)

for i in range(len(arr2)):
    url = arr2[i]['url']
    r = requests.get(url).content
    with open('{}/{}'.format(arr2[i]['title'],arr2[i]['title'] + '_'+KEYS[arr2[i]['key']]+'_'+'{}'.format(i)+'.jpg'), 'wb') as f:
        f.write(r)
