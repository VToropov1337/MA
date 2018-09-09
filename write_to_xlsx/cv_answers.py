import psycopg2
from openpyxl import Workbook
import csv

connect = psycopg2.connect(database='***', user='***', host='***', port='***', password='***')
cursor = connect.cursor()
cursor.execute("SELECT reports.metro_price,cv_responses.response,geo_objects.title \
FROM ma_metro.reports \
JOIN ma_metro.tasks \
	ON reports.task_id = tasks.id \
JOIN ma_metro.geo_objects \
	ON geo_objects.id = tasks.geo_object_id \
JOIN ma_metro.conveyor_jobs \
    ON reports.id = conveyor_jobs.target_id \
JOIN ma_metro.cv_responses \
    ON cv_responses.target_id = conveyor_jobs.id \
WHERE reports.state = 'accepted' \
    AND conveyor_jobs.wave = '***' \
    AND cv_responses.state = 'completed' \
    AND cv_responses.req_type = 'get_bulk_result_detect_classify_images';")

data = list()
for i in cursor:
    if i[0]:
        data.append(i)


book = Workbook()
sheet = book.active
sheet['A1'] = "report_price"
sheet['B1'] = "cv_price"
sheet['C1'] = "geo_object"
sheet['D1'] = "isequal"
sheet['E1'] = "url"




