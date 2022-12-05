import requests
import json



def name_vk_user(id):
    data = ''
    https1 = 'https://api.vk.com/method/users.get?user_ids='
    https2 = '&fields=bdate&access_token='
    https3 = '&v=5.131'
    access_token = 'token'
    response = requests.get(https1 + id + https2 + access_token + https3)
    response = response.json()


    for element in response['response']:
        for keys in element:
            if keys == 'id' or keys == 'first_name' or keys == 'last_name':
                id = str(element['id'])
                #print(keys + ':', element[keys])
                info = (str(keys) + str(':') + str(element[keys]))
                data += info + ' '

        return data
    #print(data)
#name_vk_user(str(input()))

