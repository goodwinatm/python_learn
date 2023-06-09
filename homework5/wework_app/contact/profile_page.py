from appium.webdriver.common.appiumby import AppiumBy

from homework5.framework.base_page import BasePage


class ProfilePage(BasePage):
    _name = dict(by=AppiumBy.ID, value='com.tencent.wework:id/kps')
    _mail = dict(by=AppiumBy.ID, value='com.tencent.wework:id/c22')
    _depart = (AppiumBy.ID, 'com.tencent.wework:id/cad')

    def get_info(self) -> dict:
        name = self.driver.find_element(**self._name).text
        mail = self.driver.find_element(**self._mail).text
        depart = self.driver.find_element(*self._depart).text
        return dict(name=name, mail=mail, depart=depart)
