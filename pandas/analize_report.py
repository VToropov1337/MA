import pandas as pd
import numpy as np

df = pd.read_csv('raw_data.csv',dtype = {'bc': str, 'sku': str, 'producer': str, 'brand': str})

pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 20)



#метод на запись в файл
def toCsv(df, path):
    df.to_csv(path, index=False, float_format='%.2f')
    return df

#метод на получение строк с пустыми ценами
def getWithoutPrices(df):
    return df[
        (df['price_orig'].isnull()) &
        (df['promo_price'].isnull()) &
        (df['price_disc'].isnull())
    ]



#просмотр подозрительно коротких названий товаров
df[(df['sku'].notnull()) & (df['sku'].apply(lambda x: len(str(x)) <15))]


#выбираю непустые и уникальные шк
grouped_df = df[df['bc'].notnull()].groupby('bc').nunique()


#смотрю на шк у которого более 1 сегмента
df1 = grouped_df[grouped_df['seg'] > 1].sort_values('bc',ascending=False)

#создаю датафрейм с проверкой попадания шк по индексам(шк из дф1)
df2 = df[(df['bc'].isin(df1.index))]

#сортирую получившийся дф по шк в порядке убывания
df2.sort_values(by=['bc'],ascending=False)


#создаю массив с ссылками на отчеты
arr = df2['raw_report_edit_link'].tolist()


#создаю двумерный массив из каждого элемента arr по разделителю '/'
qq = list()
for i in arr:
    qq.append(i.split('/'))


#вытаскиваю ид отчета и записываю в файл txt
for i in qq:
    with open('ids.txt','a') as f:
        f.write('{}\n'.format(i[4]))




#шапка для отчета
HEADERS = ['geo_object_id', 'title' , 'id', 'price', etc]
RAW_HEADERS = df.columns.tolist()

#удаляю ненужные признаки(колонки) через множества, тк вычитать массивы нельзя
df_final = df.drop(columns=list(set(RAW_HEADERS) - set(HEADERS)))



# writer = pd.ExcelWriter(path, engine='xlsxwriter', options={'strings_to_urls': False})
# df_final.to_excel(writer, sheet_name='Лист 1', index=False)
# worksheet = writer.sheets['Лист 1']
#
# #указываю признаки (колонки) для форматирования и формат для них
# FORMATS = ["ШТРИХКОД", "Цена конкурента (без карты)", "Цена по карте клиента", "Цена по акции"]
# barcode_format = writer.book.add_format({'num_format': '0'})
# price_format = writer.book.add_format({'num_format': '0.00'})
#
# #иду по сторока и столбцам и если названия признака нет в списке для форматирования иду дальше
# for j, header in enumerate(df1):
#         if header not in FORMATS:
#             continue
#         #найденный нужный признак для форматирования записываю в файл, устанавливая нужный формат данных
#         for i, value in enumerate(df_final[header]):
#             if header == "ШТРИХКОД":
#                 worksheet.write_number(i+1, j, int(value), barcode_format)
#                 continue
#
#             if np.isnan(value):
#                 continue
#
#             worksheet.write(i+1, j, value, price_format)
#
#     writer.save()
