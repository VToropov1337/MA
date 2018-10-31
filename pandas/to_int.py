import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 10)

df = pd.read_csv('all_prices_filled.csv', sep=',')
writer = pd.ExcelWriter("report_test.xlsx", engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')

workbook = writer.book
worksheet = writer.sheets['Sheet1']

f1 = workbook.add_format({'num_format': '0.00'})
f2 = workbook.add_format({'num_format': '0.0'})
f3 = workbook.add_format({'num_format': '0'})

counter_barcode = 1
counter_client_card = 1
counter_without_card = 1
counter_promo = 1

for i in df:
    for value in df[i]:
        if i == 'ШТРИХКОД':
            column_index = df.columns.get_loc("ШТРИХКОД")
            worksheet.write(counter_barcode, column_index + 1, value, f3)
            counter_barcode += 1

for i in df:
    for value in df[i]:
        if i == 'Цена по карте клиента':
            value = str(value)
            # print(value,len(value[value.index('.'):]))
            if value.find('.') and len(value[value.index('.'):]) == 3:
                column_index = df.columns.get_loc("Цена по карте клиента")
                value = float(value)
                worksheet.write_number(counter_client_card, column_index + 1, value, f1)
                counter_client_card += 1
            elif value.find('.') and len(value[value.index('.'):]) == 2 and value[-1] != '0':
                column_index = df.columns.get_loc("Цена по карте клиента")
                value = float(value)
                worksheet.write_number(counter_client_card, column_index + 1, value, f2)
                counter_client_card += 1
            else:
                column_index = df.columns.get_loc("Цена по карте клиента")
                value = int(float(value))
                worksheet.write_number(counter_client_card, column_index + 1, value, f3)
                counter_client_card += 1

        if i == 'Цена конкурента (без карты)':
            value = str(value)
            if value.find('.') and len(value[value.index('.'):]) == 3:
                column_index = df.columns.get_loc("Цена конкурента (без карты)")
                value = float(value)
                worksheet.write_number(counter_without_card, column_index + 1, value, f1)
                counter_without_card += 1
            elif value.find('.') and len(value[value.index('.'):]) == 2 and value[-1] != '0':
                column_index = df.columns.get_loc("Цена конкурента (без карты)")
                value = float(value)
                worksheet.write_number(counter_without_card, column_index + 1, value, f2)
                counter_without_card += 1
            else:
                column_index = df.columns.get_loc("Цена конкурента (без карты)")
                value = int(float(value))
                worksheet.write_number(counter_without_card, column_index + 1, value, f3)
                counter_without_card += 1

        if i == 'Цена по акции':
            value = str(value)
            if value.find('.') and len(value[value.index('.'):]) == 3:
                column_index = df.columns.get_loc("Цена по акции")
                value = float(value)
                worksheet.write_number(counter_promo, column_index + 1, value, f1)
                counter_promo += 1
            elif value.find('.') and len(value[value.index('.'):]) == 2 and value[-1] != '0':
                column_index = df.columns.get_loc("Цена по акции")
                value = float(value)
                worksheet.write_number(counter_promo, column_index + 1, value, f2)
                counter_promo += 1
            else:
                column_index = df.columns.get_loc("Цена по акции")
                value = int(float(value))
                worksheet.write_number(counter_promo, column_index + 1, value, f3)
                counter_promo += 1

writer.save()
