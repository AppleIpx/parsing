from modified_vk_api import vk_api
import json

with open('users_ids_copy', 'r') as file:
    chet = 0
    a = file.read()
    a = json.loads(a)

for i in range(0, len(a) + 1, 1000):
    chet += 1000
    vk_ids = a[i:chet]
    vk_api(vk_ids, chet)