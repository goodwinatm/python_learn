#测试server的client 端
import requests


def test_get_json():
    r=requests.post("http://127.0.0.1:5000/user",json={"name":"yan"})
    print(r.text)
def test_get_json():
    r=requests.post("http://127.0.0.1:5000/user",data={"name":"gu"})
    print(r.text)