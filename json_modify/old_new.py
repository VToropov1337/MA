import json

old = list()
new = list()
false = False
true = True



with open('magnit.json','r') as f2:
    old = json.loads(f2.read())


c = 0
for i in old:
    hh = dict()
    hh['data'] = ''
    hh['class'] = ''
    hh['objects'] = list()
    for j in i['polygons']:
        smpl = dict()
        polygon = dict()
        smpl['modified'] = false
        smpl['polygon'] = dict()
        smpl['polygon']['id'] = j['id']
        smpl['polygon']['vector'] = []
        smpl['polygon']['vertexes'] = j['vertexes']
        hh['objects'].append(smpl)

    hh['result'] = ''
    hh['source'] = i['source']
    new.append(hh)




with open('magnit-new.json','w') as nf:
    nf.write(json.dumps(new))
