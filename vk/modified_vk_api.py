import json
import requests
from time import sleep



def vk_api(id, chet):
    https1 = 'https://api.vk.com/method/users.get?user_ids='
    https2 = '&fields=bdate&access_token='
    https3 = '&v=5.131'
    access_token = 'token'
    response = requests.get(https1 + str(id) + https2 + access_token + https3)
    sleep(3)
    response = response.json()
    count = chet - 999 - 3
    info = {'users': []}

    for element in response['response']:
        if count == -2:
            count = 1
        elif count == -1:
            count = 2
        elif count == 0:
            count = 3
        id = str(element['id'])
        info['users'].append('Порядковый номер:' + str(count))
        info['users'].append('Имя:' + element['first_name'])
        info['users'].append('Фамилия:' + element['last_name'])
        info['users'].append('ID:' + id)
        info['users'].append('')
        count += 1

    with open('users_json', 'a') as file:
        json.dump(info, file, ensure_ascii=False, indent=3)
