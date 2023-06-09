"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import yaml


# 《python 内置装饰器》 静态方法 类方法 实例方法的区别。
class LoadUtils:

    # 如果此类中的数据，不需要被其他的方法使用，则可以利用类方法
    # 应用场景： 工具类。
    @classmethod
    def load_yaml(self, yaml_path):
        return yaml.safe_load(open(yaml_path,encoding="utf8"))

    # @staticmethod
    # def load_data():
    #     pass


if __name__ == '__main__':
#    print(__name__)
    print(LoadUtils.load_yaml("hp_data.yaml"))
