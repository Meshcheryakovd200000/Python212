from requests import get
from cities import cities
from bs4 import BeautifulSoup
from json import dumps, loads

def getPage(url: str, city: str) -> str:
    response = get(url, cookies=cities[city]['cookies'], headers=cities[city]['headers'])
    return response.text

def main() -> None:
    all_stuff = []
    for city in cities.keys():
        for n in range(1, 6):
            page_stuff = {}
            catalog_url = f'https://4lapy.ru/catalog/sobaki/letniy-sezon/?section_id=1998&sort=popular&page={n}'
            page = getPage(catalog_url, city)
            soup = BeautifulSoup(page, 'lxml')
            for item in soup.findAll(class_='b-common-item'):
                brand = item.find(class_="span-strong")
                if brand:
                    product_id = item.get('data-productid')
                    page_stuff[product_id] = {}
                    page_stuff[product_id]['brand'] = brand.text.strip()
                    page_stuff[product_id]['title'] = item.find(class_="b-item-name js-item-name").text.strip()
                    page_stuff[product_id]['price'] = item.find(class_="js-price-block").text.strip()
                    page_stuff[product_id]['url'] = 'https://4lapy.ru' + item.find(
                        class_="b-common-item__description-wrap js-item-link").get('href')
                    page_stuff[product_id]['id'] = page_stuff[product_id]['url'][
                                                   page_stuff[product_id]['url'].find('offer=') + 6:]
                    page_stuff[product_id]['city'] = city
                    page_stuff[product_id]['available'] = None
            url = f'https://4lapy.ru/ajax/catalog/product-info/?section_id=1998&sort=popular&page={n}' + ''.join(
                ['&product[]=' + key for key in page_stuff.keys()])
            results = loads(getPage(url, city))['data']['products']
            for item in page_stuff:
                page_stuff[item]['available'] = results[item]['offers'][page_stuff[item]['id']]['available']
            all_stuff += [page_stuff[item] for item in page_stuff]
    with open('result.json', 'w', encoding='utf-8') as f:
        f.write(dumps(all_stuff, ensure_ascii=False))

if __name__ == '__main__':
    main()
