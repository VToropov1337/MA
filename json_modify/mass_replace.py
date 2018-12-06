import json


def promo_replace(sstr):
    with open('{}_promo.json'.format(sstr), 'r') as f:
        old = json.loads(f.read())

    c = 0
    for i in old:
        i['source'] = i['source'].replace('data2', 'data3')
        c += 1
        continue

    with open('{}_promo_1000.json'.format(sstr), 'w') as f:
        json.dump(old, f)


def reg_replace(sstr):
    with open('{}_reg.json'.format(sstr), 'r') as f:
        old = json.loads(f.read())

    c = 0
    for i in old:
        i['source'] = i['source'].replace('data2', 'data3')
        c += 1
        continue

    with open('{}_reg_1000.json'.format(sstr), 'w') as f:
        json.dump(old, f)


arr = ['Auchan', 'Globus', 'Karusel', 'Lenta', 'Liniya', 'Magnit', 'Okey']

for i in arr:
    promo_replace(i)
    reg_replace(i)
