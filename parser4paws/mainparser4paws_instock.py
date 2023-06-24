import re
import requests
from bs4 import BeautifulSoup
import csv

from flask.json import tag


# res = requests.get('https://4lapy.ru/shares/mobilnoe-prilozhenie-chetyre-lapy/')
# # print(res.status_code)
# # print(res.headers['content-Type'])
# # print(res.content)
# print(res.text)
# print(type(res.text))  # <class 'str'>

# ---------------------------------

def get_html(url):
    res = requests.get(url)
    return res.text


def write_csv(data):
    with open('goods.csv', 'a', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')

        writer.writerow((data['discount']))


def refinedname(s):
    return re.sub(r"^\s+|\s+$", "", s)


def refinedurl(s):
    a = re.sub(r"\s+", "", s)
    return 'https://4lapy.ru/catalog/sobaki/letniy-sezon/' + a


def get_data2(html):  # в наличии и скидка
    soup = BeautifulSoup(html, "lxml")
    goodsinstockdis = soup.find_all("div", class_="b-product-card__info")

    for good in goodsinstockdis:
        # id
        # idgood = good.find_next("div", class_="b-product-card__tab").good.find_next("div", class_="b-characteristics-tab__characteristics-value")
        # print(idgood)

        # global name1
        # name = good.find("span", class_="b-title--card").text
        # # print(re.sub(r"^\s+", "", name), sep='')
        # name1 = refinedname(name)
        # print(name1)

        # url
        url = good.find('a')['href']

        # discount +
        global discount
        discount = good.find('span', class_='js-main-old-price').text
        print(discount)

        # vnalich +

        # vnalich = good.find_all("li", class_="b-product-information__item js-current-offer-availability")

        vnalich = good.find_all('div', class_='b-product-information__value')[2].text
        print(vnalich)

        #
        data = {'discount': discount}
        # print(data)
        # write_csv(data)


def main():
    # for i in [1, 2, 3, 4, 5]:
    # for i in [1]:
    url2 = f'https://4lapy.ru/catalog/sobaki/letniy-sezon/igrushka-dlya-sobak-palochka-dlya-lakomstv-13-sm.html' \
           f'?offer=107148'
    get_data2(get_html(url2))


if __name__ == '__main__':
    main()
