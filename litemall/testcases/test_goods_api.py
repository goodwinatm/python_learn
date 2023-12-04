import jsonpath
import pytest

from litemall.api.goods_api import Goods_API
from litemall.utils.schema_utils import Schema_utils


class TestGoodsAPI:
    def setup_class(self):
        self.goods_api=Goods_API()

    @pytest.mark.parametrize("goods_name", ["yangu_612"])
    def test_create(self,goods_name):
        goods_data = {"goods": {"picUrl": "", "gallery": [],
                                "isHot": True,
                                "isNew": True,
                                "isOnSale": True,
                                "goodsSn": "12491264512421",
                                "name": f"{goods_name}",
                                "counterPrice": "8888"},
                      "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
                      "products": [{"id": 0, "specifications": ["标准"], "price": 0, "number": 0, "url": ""}],
                      "attributes": [{"attribute": "材质", "value": "纯棉"}]}
        create_r = self.goods_api.create(goods_data)
        list_r = self.goods_api.list(goods_name)
        delete_id = jsonpath.jsonpath(list_r, "$..id")[0]
        list_goods_name = jsonpath.jsonpath(list_r, "$..name")[0]
        self.goods_api.delete(delete_id)
        assert create_r["errmsg"] == "成功"
        assert list_goods_name == goods_name
    def test_list(self):
        r=self.goods_api.list("yangu_613")
        assert r["errmsg"]=="成功"
        assert Schema_utils.schema_validate_by_file(r, "schema.json")

    def test_delete(self):
        assert False
