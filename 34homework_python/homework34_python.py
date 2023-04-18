import requests
from bs4 import BeautifulSoup
import csv


# работа с функциями, спарсим данные с нескольких страниц:

# "1" Найти в "Скачать программы для компьютера бесплатно" данные про ТОП-10, само содержимое
# "2" ссылки
# "3" рейтинг
# "4" сохранение в csv

def get_html(url):
    res = requests.get(url)
    return res.text


def write_csv(data):
    with open('soft.csv', 'a', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')
        writer.writerow((data['name'], data['url'], data['rating']))


def get_data(html):
    # soup = BeautifulSoup(html, "html.parser")
    soup = BeautifulSoup(html, "lxml")  # pip install lxml
    element = soup.find_all('div', class_='bb')  # 'article' - тег
    for el in element:
        try:
            name = el.find('div').text
        except ValueError:
            name = ''
        # print(name)
        try:
            url = el.find('a').get('href')  # "2"
        except ValueError:
            url = ''
        # print(url)
        try:
            rating = el.find('div', class_="post-ratings").text.strip()  # рейтинг "3"
        except ValueError:
            rating = ''

        # print(rating)

        data = {
            'name': name,
            'url': url,
            'rating': rating
        }

        write_csv(data)


def main():
    for i in range(1, 19):
        url = f'https://soft-file.ru/internet/page/{i}/'
        get_data(get_html(url))


if __name__ == '__main__':
    main()
