import pandas as pd
import numpy as np
import re
import matplotlib


1 - Скачать Access Log сервера NASA за июль 1995 года
2 - Распарсить файл в Pandas DataFrame
3 - Посчитать кол-во обращений к каждому урлу
4 - Найти топ-15 самый посещаемых урлов
5 - Посчитать число запросов в секунду
6 - Нарисовать график числа запросов в секунду
7 - построить гистограмму распределения размеров запросов

df = pd.read_csv('NASA_access_log_Jul95.txt',sep=' ',\
encoding='ISO-8859-1',header=None,\
error_bad_lines=False,engine='c',\
infer_datetime_format=True)

df.columns=['host','todel1','todel2','timestamp','timezone','requests','http_code','bitr']
df = df.drop(['todel1', 'todel2'],axis=1)

df = df[df['timestamp'].notnull()]
df['timestamp'] = df['timestamp'].replace('\[','',regex=True)
df['timezone'] = df['timezone'].replace('\]','',regex=True)

df.head() #2

df.groupby(['host'])['requests'].count().sort_values(ascending=False).#3
df.groupby(['host'])['requests'].count().sort_values(ascending=False).head(15) #4 


##############
df['time'] = pd.to_datetime(df['timestamp'], format='%d/%b/%Y:%H:%M:%S')

#дф с шагом 1 секунда
r1 = DataFrame(pd.date_range(start='1995-07-01 00:00:00', end='1995-07-28 13:32:25',freq='S'))
r1.columns=['date']


#дф с кол-ом запросов в определенное время
r2 = DataFrame(df.groupby('time')['time'].count())
r2.index.name='date'
r2.columns=['quantity']
r2.reset_index(level=0, inplace=True)


r3 = r1.merge(r2,how='outer')
r3 = r3.fillna(0)

df44 = r3.sort_values('date', ascending=True)

df44['day'] = pd.DatetimeIndex(df44['date']).day

df44.groupby('day')['quantity'].sum().plot(style='k--')

df44.plot(x='date',y='quantity',grid=True,legend=False,sharey=True,rot=0)


















