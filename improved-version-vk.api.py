import requests
import json
id = str(input())
access_token = str(input())
response = requests.get('https://api.vk.com/method/users.get?user_ids=' + id + '&fields=bdate&access_token=' + access_token + '&v=5.131')
response = response.json()
with open('json-file', 'w') as file:
    json.dump(response, file, indent=3)
with open('json-file', 'r') as file:
    json_code = json.load(file)
for i in json_code['response']:
    print('имя:', i['first_name'], 'фамилия:', i['last_name'], 'id:', i['id'], sep='\n')
    print()
    with open('users', 'a') as file:
        file.write(i['first_name'])
        file.write('\n')
        file.write(i['last_name'])