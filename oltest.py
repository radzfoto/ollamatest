import requests
import json

url = 'http://localhost:11434/api/generate'

headers = {
    'Content-Type': 'application/json'
}

data = {
    'model': 'zephyr',
    'prompt': 'Why is the sky blue?',
    'stream': True
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    response_text = response.text
    print(response.text)
    # data = json.loads(response_text)
    # actual_response = data['response']
    # print(actual_response)
else:
    print('Error: ', response.status_code, response.text)