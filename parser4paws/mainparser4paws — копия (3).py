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
    with open('goods.csv', 'a', encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')

        writer.writerow((data['id'], data['name'], data['url'], data['price'], data['brand']))


def refinedname(s):
    return re.sub(r"^\s+|\s+$", "", s)


def refinedurl(s):
    a = re.sub(r"\s+", "", s)
    return 'https://4lapy.ru' + a


def get_data(html):
    # soup = BeautifulSoup(html, "html.parser")
    soup = BeautifulSoup(html, "lxml")  # pip install lxml
    # goods = soup.find_all("div", class_="js-product-item")
    goods = soup.find_all("div", class_="b-common-item--catalog-item")



    #!!!!!!!!!!!!!!!!!!  в наличии
    # for good2 in goods2
    goodsinstock = soup.find_all("div", class_="b-product-information__value")
    print(goodsinstock)

    # instock = goodsinstock.find("div", class_="b-product-information__value")

    for good in goods:
        # id
        idgood = good.get('data-product-articul')
        # print(idgood)

        #
        name = good.find("span", class_="js-item-name").text
        # print(re.sub(r"^\s+", "", name), sep='')
        name1 = refinedname(name)
        # print(name1)

        #
        # url = good.find('a').get('href')
        url = good.find('a')['href']
        # print('https://4lapy.ru', re.sub(r"\s+", "", url), sep='')

        price = good.find('span', class_="js-price-block").text
        # print(price)

        #
        pricediscount = good.find('span', class_="b-common-item__price_discount")
        # if pricediscount != 0:
        # print(pricediscount)

        #
        brand = good.find('span', class_="span-strong").text
        # print(brand)

        #
        data = {'id': idgood, 'name': name1, "url": refinedurl(url), "price": price, "brand": brand}
        print(data)
        # write_csv(data)


def main():
    # for i in [1, 2, 3, 4, 5]:
    for i in [4]:
        url = f'https://4lapy.ru/catalog/sobaki/letniy-sezon/?section_id=1998&sort=popular&page={i}'
        get_data(get_html(url))


if __name__ == '__main__':
    main()
