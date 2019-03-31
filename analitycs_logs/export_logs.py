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


df['url'] = df['url'].replace('\?.*','',regex=True)
df['url'] = df['url'].replace('/.*/bulk_photos_show.json','/xxx/gg/pop/rr/bulk_photos_show.json',regex=True)
df['url'] = df['url'].replace('\d*.json','',regex=True)
df['url'] = df['url'].replace('.*element_relations/\d*.json', 'element_relations/json', regex=True)
df['url'] = df['url'].replace('.*gg/rr/\d*/a/\d*/media_files/\d*.json','/media_files/json', regex=True)
df['url'] = df['url'].replace('.*gg/tt/\d*.json','/api/hq/web/tasks/json',regex=True)
df['url'] = df['url'].replace('/xxx/gg/pop/rr/\d*/edit_marks.json','/edit_marks.json',regex=True)
df['url'] = df['url'].replace('/xxx/u/model/tt/.*/reserve.json','/reserve.json',regex=True)
df['url'] = df['url'].replace('/xxx/u/model/tt/.*/scenario.json','/scenario.json',regex=True)
df['url'] = df['url'].replace('/xxx/gg/pop/users/.*.json','/users/json', regex=True)
df['url'] = df['url'].replace('/xxx/gg/pop/geo_objects/\d*.json','/geo_objects/json',regex=True)
df['url'] = df['url'].replace('/xxx/gg/pop/articles/\d*.json','/articles/json',regex=True)
df['url'] = df['url'].replace('.*/background_jobs/\d*','/background_jobs',regex=True)
df['url'] = df['url'].replace('/xxx/gg/pop/reports/\d*/answers/\d*.json','/reports/answers/json',regex=True)
df['url'] = df['url'].replace('/xxx/gg/pop/reports/\d*/answers/\d*/media_files/.*/left.json','/media_files/left.json', regex=True)
df['url'] = df['url'].replace('/xxx/gg/pop/reports/\d*.json','/reports/json', regex=True)
df['url'] = df['url'].replace('/xxx/u/model/tickets/\d*.json','/tickets/json', regex=True)
df['url'] = df['url'].replace('/xxx/u/model/tt/\d*.json','/tasks/json',regex=True)
df['url'] = df['url'].replace('/xxx/gg/pop/rr/\d*/duplicate.json','/duplicate.json',regex=True)
df['url'] = df['url'].replace('/xxx/gg/pop/rr/\d*/template.json','/template.json', regex=True)
df['url'] = df['url'].replace('/xxx/gg/pop/rr/\d*/answers/\d*/media_files/.*/right.json','/media_files/right.json', regex=True)


df['url'].value_counts(ascending=False).head(20) #
df.groupby('date')['spent'].describe() 