import allure
import pytest

from hw2.test_pytest2.hero_management import HeroManagement


# 实例化类 类名()


# 问题： 用例冗余， 成功的所有的用例步骤全部都是一样的，包括断言信息
#           不一样的地方，只有输入的数据信息。
# 解决方案： 如果测试步骤与断言全部一样，只有输入的数据不一样，就可以使用 《 参数化 》

# 装饰器语法： @pytest.mark.parametrize
# 装饰器，一定是写在函数定义的头上。
# 反例xxxxxxx
# @pytest.mark.parametrize
# def demo():
#     pass
# 反例xxxxxxx
# 参数1： 有几个形参， "形参1, 形参2, 形参3"，装饰器内定义了几个形参，
# 就需要在 pytest 测试方法内添加几个形参， 名称需要保持一致。
# 参数2：

@pytest.mark.parametrize("volume", [1, 2, 98, 99])
def test_create_hero_success(volume):
    """
    边界值以及等价类场景的测试用例
    """
    # print(f"英雄AD的血量为{volume}")
    hero_mangement = HeroManagement()
    hero_mangement.create_hero("jinx", volume, 20)
    res = hero_mangement.find_hero("jinx")
    assert res.get("name") == "jinx"
    assert res.get("volume") == volume

@pytest.mark.parametrize("name", ["erty","rtyuihghjk", "tyuighj", "tyuihgj"])
def test_create_hero_success_name_valid(name):
    """
    有效等价类场景的测试用例
    """

    hero_mangement = HeroManagement()
    hero_mangement.create_hero(name, 20, 20)
    res = hero_mangement.find_hero(name)
    assert res.get("name") == name


@pytest.mark.parametrize("name", [1,1.05,True,False],ids=["姓名为整数1","姓名为浮点数1.05","姓名为布尔型True","姓名为布尔型False"])
def test_create_hero_fail_name_valid(name):
    """
    无效等价类场景的测试用例
    """

    hero_mangement = HeroManagement()
    hero_mangement.create_hero(name, 20, 20)
    res = hero_mangement.find_hero(name)
    assert res == False
@pytest.mark.parametrize("volume", [0, 100], ids=["边界值为0", "边界值为100"])
def test_create_hero_fail(volume):
    """
    边界值以及等价类场景的测试用例
    """
    # print(f"英雄AD的血量为{volume}")
    hero_mangement = HeroManagement()
    hero_mangement.create_hero("jinx", volume, 20)
    res = hero_mangement.find_hero("jinx")
    assert res == False


@pytest.mark.parametrize("volume", ["00000", 20.2,False], ids=["无效类字符串为00000", "无效类浮点值为20.2","无效类布尔型False"])
def test_create_hero_fail_invalid(volume):
    """
    边界值以及等价类场景的测试用例
    """
    # print(f"英雄AD的血量为{volume}")
    hero_mangement = HeroManagement()
    hero_mangement.create_hero("jinx", volume, 20)
    res = hero_mangement.find_hero("jinx")
    assert res == False

@pytest.mark.parametrize("power", [1,2,3])
def test_create_hero_success_power(power):
    """
    边界值以及等价类场景的测试用例
    """
    # print(f"英雄AD的血量为{volume}")
    hero_mangement = HeroManagement()
    hero_mangement.create_hero("jinx", 20, power)
    res = hero_mangement.find_hero("jinx")
    assert res.get("power") == power

@pytest.mark.parametrize("power", [0,-1,3.0,"555",False],ids=["无效值0","无效-1","无效类浮点值为3.0","无效字符串","无效类布尔型False"])
def test_create_hero_fail_power(power):
    """
    边界值以及等价类场景的测试用例
    """
    # print(f"英雄AD的血量为{volume}")
    hero_mangement = HeroManagement()
    hero_mangement.create_hero("jinx", 20, power)
    res = hero_mangement.find_hero("jinx")
    assert res == False
# 多参数传参
# @pytest.mark.parametrize("name,volume", [("jinx", 0), ("ez", 100)])
# def test_create_hero_fail1(name, volume):
#     """
#     边界值以及等价类场景的测试用例
#     """
#     # print(f"英雄AD的血量为{volume}")
#     hero_mangement = HeroManagement()
#     hero_mangement.create_hero(name, volume, 20)
#     res = hero_mangement.find_hero(name)
#     assert res == False
#
# # 笛卡尔积， 使用两个装饰器分别传参
# @pytest.mark.parametrize("name", ["jinx", "ez"])
# @pytest.mark.parametrize("volume", [0, 100])
# @allure.title("创建英雄失败的场景")
# def test_create_hero_fail(name, volume):
#     """
#     边界值以及等价类场景的测试用例
#     """
#     # print(f"英雄AD的血量为{volume}")
#     hero_mangement = HeroManagement()
#     hero_mangement.create_hero(name, volume, 20)
#     res = hero_mangement.find_hero(name)
#     assert res == False
#
