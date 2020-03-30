import requests
from bs4 import BeautifulSoup



def getWeather():
    url='http://wthrcdn.etouch.cn/weather_mini?city=太原'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    }
    res =requests.get(url=url,headers=headers)
    forecast=res.json()['data']['forecast']
    type_we=[]
    for fore in forecast[0:2]:
        type_we.append(fore['type'])
    return  type_we