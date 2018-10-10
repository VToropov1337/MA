import psycopg2
from openpyxl import Workbook
import json

connect = psycopg2.connect(database='***', user='***', host='***', port='***', password='***')
cursor = connect.cursor()






cursor.execute("SELECT CONCAT_WS('','https://***.com/data2/***/image/', answer_files.id, '/', file) as url,reports.id as report_id, geo_objects.title FROM m10.reports \
JOIN m10.tasks \
ON reports.task_id = tasks.id \
JOIN m10.geo_objects \
ON tasks.geo_object_id = geo_objects.id \
JOIN m10.answers \
ON answers.report_id = reports.id \
JOIN m10.answer_files \
ON answers.id = answer_files.answer_id \
WHERE tasks.project_id = 1\
AND tasks.wave = '***'\
AND tasks.geo_object_id = 128\
AND answers.key = 'photo_price'\
LIMIT 1000;")



arr = list()


for i in cursor:
    hh = dict()
    hh['url'] = i[0]
    hh['report_id'] = i[1]
    hh['store_title'] = i[2]
    arr.append(hh)



print(arr)

with open('xxx.json', 'w') as f:
    json.dump(arr, f)
