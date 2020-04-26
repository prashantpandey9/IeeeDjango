import requests

import json

api="https://api.covid19india.org/data.json"

s=(requests.get(api)).text

data=json.loads(s)
b=1
for j in data['statewise']:
##    print(j['state'])
    if j['state']=="Uttarakhand":
        print(j['active'])
##    print(b)
    b+=1
