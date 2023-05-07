import pytest
from homework2.test_pytest2.hero_management import HeroManagement
from homework3.homework3.utils import LoadUtils


class TestCreateHero:
    @pytest.mark.parametrize("volume", LoadUtils.load_yaml("hp_data.yaml")["success"],ids=["边界值为1", "边界值为2","边界值为98", "边界值为99"])
    def test_create_hero_volume_success(self, volume):
        """
        边界值以及等价类场景的测试用例
        """
        # print(f"英雄AD的血量为{volume}")
        hero_mangement = HeroManagement()
        hero_mangement.create_hero("jinx", volume, 20)
        res = hero_mangement.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("volume") == volume

    @pytest.mark.parametrize("volume", LoadUtils.load_yaml("hp_data.yaml")["fail"],ids=["无效类字符串", "无效类布尔型","边界值为0", "边界值为100"])
    def test_create_hero_volume_fail(self, volume):
        """
        边界值以及等价类场景的测试用例
        """
        # print(f"英雄AD的血量为{volume}")
        hero_mangement = HeroManagement()
        hero_mangement.create_hero("jinx", volume, 20)
        res = hero_mangement.find_hero("jinx")
        assert res == False

    #原有需求发生变化，边界值都增加1（变为最大值100，最小值2）。如何在不改变原始测试数据情况下，还能依然完成对修改需求后的测试（使用fixture）。
    def test_create_hero_volume_success3(self, get_hero):
        """
        边界值以及等价类场景的测试用例
        """
        # print(f"英雄AD的血量为{volume}")
        hero_mangement = HeroManagement()
        hero_mangement.create_hero("jinx", get_hero, 20)
        res = hero_mangement.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("volume") == get_hero