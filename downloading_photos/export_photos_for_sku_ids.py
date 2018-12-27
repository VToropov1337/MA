import psycopg2
import requests
import os
from PIL import Image
from io import BytesIO


connect = psycopg2.connect(database='***', user='***', host='***', port='***', password='***')
cursor = connect.cursor()


cursor.execute(" \
SELECT article_id, g.title, g.id, metro_price_photo_id,CONCAT_WS('','https://***.com/***/***/***/***/***/', answer_files.id, '/', file) as url, r.id \
FROM ma_metro.tasks t \
INNER JOIN ma_metro.reports r \
	ON r.task_id=t.id \
INNER JOIN ma_metro.answer_files \
	ON answer_files.id = r.metro_price_photo_id \
INNER JOIN ma_metro.geo_objects g \
	ON g.id = t.geo_object_id \
WHERE  t.project_id=2 \
AND  r.article_id::text in (\
		SELECT DISTINCT (unnest(active_article_ids)) \
		FROM ma_metro.tasks WHERE wave='S6-18-50' LIMIT 20) \
AND r.created_at>'2018-01-01' \
AND r.metro_available = True \
GROUP BY g.title, r.article_id,g.id, metro_price_photo_id,answer_files.id,r.id")


article_id = list()
data = list()
geo_object_id = list()

for i in cursor:
    if i[0] not in article_id:
        article_id.append(i[0])
    if i[2] not in geo_object_id:
        geo_object_id.append(i[2])
    data.append(i)



def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


path = os.getcwd()

for i in article_id:
    os.mkdir('{}'.format(i))

for i in range(len(data)):
    createFolder(path+'/{}/{}'.format(data[i][0],data[i][2]))




for i in range(len(data)):
    c+=1
    print(c)
    url = data[i][4]
    response = requests.get(url)
    photo = requests.get(url).content
    try:
        Jpegimagefile = Image.open(BytesIO(response.content))
        with open('{}/{}/{}'.format(data[i][0],data[i][2],data[i][5]) + '.jpg', 'wb') as f:
            f.write(photo)
            print('good')
    except OSError:
        url = url.replace('data2','data3')
        response = requests.get(url)
        photo = requests.get(url).content
        Jpegimagefile = Image.open(BytesIO(response.content))
        with open('{}/{}/{}'.format(data[i][0], data[i][2], data[i][5]) + '.jpg', 'wb') as f:
            f.write(photo)
        print('link was changed')
