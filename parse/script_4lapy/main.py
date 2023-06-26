from requests import get
from headers import headers, cookies
from bs4 import BeautifulSoup
from json import dumps


def getPage(url: str) -> str:
    response = get(url, cookies=cookies, headers=headers)
    return response.text


def main():
    urls = []
    for n in range(1, 2):
        catalog_url = f'https://4lapy.ru/catalog/sobaki/zashchita-ot-blokh-i-kleshchey-sobaki/?section_id=326&sort=popular&page={n}'
        page = getPage(catalog_url)
        soup = BeautifulSoup(page, 'lxml')
        urls += list(map(lambda x: 'https://4lapy.ru' + x.get('href'),
                         soup.findAll(class_='b-common-item__image-link js-item-link')))
    data = []
    for url in urls:
        item = {}
        page = getPage(url)
        soup = BeautifulSoup(page, 'lxml')
        item['url'] = url
        item['id'] = url[url.find('offer=') + 6:]
        item['title'] = soup.find('h1').text
        item['brand'] = soup.find(itemprop="brand").text
        item['price'] = soup.find(
            class_="b-product-information__price js-price-product js-current-offer-price js-main-price").text
        item['old-price'] = soup.find(
            class_="b-product-information__old-price js-main-old-price js-current-offer-price-old").text
        data.append(item)

    print(data)

    # with open('result.json', 'w', encoding='utf-8') as f:
        # f.writelines(dumps(data, ensure_ascii=False))


if __name__ == '__main__':
    main()
