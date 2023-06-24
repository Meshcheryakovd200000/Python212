import re
import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    res = requests.get(url)
    return res.text


def get_data2(html):  # в наличии и скидка
    soup = BeautifulSoup(html, "lxml")
    goodsinstockdis = soup.find_all("div", class_="b-product-card__info")

    discount = goodsinstockdis.find('span', class_='js-main-old-price').text
    print(discount)


def main():
    # for i in [1, 2, 3, 4, 5]:
    # for i in [1]:
    url2 = f'https://4lapy.ru/catalog/sobaki/letniy-sezon/igrushka-dlya-sobak-palochka-dlya-lakomstv-13-sm.html' \
           f'?offer=107148 '
    get_data2(get_html(url2))
