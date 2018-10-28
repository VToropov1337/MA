import json


old = list()
new = list()

false = False
true = True



with open('auchan_old.json','r') as f2:
    old = json.loads(f2.read())





for i in old:
    c = 0
    c1 = 1
    hh = dict()
    hh['data'] = ''
    hh['objects'] = list()
    hh['result'] = ''
    hh['source'] = i['source']
    for j in i['predicted_objects']:
        wrapped = dict()
        polygon = dict()
        wrapped['class'] = j['class']
        wrapped['class_id'] = c
        wrapped['modified'] = i['modified']
        polygon['id'] = c
        polygon['markup_id'] = c+1
        polygon['vertexes'] = j['polygons'][0]['points']
        wrapped['polygon'] = polygon
        c += 1
        hh['objects'].append(wrapped)

    new.append(hh)




with open('auchan-new.json','w') as nf:
    nf.write(json.dumps(new))
