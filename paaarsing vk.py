import requests
from bs4 import BeautifulSoup
id = str(input())
access_token = str(input())
response = requests.get('https://api.vk.com/method/users.get?user_ids=' + id + '&fields=bdate&access_token=' + access_token + '&v=5.131')
print(response.json())
