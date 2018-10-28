import json


new = list()
false = False
true = True



with open('auchan20.json', 'r') as f:
    old = json.loads(f.read())



for i in old:
    hh = dict()
    hh['data'] = ""
    hh['class'] = ""
    hh['objects'] = list()
    try:
        for j in i['polygons']:
            wrapper = dict()
            wrapper.setdefault('modified',false)
            wrapper['polygon'] = dict()
            wrapper['polygon']['id'] = j['id']
            wrapper['polygon']['vertexes'] = j['vertexes']
            wrapper['polygon']['vector'] = []
            hh['objects'].append(wrapper)
    except:
        continue
    hh['result'] = ""
    hh['source'] = i['source']
    new.append(hh)

with open('auchan-20-new.json','w') as nf:
    nf.write(json.dumps(new))
