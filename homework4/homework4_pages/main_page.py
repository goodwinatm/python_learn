from selenium import webdriver
from selenium.webdriver.common.by import By

from homework4.homework4_pages.search_page import SearchPage


class MainPage:
    def __init__(self):
        # options = webdriver.ChromeOptions()
        # options.add_argument('--lang=zh-CN')
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome()

    def get_topic_list(self) -> list[dict]:
        ...

    def to_search_advance(self) -> SearchPage:
        self.driver.get("https://ceshiren.com")
        self.driver.find_element(By.CSS_SELECTOR, ".d-icon-search").click()
        # self.driver.find_element(By.CSS_SELECTOR, '#search-button[title=搜索]').click()
        #self.driver.find_element(By.XPATH, '//div[@id="search-button"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.show-advanced-search').click()
        return SearchPage(self.driver)

    def close(self):
        self.driver.quit()
