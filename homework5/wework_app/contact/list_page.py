from __future__ import annotations

from selenium.webdriver.common.by import By

import homework5
from homework5.framework.base_page import BasePage
# from homework5.wework_app.contact.admin_page import AdminPage
from homework5.wework_app.contact.profile_page import ProfilePage
from appium.webdriver.common.appiumby import AppiumBy


class ListPage(BasePage):
    _search_button=dict(by=AppiumBy.ID, value='com.tencent.wework:id/lf_')
    _item=dict(by=AppiumBy.ID, value='com.tencent.wework:id/esg')
    _admin=dict(by=AppiumBy.ID, value='com.tencent.wework:id/lf5')
    _input=dict(by=AppiumBy.ID, value='com.tencent.wework:id/jn1')

    def 管理(self)->'AdminPage':
        # adb devices
        # adb connect 127.0.0.1:7555
        #右上角管理按钮
        self.click(**self._admin)
        from homework5.wework_app.contact.admin_page import AdminPage
        return AdminPage(self.driver)
    def 搜索(self,keyword)->ProfilePage:
        self.click(**self._search_button)
        self.send_keys(**self._input,text=keyword)
        self.click(**self._item)
        return ProfilePage(self.driver)
    def 浏览(self,name) -> ProfilePage:
        ...
