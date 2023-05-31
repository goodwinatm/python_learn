
import homework5
# from homework5.wework_app.contact.admin_page import AdminPage
from homework5.wework_app.contact.profile_page import ProfilePage


class ListPage:
    def 管理(self)->homework5.wework_app.contact.admin_page.AdminPage:
        ...
    def 搜索(self,keyword)->ProfilePage:
        ...
    def 浏览(self,name) -> ProfilePage:
        ...
