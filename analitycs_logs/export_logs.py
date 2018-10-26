import re
import pandas as pd
import numpy as np


def csv_dict_writer(path, fieldnames, data):
    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter='|', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


pattern_url= re.compile(r'/\S*')
pattern_date = re.compile(r'DATE:.\b(\S*.\S*)')
pattern_spent = re.compile(r'SPENT.\b(\S*)')


with open('.log','r') as f:
    arr = f.readlines()

output = list()

for i in arr[1:]:
    hh = dict()
    hh['url'] = pattern_url.findall(i)
    hh['date'] = pattern_date.findall(i)
    hh['spent'] = pattern_spent.findall(i)
    output.append(hh)

fieldnames = output[0].keys()
csv_dict_writer('data_prod.csv',fieldnames , output)



df = pd.read_csv('data_prod.csv',sep='|')

df['url'] = df['url'].replace('\?.*','',regex=True) #удаляю параметры после .json
df['url'].value_counts(ascending=False).head(20) #самые популярные топ20
df.groupby('date')['spent'].describe() #первый взгляд
