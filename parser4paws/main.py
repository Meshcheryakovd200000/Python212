import requests
from bs4 import BeautifulSoup
import json

PAGES_COUNT = 1
OUT_FILENAME = 'out.json'


def get_soup(url, **kwargs):
    response = requests.get(url, **kwargs)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features='html.parser')
    else:
        soup = None
    return soup


def crawl_products(pages_count):
    urls = []
    fmt = f'https://4lapy.ru/catalog/sobaki/letniy-sezon/?section_id=1998&sort=popular&page={pages_count}'

    for page_n in range(1, 1 + pages_count):
        print('page: {}'.format(page_n))

        page_url = fmt.format(page=page_n)
        soup = get_soup(page_url)
        if soup is None:
            break

        for tag in soup.select('b-item-name js-item-name'):
            href = tag.attrs['href']
            url = 'https://4lapy.ru/{}'.format(href)
            urls.append(url)

    return urls


def parse_products(urls):
    data = []
    for url in urls:
        print('\tproduct: {}'.format(url))
        soup = get_soup(url)
        if soup is None:
            break

        name = soup.select_one('b-title b-title--h1 b-title--card').text.strip()
        amount = soup.select_one('b-product-information__price js-price-product js-current-offer-price js-main-price '
                                 'active').text.strip()
        vnalich = soup.select_one('b-product-information__value').text.strip()

        item = {
            'name': name,
            'amount': amount,
            'vnalich': vnalich
        }
        data.append(item)

    return data


def main():
    urls = crawl_products(PAGES_COUNT)
    print('\n'.join(urls))

    data = parse_products(urls)

    with open(OUT_FILENAME, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)


if __name__ == '__name__':
    main()
