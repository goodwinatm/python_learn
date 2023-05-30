import json

from selenium import webdriver
from selenium.webdriver.common.by import By

from homework5.utils import get_project_dir
from homework5.wework.contact_page import ContactPage


class MainPage:
    # 自动带cookie登录
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        with open(get_project_dir('data\cookies.json')) as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
    def to_contact(self) -> ContactPage:
        self.driver.find_element(By.CSS_SELECTOR,'#menu_contacts').click()
        return  ContactPage(self.driver)