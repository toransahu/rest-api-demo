import requests
import json
 
str = 'raw mango'
payloads = {'api_key':'DEMO_KEY','format':'json','q':str, }
res = requests.get('https://api.nal.usda.gov/ndb/search/',params=payloads)
 
print(res.url)

data = json.loads(res.text)

print (data)