import requests
from bs4 import BeautifulSoup
import re
import csv


# "1" Найти в "Скачать программы для компьютера бесплатно" данные про ТОП-10, само содержимое
# "2" ссылки
# "3" рейтинг
# "4" сохранение в csv

def get_html(url):
    res = requests.get(url)
    return res.text


def refined(s):  # "3"
    return re.sub(r"\D+", "", s)  # поиск и замена всё что не цифры


def write_csv(data):
    with open('program.csv', 'a') as f:  # открываем файл program.csv, и будем дозаписывать - 'a'
        writer = csv.writer(f, delimiter=";", lineterminator='\r')
        writer.writerow((data['name'], data['url'], data['rating']))  # список из элементов


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find("main", id="main")
    program = p1.find_all("div", class_="bb")

    for prog in program:
        name = prog.find('div').text
        # print(name)
        url = prog.find("a").get('href')  # "2"
        # print(url)
        rating = prog.find("div", class_="post-ratings").text  # рейтинг "3"
        r = refined(rating)
        # print(r)
        data = {'name': name, "url": url, "rating": r}  # 4
        # print(data)
        write_csv(data)


def main():
    url = 'https://soft-file.ru/luchshie-programmy-top10'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
