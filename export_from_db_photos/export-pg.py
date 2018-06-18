import psycopg2
from openpyxl import Workbook

#устанавливаю соединение с бд
connect = psycopg2.connect(database='***', user='***', host='***', port='***', password='***')
#объект связи
cursor = connect.cursor()
#запуск запроса в бд
cursor.execute(

"SELECT \
CONCAT_WS('','https://***/data2/answer/image/', a.id, '/', file) concat_ws, barcode \
FROM m10.reports \
JOIN m10.tasks \
ON reports.task_id = tasks.id \
JOIN m10.answer_files a \
ON a.id = reports.metro_price_photo_id \
JOIN m10.answers \
ON a.answer_id = answers.id \
WHERE tasks.wave = 'zhal_chto_ne_na_m54_auchan_zs_may18' \
AND tasks.project_id = 2 \
AND reports.state = 'accepted' \
AND reports.barcode != '' \
;")

arr = list()
hh = dict()

#иду по объекту и заполняю хэш hh значениями, после чего помещаю в массив.
for i in cursor:
    hh['url'] = i[0]
    hh['barcode'] = i[1]
    arr.append(hh)



#записываю в файл
with open('photo_price.txt', 'w') as f:
    f.write(str(arr))
