# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

from pprint import pprint
import requests
import json

user_name = input('Enter the github username:')
main_link = f'https://api.github.com/users/{user_name}/repos'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/81.0.4044.138 Safari/537.36',
          'Accept':'*/*'}

response = requests.get(main_link, headers=header)
if response.ok:
    data = json.loads(response.text)

repos = []
for i in data:
    repos.append(i['name'])


print(f'У пользователя {user_name} имеется {len(repos)} репозиториев. '
      f'Список репозиториев: ', *repos, sep='\n')

# 2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
