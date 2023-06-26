from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random

# import lib.config


class UseSelenium:
    def __init__(self, url: str, filename: str):
        self.url = url
        self.filename = filename

    def save_page(self):
        # persona = self.__get_headers_proxy()

        options = webdriver.ChromeOptions()
        # options.add_argument(f"user-agent={persona['user-agent']}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless")

        options_proxy = {
            'proxy': {
                # 'https': persona['http_proxy'],
                'no_proxy': 'localhost,127.0.0.1:8080'
            }
        }

        s = Service(executable_path="/lib/chromedriver")

        driver = webdriver.Chrome(options=options, service=s, seleniumwire_options=options_proxy)

        try:
            driver.get(self.url)
            time.sleep(3)
            driver.execute_script("window.scrollTo(5,4000);")
            time.sleep(5)
            html = driver.page_source
            with open('pages/' + self.filename, 'w', encoding='utf-8') as f:
                f.write(html)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()

    # def __get_headers_proxy(self) -> dict:
    #     '''
    #     The config file must have dict:
    #         {
    #             'http_proxy':'http://user:password@ip:port',
    #             'user-agent': 'user_agent name'
    #         }
    #     '''
    #
    #     try:
    #         users = lib.config.USER_AGENTS_PROXY_LIST
    #         persona = random.choice(users)
    #     except ImportError:
    #         persona = None
    #     return persona
