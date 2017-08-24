import requests
import json


#GET
#res = requests.get('http://127.0.0.1:8000/snippets/1/')

#DELETE
#res = requests.delete('http://127.0.0.1:8000/snippets/3/')

print(res.url)

data = json.loads(res.text)

#print (data)
