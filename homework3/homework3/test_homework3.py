import pytest
from homework2.test_pytest2.hero_management import HeroManagement
from homework3.homework3.utils import LoadUtils


class TestCreateHero:
    @pytest.mark.parametrize("volume", LoadUtils.load_yaml("hp_data.yaml")["success"])
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

    @pytest.mark.parametrize("volume", LoadUtils.load_yaml("hp_data.yaml")["fail"])
    def test_create_hero_volume_fail(self, volume):
        """
        边界值以及等价类场景的测试用例
        """
        # print(f"英雄AD的血量为{volume}")
        hero_mangement = HeroManagement()
        hero_mangement.create_hero("jinx", volume, 20)
        res = hero_mangement.find_hero("jinx")
        assert res == False