count = 0
for i in data:
    count += 1
    print(count)
    if i[1]['images'][0]['tags'] == []:
        url = (i[1]['images'][0]['url'])
        sheet.cell(row=count+1, column=5).value = url
        sheet.cell(row=count+1, column=2).value = 'Нет ответа'
        sheet.cell(row=count+1, column=4).value = 0
        sheet.cell(row=count+1, column=1).value = i[0]
        sheet.cell(row=count+1, column=3).value = i[2]

    elif len(i[1]['images'][0]['tags']) == 1:
            if i[1]['images'][0]['tags'][0]['price_rub'] != None and i[1]['images'][0]['tags'][0]['price_kop'] != None:
                r = str(i[1]['images'][0]['tags'][0]['price_rub']['text']).strip()
                k = str(i[1]['images'][0]['tags'][0]['price_kop']['text']).strip()
                p = str(r+'.'+k).strip()
                p = p.strip()
                # sheet.cell(row=count+1, column=1).value = i[0]
                # sheet.cell(row=count+1, column=2).value = p
                # sheet.cell(row=count+1, column=3).value = i[2]
                if i[0] == float(p):
                    #print('YES')
                    sheet.cell(row=count+1, column=4).value = 1
                    sheet.cell(row=count+1, column=1).value = i[0]
                    sheet.cell(row=count+1, column=2).value = p
                    sheet.cell(row=count+1, column=3).value = i[2]
                else:
                    #print("NO")
                    url = (i[1]['images'][0]['url'])
                    sheet.cell(row=count+1, column=4).value = 0
                    sheet.cell(row=count+1, column=5).value = url
                    sheet.cell(row=count+1, column=1).value = i[0]
                    sheet.cell(row=count+1, column=2).value = p
                    sheet.cell(row=count+1, column=3).value = i[2]
            elif i[1]['images'][0]['tags'][0]['price_rub'] != None and i[1]['images'][0]['tags'][0]['price_rub']['text'] != '' and i[1]['images'][0]['tags'][0]['price_kop'] == None:
                r = str(i[1]['images'][0]['tags'][0]['price_rub']['text']).strip()
                if i[0] == float(r):
                    sheet.cell(row=count+1, column=4).value = 1
                    sheet.cell(row=count+1, column=1).value = i[0]
                    sheet.cell(row=count+1, column=2).value = r
                    sheet.cell(row=count+1, column=3).value = i[2]
                else:
                    url = (i[1]['images'][0]['url'])
                    sheet.cell(row=count+1, column=4).value = 0
                    sheet.cell(row=count+1, column=5).value = url
                    sheet.cell(row=count+1, column=1).value = i[0]
                    sheet.cell(row=count+1, column=2).value = r
                    sheet.cell(row=count+1, column=3).value = i[2]
            elif i[1]['images'][0]['tags'][0]['price_rub'] == None and i[1]['images'][0]['tags'][0]['price_kop'] != None:
                url = (i[1]['images'][0]['url'])
                sheet.cell(row=count+1, column=4).value = 0
                sheet.cell(row=count+1, column=5).value = url
                sheet.cell(row=count+1, column=1).value = i[0]
                sheet.cell(row=count+1, column=2).value = str(i[1]['images'][0]['tags'][0]['price_kop']['text'])
                sheet.cell(row=count+1, column=3).value = i[2]
                #sheet.cell(row=count+1, column=6).value = 'только копейки'
            else:
                url = (i[1]['images'][0]['url'])
                sheet.cell(row=count+1, column=4).value = 0
                sheet.cell(row=count+1, column=5).value = url
                sheet.cell(row=count+1, column=1).value = i[0]
                sheet.cell(row=count+1, column=2).value = str(i[1]['images'][0]['tags'][0])
                sheet.cell(row=count+1, column=3).value = i[2]
                #sheet.cell(row=count+1, column=6).value = 'нет цен вообще'
    else:
        doublearr = list()
        for j in i[1]['images'][0]['tags']:
            if j['price_rub'] != None and j['price_kop'] != None:
                r = str(j['price_rub']['text'])
                k = str(j['price_kop']['text'])
                p = str(r+'.'+k).strip()
                if i[0] == float(p):
                    url = (i[1]['images'][0]['url'])
                    #sheet.cell(row=count+1, column=5).value = url
                    sheet.cell(row=count+1, column=4).value = 1
                    sheet.cell(row=count+1, column=1).value = i[0]
                    sheet.cell(row=count+1, column=2).value = p
                    sheet.cell(row=count+1, column=3).value = i[2]
                    #sheet.cell(row=count+1, column=6).value = 'первая цена совпала'
                    #sheet.cell(row=count+1, column=7).value = '>= 2 ответа'
                    break
                else:
                    doublearr.append(p)
                    url = (i[1]['images'][0]['url'])
                    sheet.cell(row=count+1, column=5).value = url
                    sheet.cell(row=count+1, column=4).value = 0
                    sheet.cell(row=count+1, column=1).value = i[0]
                    sheet.cell(row=count+1, column=2).value = str(doublearr)
                    sheet.cell(row=count+1, column=3).value = i[2]
                    #sheet.cell(row=count+1, column=6).value = '2 и более значения и ничего не совпало'
                    #sheet.cell(row=count+1, column=7).value = '>= 2 ответа'


            elif j['price_rub'] != None  and j['price_rub']['text'] != '' and j['price_kop'] == None:
                r = str(j['price_rub']['text']).strip()
                doublearr.append(r)
                if i[0] == float(r):
                    sheet.cell(row=count+1, column=4).value = 0
                    url = (i[1]['images'][0]['url'])
                    sheet.cell(row=count+1, column=5).value = url
                    sheet.cell(row=count+1, column=1).value = i[0]
                    sheet.cell(row=count+1, column=2).value = str(doublearr)
                    sheet.cell(row=count+1, column=3).value = i[2]
                    #sheet.cell(row=count+1, column=6).value = 'совпали только рубли'
                    #sheet.cell(row=count+1, column=7).value = '>= 2 ответа'
                    #sheet.cell(row=count+1, column=8).value = str(i[1]['images'][0]['tags'])
                    break
                else:
                    doublearr.append(r)
                    url = (i[1]['images'][0]['url'])
                    sheet.cell(row=count+1, column=4).value = 0
                    sheet.cell(row=count+1, column=5).value = url
                    sheet.cell(row=count+1, column=1).value = i[0]
                    sheet.cell(row=count+1, column=2).value = str(doublearr)
                    sheet.cell(row=count+1, column=3).value = i[2]
                    #sheet.cell(row=count+1, column=6).value = 'должно быть 2 значения и только копейки'
                    #sheet.cell(row=count+1, column=7).value = '>= 2 ответа'

            else:
                if j['price_rub'] and j['price_rub']['text'] != '':
                    r = str(j['price_kop']['text']).strip()
                else:
                    r = "-"
                if j['price_kop'] and j['price_kop']['text'] != '':
                    k = str(j['price_kop']['text']).strip()
                else:
                    k = "-"
                p = str(r+'.'+k)
                doublearr.append(p)
                #sheet.cell(row=count+1, column=6).value = 'хуйня какая-то'
                sheet.cell(row=count+1, column=1).value = i[0]
                url = (i[1]['images'][0]['url'])
                sheet.cell(row=count+1, column=2).value = str(doublearr)
                sheet.cell(row=count+1, column=3).value = i[2]
                sheet.cell(row=count+1, column=4).value = 0
                sheet.cell(row=count+1, column=5).value = url
                #sheet.cell(row=count+1, column=7).value = '>= 2 ответа'
                #sheet.cell(row=count+1, column=8).value = str(i[1]['images'][0]['tags'])







book.save('cv_answers.xlsx')
connect.close()
