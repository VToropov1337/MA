import pandas as pd

df = pd.read_csv('raw_data.csv', sep=',')
dfx = df.head(10)

writer = pd.ExcelWriter("report_test.xlsx", engine='xlsxwriter')

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

HEADERS = [
    "ГОРОД", "КОНКУРЕНТ", "АДРЕС КОНКУРЕНТА", "Номер Сегмента", "Название Сегмента", "ШТРИХКОД", "НАЗВАНИЕ Артикула",
       "Производитель конкурента","БРЕНД","Цена конкурента (без карты)","Цена по карте клиента",
       "Цена по акции","Фото"]

COLUMNS = ["territory","outlet","address","seg_code","seg","bc","sku","producer","brand","price_orig","price_card","price_disc","collage"]

NEW_HEADERS = dict()

df1 = dfx.copy()

for i in range(len(COLUMNS)):
    NEW_HEADERS[COLUMNS[i]] = HEADERS[i]


for i,value in enumerate(df1.columns.values):
    if value not in NEW_HEADERS:
        df1 = df1.drop(columns=value)


for i,value in enumerate(df1.columns.values):
    if value in NEW_HEADERS:
        df1.rename(columns={value: NEW_HEADERS[value]}, inplace=True)



df1.to_csv('renamed_raw_data.csv', sep=',')