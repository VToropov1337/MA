import psycopg2
import json

connect = psycopg2.connect(database=***, user=***, host=***, port=***, password=***)
cursor = connect.cursor()

cursor.execute("SELECT DISTINCT(r2.article_id),\
    CONCAT_WS('','https://***/***/answer/image/', answer_files.id, '/', file) as url,r2.id \
    FROM ma_metro.reports r \
    INNER JOIN ma_metro.reports r2 \
	    ON r.id = r2.origin_report_id \
    INNER JOIN ma_metro.tasks t \
	    ON r2.task_id = t.id \
    JOIN ma_metro.answer_files \
        ON answer_files.id = r2.metro_price_photo_id \
    INNER JOIN ma_metro.geo_objects \
        ON t.geo_object_id = geo_objects.id \
    WHERE r2.state = 'accepted'\
    AND r2.promo_price > 0\
    AND geo_objects.title = '***'\
    AND t.wave IN ('os_auchan_46-18','os_auchan_44-18','os_auchan_42-18','os_auchan_40-18')\
    LIMIT 4435")



arr = list()


for i in cursor:
    hh = dict()
    hh['store_title'] = '***'
    hh['source'] = i[1]
    arr.append(hh)



print('promo',len(arr))

with open('***_promo.json', 'w') as f:
    json.dump(arr, f)


cursor.execute("SELECT DISTINCT(r2.article_id),\
    CONCAT_WS('','https://***/***/answer/image/', answer_files.id, '/', file) as url \
    FROM ma_metro.reports r \
    INNER JOIN ma_metro.reports r2 \
	    ON r.id = r2.origin_report_id \
    INNER JOIN ma_metro.tasks t \
	    ON r2.task_id = t.id \
    JOIN ma_metro.answer_files \
        ON answer_files.id = r2.metro_price_photo_id \
    INNER JOIN ma_metro.geo_objects \
        ON t.geo_object_id = geo_objects.id \
    WHERE r2.state = 'accepted'\
    AND r2.promo_price IS NULL \
    AND geo_objects.title = '***'\
    AND t.wave IN ('os_auchan_46-18','os_auchan_44-18','os_auchan_42-18','os_auchan_40-18')\
    LIMIT 4435")


arr2 = list()


for i in cursor:
    hh2 = dict()
    hh2['store_title'] = '***'
    hh2['source'] = i[1]
    arr2.append(hh2)



print('reg',len(arr2))

with open('***_reg.json', 'w') as f:
    json.dump(arr2, f)
