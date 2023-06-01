from selenium.webdriver.common.by import By

from homework5.framework.base_page import BasePage
from homework5.wework_app.contact.list_page import ListPage


class WeworkPage(BasePage):
    def __init__(self,driver=None,caps=None):
        caps={}
        caps['noReset']=True
        caps['appPackage']='com.tencent.wework'
        caps['appActivity']='.launch.LaunchSplashActivity'
        super().__init__(driver,caps)
        # self.driver.implicitly_wait(3)
    def 通讯录(self) ->ListPage:
        #主界面右下角的通讯录
        self.click(By.XPATH,'//*[@text="通讯录"]')
        return ListPage(self.driver)
    def 工作台(self):
        ...