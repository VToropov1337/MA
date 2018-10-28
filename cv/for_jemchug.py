import psycopg2
import json

connect = psycopg2.connect(database='***', user='***', host='***', port='***', password='***')
cursor = connect.cursor()



cursor.execute("SELECT \
CONCAT_WS('','https://***.com/***/***/***/image/', answer_files.id, '/', file) as url,rr.id as report_id, geo_objects.title \
FROM ma_metro.reports r \
JOIN ma_metro.tasks \
    ON r.task_id = tasks.id \
JOIN ma_metro.geo_objects \
    ON tasks.geo_object_id = geo_objects.id \
JOIN ma_metro.answers \
    ON answers.report_id = r.id \
JOIN ma_metro.answer_files \
    ON answers.id = answer_files.answer_id \
JOIN ma_metro.reports rr \
    ON r.id = rr.origin_report_id \
WHERE rr.id \
IN (17486550,17494997,17494658,17494291,17494302,17486138,17494403,17494307,17494310, \
17494714,17494684,17494717,17494249,17494626,17486493,17494281,17494477,17494490, \
17494231,17494478,17486525,17486270,17494756,17494360,17494258,17494985,17494244, \
17494984,17494656,17494999,17494399,17494981,17494382,17494379,17494288,17494273, \
17494261,17486201,17495143,17494464,17494396, \
17494237,17494105,17494983,17494098,17494710,17486478,17494689,17494503,17494259, \
17486535,17486129,17494939,17486234,17495142,17486534,17486526,17495016,17494622, \
17494950,17495003,17494961,17494290,17494467,17494631,17494300,17494283,17494254, \
17485992,17486153,17486279,17486121,17486475,17494491,17486175,17494422) \
")


arr = list()

for i in cursor:
    hh = dict()
    hh['source'] = i[0]
    hh['objects'] = []
    arr.append(hh)

with open('check_photos.json', 'w') as f:
    json.dump(arr, f)



connect.close()
