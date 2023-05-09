# 创建conftest.py 文件 ，将下面内容添加进去，运行脚本
import pytest

from homework3.homework3.utils import LoadUtils


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name=i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid=i.nodeid.encode("utf-8").decode("unicode_escape")

# @pytest.fixture(params=LoadUtils.load_yaml("hp_data.yaml")["success"])
# def get_hero(request):
#     new_list = []
#     for i in request.params:
#          i = i + 1
#          new_list.append(i)
#     yield new_list
#     #yield request.param + 1
#     print("测试用例执行完成")
@pytest.fixture(params=LoadUtils.load_yaml("hp_data.yaml")["success"])
def get_hero(request):
    # new_list = []
    # for i in request.param:
    #     i = i + 1
    #     new_list.append(i)
    # yield new_list
    print("测试用例参数为： "+str(request.param+1))
    yield request.param+1
    print("测试用例执行完成")
