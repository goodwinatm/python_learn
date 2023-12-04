import jsonpath
import requests

from litemall.utils.schema_utils import Schema_utils


class Test_litemall:
    def test_getToken(self):
        r=requests.post('https://litemall.hogwarts.ceshiren.com/admin/auth/login'
                        ,json={"username":"hogwarts","password":"test12345"})

        self.Token=jsonpath.jsonpath(r.json(),"$..token")
        print(self.Token)

    def setup_class(self):
        r = requests.post('https://litemall.hogwarts.ceshiren.com/admin/auth/login'
                          , json={"username": "hogwarts", "password": "test12345"})

        self.token = jsonpath.jsonpath(r.json(), "$..token")[0]
        self.headers={"X-Litemall-Admin-Token":self.token}
        self.good_name = "yangu_613"

    def test_create_good(self):

        body={
                "goods":{
                    "picUrl":"",
                    "gallery":[

                    ],
                    "isHot":True,
                    "isNew":True,
                    "isOnSale":True,
                    "goodsSn":"12491264512421",
                    "name":f"{self.good_name}",
                    "counterPrice":"8888"
                },
                "specifications":[
                    {
                        "specification":"规格",
                        "value":"标准",
                        "picUrl":""
                    }
                ],
                "products":[
                    {
                        "id":0,
                        "specifications":[
                            "标准"
                        ],
                        "price":0,
                        "number":0,
                        "url":""
                    }
                ],
                "attributes":[
                    {
                        "attribute":"材质",
                        "value":"纯棉"
                    }
                ]
            }

        r=requests.post("https://litemall.hogwarts.ceshiren.com/admin/goods/create"
                        ,json=body,headers=self.headers)
        print(r.json())
    def test_good_list(self):

        r = requests.get("https://litemall.hogwarts.ceshiren.com/admin/goods/list"
                          , params={"name":self.good_name}
                         , headers=self.headers)
        print(r.json())
        if jsonpath.jsonpath(r.json(),"$..total")[0]>=1:
            self.goodId=jsonpath.jsonpath(r.json(),"$..id")[0]
            print(self.goodId)
            good_name =jsonpath.jsonpath(r.json(),"$..name")[0]
            assert good_name == self.good_name
            assert True == Schema_utils.schema_validate_by_file(r.json(),"schema.json")


    def test_good_delete(self):
         r=requests.post("https://litemall.hogwarts.ceshiren.com/admin/goods/delete"
                         ,json={"id":1436672}
                         ,headers=self.headers)
