from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from homework4.homework4_pages.search_page import SearchPage


class MainPage:
    def __init__(self):
        # options = webdriver.ChromeOptions()
        # options.add_argument('--lang=zh-CN')
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome()

    def get_topic_list(self) -> list[dict]:
        ...

    # def to_login(self) ->SearchPage:
    #     self.driver.get("https://ceshiren.com")
    #     self.driver.find_element(By.CSS_SELECTOR, ".login-button").click()
    def to_login(self):
        self.driver.get("https://ceshiren.com")
        self.driver.find_element(By.CSS_SELECTOR, ".login-button").click()
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.login-title')))
        self.driver.find_element(By.CSS_SELECTOR, '#login-account-name').send_keys('guy52911@hotmail.com')
        self.driver.find_element(By.CSS_SELECTOR, '#login-account-password').send_keys('hogwarts')
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, 'div>.avatar[title="guy52911_no_phone"]')))

    def to_search_advance(self) -> SearchPage:
        # self.driver.get("https://ceshiren.com")
        # self.driver.find_element(By.CSS_SELECTOR, ".login-button").click()
        # WebDriverWait(self.driver, 2).until(
        #     expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.login-title')))
        # self.driver.find_element(By.CSS_SELECTOR, '#login-account-name').send_keys('guy52911@hotmail.com')
        # self.driver.find_element(By.CSS_SELECTOR, '#login-account-password').send_keys('hogwarts')
        # self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()

        self.driver.find_element(By.CSS_SELECTOR, ".d-icon-search").click()
        # self.driver.find_element(By.CSS_SELECTOR, '#search-button[title=搜索]').click()
        #self.driver.find_element(By.XPATH, '//div[@id="search-button"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.show-advanced-search').click()
        return SearchPage(self.driver)

    def close(self):
        self.driver.quit()

    def to_logout(self):
        self.driver.find_element(By.CSS_SELECTOR, 'div>.avatar[title="guy52911_no_phone"]').click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, 'button.user-preferences-link[title="偏好设置"]')))
        self.driver.find_element(By.CSS_SELECTOR, 'button.user-preferences-link[title="偏好设置"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'button.widget-button>span.d-button-label').click()
