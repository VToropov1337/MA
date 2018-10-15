import json

with open('spar_453.pred.json','r') as f:
    hh = json.load(f)


c = 0

for i in hh:
    if i['pred_objects'] == []:
        continue

    for j in i['pred_objects'][0]['sub_objects']:
            # print(j)
        if j['class'] == 'sk' and len(j['text']) == 13:
            print(j['text'],i['url'])
            c +=1
        else:
            continue


print(c)
