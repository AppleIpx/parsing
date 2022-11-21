from time import sleep
import requests
from vk_api import vk_api

def request():
    users = []
    Access_token = 'vk1.a.yKxxTovFfRF_K3RcLpZWBnO3N62ukrfVwgxAcebEakPJrUXReyvPDEX_z5lTNNwoUwKCPn98qWDGmvOawpialEJPDMQrIjQHE-2FDLqXBRZpRNzIrpCxP8fWpIV3zp26Uv5ncOPt4uwI_ANsItUcTGrnZ2ijCzbPDLL57LdzlNB_8mQ9nYR6dD1Dh90DQ0jZ'
    group_id = 'voronezhnetip'
    offset = str(1000)
    link = 'https://api.vk.com/method/groups.getMembers?group_id=' + group_id + '&offset=' + offset + '&access_token=' + Access_token + '&v=5.131'
    response = requests.get(link)
    str_response = response.text
    Json = response.json()
    dict = eval(str_response)
    total = int(Json['response']['count'])
    repetition_whole = total // 1000
    for user in dict['response']['items']:
        users.append(user)


    for i in range(repetition_whole + 1):
        offset = int(offset) + 1000
        link = 'https://api.vk.com/method/groups.getMembers?group_id=' + group_id + '&offset=' + str(offset) + '&access_token=' + Access_token + '&v=5.131'
        res = requests.get(link)
        str_res = res.text
        dict = eval(str_res)
        for user in dict['response']['items']:
            users.append(user)
        sleep(1)
    count = 0
    for i in range(0, len(users), 1000):
        count += 1000
        vk_api(users[i:count])




request()
