import pandas as pd
import numpy as np

df = pd.read_csv('raw_data.csv',dtype = {'bc': str, 'sku': str, 'producer': str, 'brand': str})

pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 20)



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
