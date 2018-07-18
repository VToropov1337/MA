import requests

arr = [{"url": "https://***.com/***/***/***/answer/image/***/3f1cc367-d5f3-4e71-ae7c-ea702175cf0f.jpg", "report_id": 15722987, "store_title": "\u0421\u041f\u0410\u0420"}, {"url": "https://***.com/***/***/***/answer/image/***/5d65079c-301a-464b-914d-5e6296ddaaaa.jpg", "report_id": 15722988, "store_title": "\u0421\u041f\u0410\u0420"}]
for i in range(len(arr)):
    url = arr[i]['url']
    r = requests.get(url).content

    with open('/path/{}'.format(arr[i]['store_title'] + ' ' + arr[i]['url'].split('/')[-1]), 'wb') as f:
        f.write(r)
