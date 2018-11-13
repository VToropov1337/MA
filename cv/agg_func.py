import psycopg2

connect = psycopg2.connect(database='***', user='***', host='***', port='***',
                           password='***')
cursor = connect.cursor()

# cursor.execute("SELECT r.id, r.metro_price,r.barcode,geo_objects.title, conveyor_jobs.chain_element_id\
#     FROM ma_metro.reports r \
#         JOIN ma_metro.tasks \
#     ON r.task_id = tasks.id \
#         JOIN ma_metro.geo_objects \
#     ON geo_objects.id = tasks.geo_object_id \
#         JOIN ma_metro.conveyor_jobs \
#     ON r.id = conveyor_jobs.target_id \
#         WHERE r.state = 'accepted' \
#         AND conveyor_jobs.wave = 'os_auchan_40-18' \
#         AND conveyor_jobs.chain_element_id = 79 \
#         AND tasks.project_id = 2;")
#
#
# arr = list()
# arr2 = list()
#
# for i in cursor:
#     print(i)
#     arr.append(i)
#     if i[0] not in arr2:
#         arr2.append(i[0])
#
#
#
# print(len(arr))
# print(len(arr2))
#
#
#
#
# cursor.execute("SELECT r.id, r.metro_price,r.barcode,geo_objects.title, cv_responses.response->'images'->0->'tags'->0->'barcode',cv_responses.response->'images'->0->'tags'->0->'barcode_num'\
#     FROM ma_metro.reports r \
#     JOIN ma_metro.reports rr \
#         ON rr.id = r.origin_report_id \
#         JOIN ma_metro.tasks \
#     ON rr.task_id = tasks.id \
#         JOIN ma_metro.geo_objects \
#     ON geo_objects.id = tasks.geo_object_id \
#         JOIN ma_metro.conveyor_jobs \
#     ON r.id = conveyor_jobs.target_id \
#         JOIN ma_metro.cv_responses \
#     ON cv_responses.target_id = conveyor_jobs.id \
#     WHERE cv_responses.state = 'completed' \
#         AND r.state = 'accepted' \
#         AND conveyor_jobs.wave = 'os_auchan_40-18' \
#         AND cv_responses.req_type = 'get_bulk_result_detect_classify_images';")
#
#
#
# data = list()
# dif = list()
#
# for i in cursor:
#     data.append(i)
#
#
#
# for k in data:
#     for z in arr:
#         if k[2] == z[2] and k[0] not in dif:
#             dif.append(k[0])
#
#
#
# print(len(dif))


cursor.execute("SELECT r.id, json_agg((cj.chain_element_id)) \
    FROM ma_metro.reports r \
    INNER JOIN ma_metro.conveyor_jobs cj \
        ON r.id = cj.target_id \
    WHERE cj.wave = 'os_auchan_44-18' \
    AND r.state = 'accepted' \
    GROUP BY (r.id) \
")

arr = list()

for i in cursor:
    arr.append(i)

print(len(arr))
print(arr[0])

reports = list()

for i in arr:
    for j in i[1]:
        if j == 98:
            if i[0] not in reports:
                reports.append(i[0])
            else:
                continue
        else:
            continue

print(len(reports))
