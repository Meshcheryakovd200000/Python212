import re
import requests
from bs4 import BeautifulSoup
import csv
import mainparser4paws_instock

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

        writer.writerow((data['id'], data['name'], data['url'], data['price'], data['brand']))


def refinedname(s):
    return re.sub(r"^\s+|\s+$", "", s)


def refinedurl(s):
    a = re.sub(r"\s+", "", s)
    return 'https://4lapy.ru' + a


# def get_data2(html):  # в наличии и скидка
#     soup = BeautifulSoup(html, "lxml")
#     goodsinstockdis = soup.find_all("div", class_="b-product-card__info")
#
#     for good in goodsinstockdis:
#         # discount
#         discount = good.fing("span", class_="b-product-information__old-price")
#         print(discount)


def get_data(html):
    # soup = BeautifulSoup(html, "html.parser")
    soup = BeautifulSoup(html, "lxml")  # pip install lxml
    # goods = soup.find_all("div", class_="js-product-item")
    goods = soup.find_all("div", class_="b-common-item--catalog-item")

    for good in goods:
        # id
        global idgood, discount
        idgood = good.get('data-product-articul')
        # print(idgood)

        #
        global name1
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

        ##########################
        # price2 = good.find(r"^\d\s*", 'span', class_="b-common-item__prev-price js-sale-origin")
        # # price3 = price2.replace("&nbsp;", " ")
        # # price3 = good.find(re.sub(r"^\s+", "", price2), sep='')
        # print(re.sub(r"^\d\s*", "", price2), sep='')

        #
        # pricediscount = good.find('span', class_="js-current-offer-price-old")
        # # pricediscount = good.get('style="display: block;"')
        # print(pricediscount)

        #
        brand = good.find('span', class_="span-strong").text
        # print(brand)

        #
        discount = None

        # discount = good.find('span', class_='js-main-old-price').text
        # print(discount)

        vnalich = 'yes'

        data = {'id': idgood, 'name': name1, "url": refinedurl(url), "price": price, "brand": brand}
        # print(data)
        write_csv(data)


def main():
    for i in [1, 2, 3, 4, 5]:
        # for i in [3]:
        url = f'https://4lapy.ru/catalog/sobaki/letniy-sezon/?section_id=1998&sort=popular&page={i}'
        # url2 = f'https://4lapy.ru/catalog/sobaki/letniy-sezon/{name1}'
        get_data(get_html(url))
        # get_data(get_html(url2))

    # for i in [1]:
    #     url2 = f'https://4lapy.ru/catalog/sobaki/letniy-sezon/{name1}'
    #     get_data(get_html(url2))


if __name__ == '__main__':
    main()
