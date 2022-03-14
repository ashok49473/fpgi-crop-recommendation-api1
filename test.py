import requests
import json

api = r'http://127.0.0.1:5000/plant/crop_recommendation'
data = {
    "data": {
        'N': 35.0,
        'P': 7.0,
        'K': 21.0, 
        'temperature': 20.03619494, 
        'humidity': 64.28791388,
        'ph': 7.741418772
        }
    }

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  
payload = json.dumps(data)
response = requests.post(api, data=payload, headers=headers)
try:
    data = response.json()     
    print(data)                
except requests.exceptions.RequestException:
    print(response.text)


# prediction = requests.post(url, data = data)

# print(prediction)
