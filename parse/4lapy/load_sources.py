from selenium_page import UseSelenium


def main():
    url = "https://4lapy.ru/catalog/sobaki/letniy-sezon/?section_id=1998&sort=popular&page=1"

    # Ограничим парсинг первыми 10 страницами
    MAX_PAGE = 5
    i = 1
    while i <= MAX_PAGE:
        filename = f'page_' + str(i) + '.html'
        if i == 1:
            UseSelenium(url, filename).save_page()
        else:
            url_param = url + '?page=' + str(i)
            UseSelenium(url_param, filename).save_page()

        i += 1


if __name__ == '__main__':
    main()
