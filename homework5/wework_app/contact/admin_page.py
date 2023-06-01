from __future__ import annotations

from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

import homework5
from homework5.framework.base_page import BasePage
from homework5.wework_app.contact.list_page import ListPage


class AdminPage(BasePage):
    _add_member=dict(by=AppiumBy.ID, value="com.tencent.wework:id/g18")
    _input_username=dict(by=AppiumBy.ID, value="com.tencent.wework:id/c1a")
    _input_phone=dict(by=AppiumBy.ID, value="com.tencent.wework:id/iaq")
    _save=dict(by=AppiumBy.ID, value="com.tencent.wework:id/b0b")
    _cancel=dict(by=AppiumBy.ID, value="com.tencent.wework:id/lf0")
    _manual=dict(by=AppiumBy.ID, value="com.tencent.wework:id/m5_")
    _back=dict(by=AppiumBy.ID, value="com.tencent.wework:id/lea")

    def 添加成员(self, name, phone) -> AdminPage:
        # 左下角添加成员
        self.click(**self._add_member)
        # 手动输入添加
        self.click(**self._manual)
        # 姓名
        self.send_keys(**self._input_username, text=name)
        # 电话
        self.send_keys(**self._input_phone, text=phone)
        # 保存
        self.click(**self._save)
        #利用implicity wait,直到出现手工添加按钮，但不操作
        self.driver.find_element(**self._manual)
        self.click(**self._back)
        # 没有点back按钮
        # self.back()
        return self
    def 添加子部门(self, name) -> AdminPage:
        ...

    def 修改部门名字(self, name) -> AdminPage:
        ...

    def 取消(self) -> ListPage:
        #管理页面右上角叉子
        self.click(**self._cancel)
        return ListPage(self.driver)
