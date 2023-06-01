from datetime import datetime

import pytest

from homework5.wework_app.wework_page import WeworkPage


class TestWework:
    def setup_class(self):
        self.wework=WeworkPage()
        self.contact=self.wework.通讯录()
    def setup(self):
        ...
    # @pytest.mark.parametrize('name',['中文','english','_'])
    @pytest.mark.parametrize('name',['中文','english','_'])
    @pytest.mark.parametrize('phone',['130','133'])
    def test_add_member(self,name,phone):
        phone=phone+datetime.now().strftime('%d%H%M%S')
        assert name==self.contact.管理().\
            添加成员(name=name,phone=phone)\
            .取消().搜索(name).get_info()['name']
        self.contact.back()
        self.contact.back()
