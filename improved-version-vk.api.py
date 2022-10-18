import requests
import json

def request(id):
    https1 = 'https://api.vk.com/method/users.get?user_ids='
    https2 = '&fields=bdate&access_token='
    https3 = '&v=5.131'
    global response
    access_token = 'vk1.a.yKxxTovFfRF_K3RcLpZWBnO3N62ukrfVwgxAcebEakPJrUXReyvPDEX_z5lTNNwoUwKCPn98qWDGmvOawpialEJPDMQrIjQHE-2FDLqXBRZpRNzIrpCxP8fWpIV3zp26Uv5ncOPt4uwI_ANsItUcTGrnZ2ijCzbPDLL57LdzlNB_8mQ9nYR6dD1Dh90DQ0jZ'
    response = requests.get(https1 + id + https2 + access_token + https3)
    response = response.json()


request(str(input(id)))

with open('json-file', 'w') as file:
    json.dump(response, file, indent=3)
with open('json-file', 'r') as file:
    json_code = json.load(file)
for element in json_code['response']:
    for keys in element:
        if keys == 'id' or keys == 'first_name' or keys == 'last_name':
            print(keys + ':', element[keys])
            id = str(element['id'])
    with open('users', 'a') as file:
        file.write('\n')
        file.write('имя: ')
        file.write(element['first_name'])
        file.write('\n')
        file.write('фамилия: ')
        file.write(element['last_name'])
        file.write('\n')
        file.write('id: ')
        file.write(id)
        file.write('\n')