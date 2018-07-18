import psycopg2
from openpyxl import Workbook
import json

connect = psycopg2.connect(database='***', user='***', host='***', port='***', password='***')
cursor = connect.cursor()
cursor.execute(

#запрос в бд
"SELECT \
CONCAT_WS('','https://***/***/***/answer/image/', answer_files.id, '/', file) as url,reports.id as report_id, geo_objects.title \
FROM ma_metro.reports \
JOIN ma_metro.tasks \
ON reports.task_id = tasks.id \
JOIN ma_metro.geo_objects \
ON tasks.geo_object_id = geo_objects.id \
JOIN ma_metro.answers \
ON answers.report_id = reports.id \
JOIN ma_metro.answer_files \
ON answers.id = answer_files.answer_id \
WHERE reports.id \
IN (range) \
AND \
answers.key = 'key'")




#пустой массив
arr = list()

#бегу по объекту и создаю хэши по ключам
for i in cursor:
    hh = dict()
    hh['url'] = i[0]
    hh['report_id'] = i[1]
    hh['store_title'] = i[2]
    arr.append(hh)


#массив хэшей
print(arr)

with open('export_photos.json', 'w') as f:
    #f.write(str(arr))
    json.dump(arr, f)
