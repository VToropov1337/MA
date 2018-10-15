import psycopg2
import json

connect = psycopg2.connect(database='***', user='***', host='***', port='***', password='***')
cursor = connect.cursor()


cursor.execute("SELECT CONCAT_WS('','https://***.com/***/***/image/', r2.metro_price_photo_id, '/',file) as url,r2.metro_price_photo_id \
FROM ma_metro.reports r2 \
JOIN ma_metro.answer_files \
	ON answer_files.id = r2.metro_price_photo_id \
WHERE r2.id IN (18106364,18106363,18106361,18106359,18106318,\
18106308,18106298,18106281,18106255,18106248,18106220,18106218,\
18106217,18106214,18106213,18106188,18105259,18104613,18104612,18104572,\
18104567,18104562,18104558,18104556,18104545,18104500,18104497,18104234,\
18104083,18104077,18103958,18103913,18103909,18103854,18103850,18103843,18103840,\
18103839,18103838,18103836,18103835,18103833,18103832,18103831,18103779,18103732,\
18103731,18103720,18103719,18103717)\
")


arr = list()
arr2 = list()


for i in cursor:
    arr.append(i)



for i in arr:
    hh = dict()
    hh['url'] = i[0]
    arr2.append(hh)


# with open('yarche.json','w') as f:
#     json.dump(arr2, f)
#
with open('***.html','w') as f:
    for i in arr2:
        k = i['url']
        # f.write("\"{}\"\n".format(k))
        f.write("<img style=\"width:300px\" src=\"{}\"/>\n".format(k))




        # <img style="width:300px" src=
