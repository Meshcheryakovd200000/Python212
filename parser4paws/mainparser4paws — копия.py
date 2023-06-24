import re
import requests
from bs4 import BeautifulSoup
import csv


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

        writer.writerow((data['name'], data['url']))


def refinedname(s):
    return re.sub(r"^\s+|\s+$", "", s)


def refinedurl(s):
    a = re.sub(r"\s+", "", s)
    return 'https://4lapy.ru' + a


def get_data(html):
    # soup = BeautifulSoup(html, "html.parser")
    soup = BeautifulSoup(html, "lxml")  # pip install lxml
    goods = soup.find_all("div", class_="js-product-item")

    for good in goods:
        #
        name = good.find("span", class_="js-item-name").text
        # print(re.sub(r"^\s+", "", name), sep='')
        name1 = refinedname(name)
        # print(name1)

        #
        # url = good.find('a').get('href')
        url = good.find('a')['href']
        # print('https://4lapy.ru', re.sub(r"\s+", "", url), sep='')
        data = {'name': name1, "url": refinedurl(url)}
        # print(data)
        write_csv(data)


def main():
    url = 'https://4lapy.ru/catalog/sobaki/letniy-sezon/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
