import json

with open('links_errors.txt','r') as f:
    errors = f.readlines()


clear_errors = list()
for i in errors:
    clear_errors.append(i.strip())


with open('Karusel_promo.json', 'r') as f:
    old = json.loads(f.read())

c = 0
for i in old:
    if i['source'] in clear_errors:
        i['source'] = i['source'].replace('data2','data3')
        c += 1
        continue


with open('Karusel_promo_2.json', 'w') as f:
    json.dump(old, f)








