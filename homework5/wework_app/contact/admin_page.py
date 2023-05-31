from __future__ import annotations
import homework5
from homework5.wework_app.contact.list_page import ListPage


class AdminPage:
    def 添加成员(self, name, phone) -> AdminPage:
        ...

    def 添加子部门(self, name) -> AdminPage:
        ...

    def 修改部门名字(self, name) -> AdminPage:
        ...

    def 取消(self) -> ListPage:
        ...
