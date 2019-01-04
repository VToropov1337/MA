import pandas as pd
import numpy as np
import matplotlib




df = pd.read_csv('NASA_access_log_Jul95.txt',sep=' ',\
encoding='ISO-8859-1',header=None,\
error_bad_lines=False,engine='c',\
infer_datetime_format=True)

df.columns=['host','todel1','todel2','timestamp','timezone','requests','http_code','bitr']
df = df.drop(['todel1', 'todel2'],axis=1)

df.head()
df = df[df['timestamp'].notnull()]
df['requests'].value_counts(ascending=False).head(15) #самые популярные топ15
