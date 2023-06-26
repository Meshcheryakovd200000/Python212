import re
import requests
from bs4 import BeautifulSoup
import csv

# res = requests.get('https://online.metro-cc.ru/virtual/morozhenoe-do-40-18455')
# print(res.status_code)
# print(res.content)
# print(res.text)
# print(type(res.text))  # <class 'str'>


def get_html(url):
    res = requests.get(url)
    return res.text


def get_data(html):
    # soup = BeautifulSoup(html, "html.parser")
    soup = BeautifulSoup(html, "lxml")  # pip install lxml
    p1 = soup.find_all('main', class_='subcategory-or-type__main')
    return p1


def main():
    # for i in [1, 2, 3, 4, 5]:
    for i in [1]:
        url = f'https://online.metro-cc.ru/virtual/morozhenoe-do-40-18455?page={i}'
        print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
