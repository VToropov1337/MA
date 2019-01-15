import pandas as pd
import numpy as np

df = pd.read_csv('raw_data.csv',dtype = {'bc': str, 'sku': str, 'producer': str, 'brand': str})

pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 20)

#создание нового признака
df1 = df.assign(is_stm = 0)

#произведение векторов
#arr.shape(6,3)
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
#arr.T.shape(3,6)
arr.T
#shape(3,3) #берем кол-во строк из транспонированного, кол-во элементов из оригинального
np.dot(arr.T,arr)

#стандартное отклонение
np.std(arr,ddof=1)

#В нашем случае, среднее , которое на следующем шаге отнимают от каждого значения выборки.
#Каждую полученную разницу возводят в квадрат и суммируют. Получившуюся сумму,
#необходимо разделить на количество элементов выборки минус 1.
#Так как у нас n элементов, получается необходимо получившуюся сумму разделить на n-1.
#Из полученного результата находим квадратный корень, это цифра будет стандартным отклонением.

# или ручками:
arr = [10, 20, 30, 40, 50, 60, 70]
sum = 0
for i in arr:
    sum += i
    
#mean
mean = sum / len(arr)

b = list()
for i in arr:
    b.append(i - mean)

sum2 = 0
for i in b:
    sum 2+= i**2

std_a = (sum2 / (len(b)-1))**0.5
################################
# 5%-ный квантиль
arr[int(-0.05 * len(arr))]

values = np.array([6, 0, 0, 3, 2, 5, 6])
#Вычисляет отсортированное множество элементов, общих для х и у
np.intersect1d(values,[1,2,3])

#Функция np. inld проверяет, присутствуют ли значения из одного массива в другом, и возвращает булев массив:
np.in1d(values,[2,3,6])

#Вычисляет отсортированное объединение элементов
np.union1d(values,[1,2,3])

#Вычисляет разность множеств, т. е. элементы, принадлежащие х, но не принадлежащие у
np.setdiff1d([1,2,3],values)

#Симметрическая разность множеств; элементы, принадлежащие одному массиву, но не обоим сразу
np.setxor1d([1,2,3],values)


# кол-во элементов в массиве np
np.array.ndim

#одномерный массив в многоверный, соответствуя кортежам индексов
arr = np.arange(32).reshape(8,4)


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

#оставляет дф содержащий определенное количество наблюдений (кол-во значений в строках не пустые)
df1.dropna(thresh = 2)

#самые большие значения по признакам
df1.idxmax()

#баркод не нул
df1 = df[(df['bc'].notnull())]

#индексация
df.loc[['index1','index2'], ['column1', 'column2']]


#уровни иерархического индекса перемещаются в столбцы
df.reset_index()

#устанавливаем индексы из признаков (и не удаляем их)
df.set_index(['c', 'd'], drop = False)

#статистика по уровню вложенности
df.sum(level = 'key1')

#булева индексация
df.loc[df['price'] > 200,:'brand']

#удалить дубликаты по признаку и создать новый датафрейм
df2 = df1.drop_duplicates(subset=['bc'])

#заполняю пропуски
#nan
clean_df = df['tz'].fillna('Missing')
#'' булево
clean_df[clean_df == ''] = 'Unknown'

#проверка на уникальность индекса
df.index.is_unique

#вычисляем каждую строку из дф
format = lambda x: '%.2f' % x
df.applymap(format)
#для series
df['e'].map(format)

#мержу значения из разных дф
df1.add(df2, fill_value = 0)

#дф с товарами только определенного производителя
dft = df[df['producer'] == 'Procter And Gamble']

#смотрим сколько в городе сетей и указываем их кол-во
dft.groupby(['city','shop_title']).size()


#аггрегирование
df.groupby(by=grouping_columns)[columns_to_show].function()

#вычисляем сумму по столбцу data1 в виде df [[]] 
df.groupby(['key1','key2'])[['data1']].sum()

#смотрим общую сумму товаров в каждом магазине
dft.groupby(['city','shop_title'])['sku_title'].sum()

#фильтрую по нужным индексам и признакам
df.loc[['tt1','tt2','tt3'],['brand1', 'brand2']]


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

df[c:].to_csv('шк_отсутствует{}.csv'.format(t+1), index=False)

#просмотр подозрительно коротких названий товаров
df[(df['sku'].notnull()) & (df['sku'].apply(lambda x: len(str(x)) <15))]


#выбираю непустые и уникальные шк
grouped_df = df[df['bc'].notnull()].groupby('bc').nunique()


#смотрю на шк у которого более 1 сегмента
df1 = grouped_df[grouped_df['seg'] > 1].sort_values('bc',ascending=False)

#создаю датафрейм с проверкой попадания шк по индексам(шк из дф1)
df2 = df[(df['bc'].isin(df1.index))]

mask = df.isin(['x1', 'x2'])
df[mask] #булево

#сортирую получившийся дф по шк в порядке убывания
df2.sort_values(by=['bc'],ascending=False)


#создаю массив с ссылками на отчеты
arr = df2['raw_report_edit_link'].tolist()


def create_ids(arr):
    if type(arr) == list():
    #создаю двумерный массив из каждого элемента arr по разделителю '/'
        qq = list()
        for i in arr:
            qq.append(i.split('/'))
            #вытаскиваю ид отчета и записываю в файл txt
        for i in qq:
            with open('ids.txt','a') as f:
    else:
        raise ValueError('args must be array')



#ПРОВЕРКА СТМ
########################################################################
#store_title - название сети
#store_list - массив строк-брендов
def check_cat(df,store_title):
    df_store = df[df['outlet'] == str(store_title)]
    df_store = df_store[df_store['brand'].apply(lambda x: str(x) in store_list)]
    return df_store

#в цикле
%time
for i in df.index:
    for j in store_list:
        if str(j) in str(df1.loc[i][['sku','brand','producer']]):
            df1.loc[i,'is_stm'] = 1

#разово
df1 = df.assign(is_stm = np.where(df['sku'].str.contains('ALPRO'),1,0))
##########################################################################




#шк на 2
df1 = df[df['bc'].apply(lambda x: str(x)[0] == '2')]


#дф, где территория не входит в выборку~
df[~df['territory'].isin(['Center'])]

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
            #если значения нет, иду дальше
            if np.isnan(value):
                continue

            worksheet.write(i+1, j, value, price_format)

        writer.save()

#шапка для отчета
HEADERS = ['geo_object_id', 'title' , 'id', 'price', etc]
RAW_HEADERS = df.columns.tolist()

#удаляю ненужные признаки(колонки) через множества, тк вычитать массивы нельзя
df_final = df.drop(columns=list(set(RAW_HEADERS) - set(HEADERS)))

#записываю в файл финальный дф
writer = pd.ExcelWriter(path, engine='xlsxwriter', options={'strings_to_urls': False})
df_final.to_excel(writer, sheet_name='Лист 1', index=False)
worksheet = writer.sheets['Лист 1']
