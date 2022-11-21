import requests
import json


def name_vk_user(id):
    https1 = 'https://api.vk.com/method/users.get?user_ids='
    https2 = '&fields=bdate&access_token='
    https3 = '&v=5.131'
    access_token = 'access_token'
    response = requests.get(https1 + id + https2 + access_token + https3)
    response = response.json()

    with open('pars_group/json-file', 'w') as file:
        json.dump(response, file, indent=3)
    with open('pars_group/json-file', 'r') as file:
        json_code = json.load(file)
    for element in json_code['response']:
        for keys in element:
            if keys == 'id' or keys == 'first_name' or keys == 'last_name':
                print(keys + ':', element[keys])
                id = str(element['id'])
        with open('pars_group/users', 'a') as file:
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

name_vk_user(str(input(id)))
