import requests
import time
import json
import traceback
import tqdm

token = ***
base_url = 'https:***.com'

headers = {'Content-Type': 'application/json; charset=utf-8',
           'X-SERVICE-TOKEN': token }
send_method = '/api/***'
get_method = '/api/***'

def get_job_id_for_url(url):
    assert isinstance(url, str), 'url should be a string'
    r = requests.post(base_url+send_method, headers=headers,
                      data=json.dumps({'urls': [url]}))
    job_id = r.json()
    return job_id['result']['job_id']
def get_prediction(job_id):
    assert isinstance(job_id, int), 'job_id should be an int'
    r = requests.post(base_url+get_method, headers=headers,
                      data=json.dumps({'job_id': job_id}))
    return r.json()
with open('***.json', 'r') as f:
    data = json.load(f)
full_prediction = []
for example in tqdm.tqdm(data):
#    try:
            job_id = get_job_id_for_url(example['url'])
        result = get_prediction(job_id)
        if job_id:
            print('job id is: ',job_id)
            while(not result['ok']):
                time.sleep(1)
                result = get_prediction(job_id)
                print(result)
#            full_prediction.append({'report_id': example['report_id'],
#                                    'store_title': example['store_title'],
#            'predictions': result['result']['images']})
#    except:
#        print(example['url'])
#        traceback.print_exc()

with open('full_pred_from_remote.json','w') as f:
    json.dump(full_prediction,f)
