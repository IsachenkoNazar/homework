import requests
# Імпортуємо модуль reguests
from .read_json import read_json
# Імпортуємо функцію read_json
import json
# Імпортуємо модуль json
data_api = read_json(name_file= 'config_api.json')
# Створення змінної 
API_KEY = data_api['api_key']
# Створення ключа
CITY_NAME = data_api['city_name']
# Створення ключа
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
# Налаштування константи
response = requests.get(URL)
# створення змінної 
if response.status_code == 200:
    # створення умови за допомогою оператора if
    data_dict = json.loads(response.content)
    # створення змінної data_dict
    print(json.dumps(data_dict, indent= 4))