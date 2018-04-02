import os
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

path_to_driver = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'utils', 'chromedriver')


class WebSiteLoader:
    def __init__(self, desc):
        self.__driver = webdriver.Chrome(path_to_driver)
        self.__desc = desc
        self.__page = 0
        self.__loaded = False
        self.__thread = Thread(target=self.__load_next_page)
        self.__thread.start()

    def __load_next_page(self):
        self.__page += 1
        if self.__page <= self.__desc.limit:
            self.__driver.get(self.__desc.url.text.format(page=self.__page))
        else:
            self.__loaded = True

    def get_next_page(self) -> str:
        if self.__loaded:
            return None
        self.__thread.join()
        page = self.__driver.find_element(by=By.TAG_NAME, value='html')\
            .get_attribute("innerHTML")
        page = '<html>' + page + '</html>'
        self.__thread = Thread(target=self.__load_next_page)
        self.__thread.start()
        return page

    def is_all_pages_loaded(self) -> int:
        return self.__loaded

    def __del__(self):
        self.__driver.close()
