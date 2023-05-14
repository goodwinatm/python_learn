import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class SearchPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search(self, keyword) -> 'SearchPage':
        query = self.driver.find_element(By.CSS_SELECTOR, 'input.search-query')
        query.clear()
        query.send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, '.search-bar .search-cta').click()
        return self

    # 1.切换三个话题，在不同类目中搜索
    def select_search_1(self, keyword) -> 'SearchPage':
        self.driver.find_element(By.CSS_SELECTOR, 'summary#search-type-header .name').click()
        self.driver.find_element(By.CSS_SELECTOR,'div#search-type-body > ul > li:nth-of-type(1)').click()
        # self.driver.find_element(By.CSS_SELECTOR,'div#search-type-body > ul > li:nth-of-type(2)').click()
        # self.driver.find_element(By.CSS_SELECTOR,'div#search-type-body > ul > li:nth-of-type(3)').click()

        query = self.driver.find_element(By.CSS_SELECTOR, 'input.search-query')
        query.clear()
        query.send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, '.search-bar .search-cta').click()
        return self
    def select_search_2(self, keyword) -> 'SearchPage':
        self.driver.find_element(By.CSS_SELECTOR, 'summary#search-type-header .name').click()
        # self.driver.find_element(By.CSS_SELECTOR,'div#search-type-body > ul > li:nth-of-type(1)').click()
        self.driver.find_element(By.CSS_SELECTOR,'div#search-type-body > ul > li:nth-of-type(2)').click()
        # self.driver.find_element(By.CSS_SELECTOR,'div#search-type-body > ul > li:nth-of-type(3)').click()

        query = self.driver.find_element(By.CSS_SELECTOR, 'input.search-query')
        query.clear()
        query.send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, '.search-bar .search-cta').click()
        return self
    def select_search_3(self, keyword) -> 'SearchPage':
        self.driver.find_element(By.CSS_SELECTOR, 'summary#search-type-header .name').click()
        # self.driver.find_element(By.CSS_SELECTOR,'div#search-type-body > ul > li:nth-of-type(1)').click()
        # self.driver.find_element(By.CSS_SELECTOR,'div#search-type-body > ul > li:nth-of-type(2)').click()
        self.driver.find_element(By.CSS_SELECTOR,'div#search-type-body > ul > li:nth-of-type(3)').click()

        query = self.driver.find_element(By.CSS_SELECTOR, 'input.search-query')
        query.clear()
        query.send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, '.search-bar .search-cta').click()
        return self
    def posted_by_search(self, keyword,poster) -> 'SearchPage':
        self.driver.find_elements(By.CSS_SELECTOR, '.formatted-selection')[1].click()
        # self.driver.find_element(By.CSS_SELECTOR,'div#search-type-body > ul > li:nth-of-type(1)').click()
        # self.driver.find_element(By.CSS_SELECTOR,'div#search-type-body > ul > li:nth-of-type(2)').click()
        # self.driver.find_element(By.CSS_SELECTOR,'div#search-type-body > ul > li:nth-of-type(3)').click()

        post = self.driver.find_element(By.CSS_SELECTOR, 'input.filter-input')
        post.clear()
        post.send_keys(poster)



        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.select-kit-row')))
        self.driver.find_elements(By.CSS_SELECTOR, '.select-kit-row')[0].click()

        #select before
        self.driver.find_element(By.XPATH,"//details[@id='postTime']").click()
        self.driver.find_elements(By.CSS_SELECTOR, 'li.select-kit-row')[0].click()
        #selct date
        # self.driver.execute_script("document.getElementById('search-post-date').removeAttribute('readonly');")
        date =self.driver.find_element(By.CSS_SELECTOR, 'input.date-picker')
        date.clear()
        date.send_keys('04042022')

        query = self.driver.find_element(By.CSS_SELECTOR, 'input.search-query')
        # query.clear()
        query.send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, '.search-bar .search-cta').click()
        return self
    def get_search_result(self) -> list[str]:
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.topic-title')))

        title_list = []
        for element in self.driver.find_elements(By.CSS_SELECTOR, '.topic-title'):
            title_list.append(element.text)

        return title_list
    def get_search_tag_result(self) -> list[str]:
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.fps-tag-item')))

        title_list = []
        for element in self.driver.find_elements(By.TAG_NAME, 'a'):
            title_list.append(element.text)
        print(title_list)
        return title_list
    def get_search_user_result(self) -> list[str]:
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.user-titles')))

        title_list = []
        # for element in self.driver.find_elements(By.TAG_NAME, 'span'):
        for element in self.driver.find_elements(By.CLASS_NAME, 'username'):
            title_list.append(element.text)
        print(title_list)
        return title_list

    def get_search_post_result(self) -> list[str]:
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.topic-title')))

        title_list = []
        # for element in self.driver.find_elements(By.TAG_NAME, 'span'):
        for element in self.driver.find_elements(By.CSS_SELECTOR, 'span.topic-title'):
            title_list.append(element.text)
        print(title_list)
        return title_list
    def close(self):
        self.driver.quit()
