import requests
import json

id = 3
payloads = {'id':id, }
url = 'http://127.0.0.1:8000/snippets/'

#GET
#res = requests.get(url,params=payloads)
#DELETE
res = requests.delete(url,params=payloads)

print(res.url)

data = json.loads(res.text)

#print (data)
