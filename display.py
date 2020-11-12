

import requests
from bs4 import BeautifulSoup

URL = 'https://www.yandex.ru/search/?text=' + str(input('Что будем искать?: ') + '&lr=51')
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/48.0.2564.48 Safari/537.36 Study_parse',
    'accept': '*/*'}
system_class = 'serp-adv__found'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.find_all('a', class_='organic__url')

    max_pages = soup.find('div', class_=system_class)
    print(max_pages)
    name_dict = []
    for item in items:
        name_dict.append({
            item.find('div', class_='organic__url-text').get_text(strip=True): item.get('href'),
        })

    print(name_dict, sep="\n")



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        name_dict = get_content(html.text)
    else:
        print('Error: ' + html.status_code)


parse()
