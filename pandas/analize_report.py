import pandas as pd
import numpy as np

df = pd.read_csv('raw_data.csv',dtype = {'bc': str, 'sku': str, 'producer': str, 'brand': str})

pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 20)




SEGMENTS_ALL = ['ПАРФЮМЕРИЯ ГИГИЕНА', 'ВИНО', 'СР-ВА ПО УХ ЗА ВОЛОСАМИ',
       'ЗЛАКИ И БАТОНЧИКИ', 'СРЕД Д/УБОРКИ ПОМЕЩЕНИЙ', 'ДЕТСКОЕ ПИТАНИЕ',
       'ДЕСЕРТЫ ОХЛАЖДЕННЫЕ', 'КОНСЕРВЫ', 'ШОКОЛАДНЫЕ КОНДИТ ИЗД-Я',
       'ПАРФЮМЕРИЯ КОСМЕТИКА', 'САХАРИСТЫЕ КОНДИТ ИЗДЕЛИЯ', 'ПЕЧЕНЬЕ',
       'АЛКОГОЛЬНЫЕ НАПИТКИ', 'ПРОДУКЦИЯ ЗАМОРОЖЕННАЯ',
       'ИНГР Д/ПР БЛЮДА Б/П СОУСЫ', 'ГАРНИРЫ/ ГОРЯЧИЕ СОУСЫ', 'ЧАЙ',
       'МАСЛА, УКСУС, СПЕЦИИ,СОЛЬ', 'СОКИ И СИРОПЫ', 'СОЛЕНЫЕ ЗАКУСКИ И ЧИПСЫ',
       'ТОВАРЫ Д/ДОМ ЖИВОТНЫХ', 'КОФЕ И КОФЕЙНЫЕ НАПИТКИ',
       'ПИВО, РАДЛЕР И СИДР', 'СЛАДКИЕ НАПИТКИ', 'ФАСОВАННЫЕ СЫРЫ',
       'МОЛ.ПРОД.ТРАДИЦИОННЫЕ', 'КОЛБАСЫ/ДЕЛИК-СЫ ШТУЧНЫЕ',
       'ОХЛАЖДЕННЫЕ МОРЕПРОДУКТЫ', 'СРЕДСТВА ДЛЯ СТИРКИ',
       'ГИГИЕНА И ЗДОР.РЕБЕНКА', 'АВТОМОБИЛИ', 'ЖЕН. ЧУЛ.-НОС. ИЗД-Я',
       'БАКАЛЕЯ ИНГ.Д/ВЫПЕЧКИ', 'ВОДКА', 'БУТИЛИРОВАННАЯ ВОДА',
       'ПРОМЫШЛ-Я ВЫПЕЧКА И ХЛЕБ', 'МАСЛО СЛ/МАРГАРИН/СОУС',
       'МОЛОКО СТЕРИЛИЗОВАННОЕ', 'ПРОМ МУЧНЫЕ КОНД-Е ИЗД-Я',
       'ЭЛЕКТРООСВЕТИТ. ПРИБОРЫ', 'МАКИЯЖ', 'РЫБА И МОРЕПРОДУКТЫ ЗАМОР',
       'МЯСО ПТИЦЫ', 'РЕМОНТ', 'ГОТОВАЯ КУЛИНАРИЯ П/П', 'ИГРУШКИ', 'МЯСО П/П',
       'ДОМАШНЯЯ УТВАРЬ']

макароны, орехи, крупы


SEGMENTS_TRUE = ['ПРОМ МУЧНЫЕ КОНД-Е ИЗД-Я','МЯСО П/П','МЯСО ПТИЦЫ','ГОТОВАЯ КУЛИНАРИЯ П/П','МАСЛА, УКСУС, СПЕЦИИ,СОЛЬ','ПРОМЫШЛ-Я ВЫПЕЧКА И ХЛЕБ']



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


#баркод не нул
df1 = df[(df['bc'].notnull())]

#удалить дубликаты по признаку и создать новый датафрейм
df2 = df1.drop_duplicates(subset=['bc'])



#заполняю пропуски
#nan
clean_df = df['tz'].fillna('Missing')
#'' булево
clean_df[clean_df == ''] = 'Unknown'



#дф с товарами только определенного производителя
dft = df[df['producer'] == 'Procter And Gamble']

#смотрим сколько в городе сетей и указываем их кол-во
dft.groupby(['city','shop_title']).size()

#смотрим общую сумму товаров в каждом магазине
dft.groupby(['city','shop_title'])['sku_title'].sum()


# создаем массив уникальных имен
all_names = top1000.name.unique()
#булевый массив с именами в которых есть подстрока
mask = np.array(['ША' in x.lower() for x in all_names])
#создаю массив с уникальными именами
sha_like = all_names[mask]




#Содержит ли строка подстроку в признаке
#                                                #true     #false
ops = np.where(df['a'].str.contains('Windows'),'Windows','Not Windows')


#данные по названию и с помощью метода size () получу объект Series, содержащий размеры групп для каждого наименования:
quantity_by_title = df.groupby('title').size()

# извлекаем последнюю букву имени в столбце name
get_last_letter = lambda x: x[-1]

#добавляю новый признак, если индексы совпадают
df['last_letter'] = last_letters



#                    по этому признаку   смотрю сюда     разбиваю на колонки    применяю функцию
mean_df = df.pivot_table('rating',index=['title'], columns=['gender'], aggfunc='mean')
#сводная пример
table = pd.pivot_table(df, values='D', index=['A', 'B'],columns=['C'], aggfunc=np.sum)

#последние 5 записей
df.tail()





#создать несколько файлов по срезам
c = 0
t = 0
s = 0
for i in range(len(df)+1):
    c+=1
    if c % 52 == 0:
        t += 1
        df[s:c].to_csv('шк_отсутствует{}.csv'.format(t), index=False)
        s = c






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


#store_title - название сети
#store_list - массив строк-брендов
#рабочая ищет
def check_cat(df,store_title):
    df_store = df[df['outlet'] == str(store_title)]
    df_store = df_store[df_store['brand'].apply(lambda x: str(x) in store_list)]
    return df_store


#шк на 2
df1 = df[df['bc'].apply(lambda x: str(x)[0] == '2')]


#шапка для отчета
HEADERS = ['geo_object_id', 'title' , 'id', 'price', etc]
RAW_HEADERS = df.columns.tolist()

#удаляю ненужные признаки(колонки) через множества, тк вычитать массивы нельзя
df_final = df.drop(columns=list(set(RAW_HEADERS) - set(HEADERS)))



writer = pd.ExcelWriter(path, engine='xlsxwriter', options={'strings_to_urls': False})
df_final.to_excel(writer, sheet_name='Лист 1', index=False)
worksheet = writer.sheets['Лист 1']

#указываю признаки (колонки) для форматирования и формат для них
FORMATS = ["ШТРИХКОД", "Цена конкурента (без карты)", "Цена по карте клиента", "Цена по акции"]
barcode_format = writer.book.add_format({'num_format': '0'})
price_format = writer.book.add_format({'num_format': '0.00'})

#иду по сторока и столбцам и если названия признака нет в списке для форматирования иду дальше
for j, header in enumerate(df1):
        if header not in FORMATS:
            continue
        #найденный нужный признак для форматирования записываю в файл, устанавливая нужный формат данных
        for i, value in enumerate(df_final[header]):
            if header == "ШТРИХКОД":
                worksheet.write_number(i+1, j, int(value), barcode_format)
                continue

            if np.isnan(value):
                continue

            worksheet.write(i+1, j, value, price_format)

    writer.save()
