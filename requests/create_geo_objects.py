import requests
import json
import pandas as pd


COL = ['title', 'comment', 'country', 'region', 'city', 'street', 'house',
       'ltd', 'lgt', 'address', 'territory', 'metro_city', 'metro_competitor',
       'problematical', 'at_code', 'category_id', 'regional_category_id']


token = '***'

params = {'Content-Type': 'application/json; charset=utf-8',
          'X-Authentication-Token': token}

base_url = 'https://***/api/***/***/***/***'

# создание 1 тт
create = '/geo_objects'


def check_file(filename):
    dataframe = pd.read_excel(filename,sheet_name=0)
    if list(dataframe.columns) == COL:
        return dataframe
    else:
        raise BaseException('Проверь названия колонок и их порядок')



df = check_file('geo_objects.xlsx')
df = df.fillna('')





data = dict()

for i in range(len(df)):
    data[i] = {
		"title": df['title'].iloc[i],
        "comment": df['comment'].iloc[i],
        "city": df['city'].iloc[i],
		"address":df['address'].iloc[i],
        "territory": df['territory'].iloc[i],
        "metro_city": df['metro_city'].iloc[i],
        "metro_competitor": df['metro_competitor'].iloc[i],
        "problematical": str(df['problematical'].iloc[i]).capitalize(),
        "at_code": df['at_code'].iloc[i],
        "category_id": df['category_id'].iloc[i],
        "regional_category_id": df['regional_category_id'].iloc[i]
    }


# print(data)


for i in data.keys():
	r = requests.post(base_url + create, headers=params,
	                  data=json.dumps({"geo_object": {
				          "title": str(data[i]['title']),
				          "comment": str(data[i]['comment']),
				          "city": str(data[i]['city']),
						  "address": str(data[i]['address']),
				          "territory": str(data[i]['territory']),
				          "metro_city": str(data[i]['metro_city']),
				          "metro_competitor": str(data[i]['metro_competitor']),
				          "problematical": str(data[i]['problematical']),
				          "at_code": str(data[i]['at_code']),
				          "category_id": int(data[i]['category_id']),
				          "regional_category_id": int(data[i]['regional_category_id'])
	                  }}))
	print(r.text)
	print(r)
