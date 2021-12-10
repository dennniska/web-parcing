# Задание 2
# Выбрать любой сайт с каталогом товаров и написать парсер

import requests
from bs4 import BeautifulSoup

URL = 'https://www.eldorado.ru/c/televizory/'
HEADERS = {
   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}


def get_html(url, params=''):
   return requests.get(url)

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('ul', class_='oh')
    for i, item in enumerate(items):
        for img in item.find_all('img'):
            if len(img.get('alt'))>0:
                f.write(img.get('alt')+"\n") 
    f.close()

f = open('Телевизоры на ELDORADO.txt',"w")
html = get_html(URL).text
get_content(html)




