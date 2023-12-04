import jsonpath
import requests

from litemall.api.base_api import Base_API


class Goods_API(Base_API):

    def create(self,goods_data):
        url = "admin/goods/create"
        # r = requests.post(url="admin/goods/create"
        #                   , json=goods_data)
        return self.send(url=url
                         , json=goods_data
                         , method="POST")
    def list(self,goods_name):
        # r = requests.get("https://litemall.hogwarts.ceshiren.com/admin/goods/list"
        #                  , params={"name": goods_name}
        #                  , headers=self.headers)
        url="admin/goods/list"
        return self.send(url=url
                     ,params={"name": goods_name}
                     ,method="GET")

    def delete(self,goods_id):
        url = "admin/goods/delete"
        # r = requests.post(url="admin/goods/delete"
        #                   , json={"id": goods_id})
        return self.send(url=url
                         , json={"id": goods_id}
                         , method="POST")
