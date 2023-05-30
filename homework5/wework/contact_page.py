from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class ContactPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_member(self, name, account, email=None, mobile=None, depart=None) -> 'ContactPage':
        def loop_click(driver):
            self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Add Members').click()
            return self.driver.find_element(By.NAME, 'username')

        WebDriverWait(self.driver, 20).until(loop_click)

        self.driver.find_element(By.NAME, 'username').send_keys(name)
        self.driver.find_element(By.NAME, 'acctid').send_keys(account)
        self.driver.find_element(By.NAME, 'mobile').send_keys(mobile)
        self.driver.find_element(By.LINK_TEXT, 'Save').click()
        sleep(3)
        return self

    # 批量导入通讯录文件
    def import_from_file(self, path) -> 'Contactpage':
        ...

    def search(self, keyword) -> 'ContactPage':
        self.driver.find_element(By.CSS_SELECTOR, '#memberSearchInput').send_keys(keyword)

        return self

    def get_first_search_result(self) -> dict:
        WebDriverWait(self.driver, 10).until(
            lambda x: self.driver.find_element(By.CSS_SELECTOR, '.member_display_cover_detail_name').text != ''
        )
        name = self.driver.find_element(By.CSS_SELECTOR, '.member_display_cover_detail_name').text
        account = self.driver.find_elements(By.CSS_SELECTOR, '.member_display_cover_detail_bottom')[-1].text
        r = {
            'name': name,
            'account': account
        }
        print(r)
        return r

    def refresh(self):
        self.driver.refresh()
