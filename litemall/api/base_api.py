import jsonpath
import requests


class Base_API:
    def __init__(self):
        self.base_url="https://litemall.hogwarts.ceshiren.com/"
        r = requests.post(self.base_url+'admin/auth/login'
                          , json={"username": "hogwarts", "password": "test12345"})

        self.token = jsonpath.jsonpath(r.json(), "$..token")[0]
        self.headers = {"X-Litemall-Admin-Token": self.token}
    def send(self,method,url,**kwargs):
        print(f"接口的请求信息为{method} {url}")
        if kwargs.get("header"):
            kwargs["headers"].update(self.headers)
        else:
            kwargs["headers"]=self.headers
        r=requests.request(method,self.base_url+url,**kwargs)
        print(f"接口的响应信息为{r.text}")
        return r.json()