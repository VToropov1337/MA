import psycopg2 as pg
import pandas as pd


df = pd.read_csv('metro.csv',sep=',')

dfm = df[(df['Промо отметка (1 - Да, 0 - нет, 2 - скрытая)'] == 1) & (df['Competiror desc'] == 'Magnit')]

arr = dfm['Фото'].tolist()

qq = list()
for i in arr:
    qq.append(i.split('/'))


reports_ids = list()
for i in qq:
    if i[4] not in reports_ids:
        reports_ids.append(int(i[4]))


zz = ()

for i in qq:
    if int(i[4]) not in zz:
        zz += (int(i[4]),)


request ="SELECT CONCAT_WS('','https://ma-metro.millionagents.com/data2/answer/image/', answer_files.id, '/', file) as url\
 FROM ma_metro.reports r \
INNER JOIN ma_metro.reports r2 \
    ON r.id = r2.origin_report_id \
INNER JOIN ma_metro.tasks t \
ON r2.task_id = t.id \
JOIN ma_metro.answer_files \
    ON answer_files.id = r2.metro_price_photo_id \
INNER JOIN ma_metro.geo_objects \
    ON t.geo_object_id = geo_objects.id \
WHERE t.project_id = 2 \
AND r2.id IN {} \
;".format(zz)

connection = pg.connect(host='***',port='***', database='***',user='***',password='***')
df_final = pd.read_sql_query(request, connection)


with open('magnit.html','w') as f:
    for line in df_final['url']:
        line = line.replace('data2','data3')
        f.write("<img style=\"width:300px\" src=\"{}\"/>\n".format(line))
