import requests

import pprint

import datetime

city = input('Введите город  ', )
app_id = '7732bdde0a28cc9ee8dbaf3488444130'
responce = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={app_id}')
responce = responce.json()
responce_city = responce['city']
responce_list = responce['list']


def weather_temp_description(hour):
    """Функция выводит погоду, в качестве передаваемого параметра кол-во часов после текущего времени"""
    responce_list_1 = responce_list[hour]
    responce_list_1_dt_txt = responce_list_1['dt_txt']
    responce_list_1_main_temp = responce_list_1['main']['temp']
    temp = responce_list_1_main_temp-273
    responce_list_1_weather_1 = responce_list_1['weather'][0]
    print(responce_list_1_dt_txt[0:10], '    ', int(temp), '    ', responce_list_1_weather_1['description'])


for i in [0, 8, 16]:
    weather_temp_description(i)

