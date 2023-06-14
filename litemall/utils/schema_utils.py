import json

from genson import SchemaBuilder
from jsonschema.validators import validate


class Schema_utils:
    @classmethod
    def generate_jsonschema(cls,obj):
        # 实例化jsonschem
        builder = SchemaBuilder()
        # 传入被转换的对象
        builder.add_object(obj)
        # 转换成 schema 数据
        return builder.to_schema()
    @classmethod
    def generate_jsonschema_file(cls,file_path,obj):
        schema_obj=cls.generate_jsonschema(obj)
        with open(file_path,"w") as f:
            json.dump(schema_obj,f)
    @classmethod
    def schema_validate_by_file(cls,obj, file_path):
        '''
        对比 python 对象与生成的 JSONSchame 的结构是否一致
        '''
        schema = json.load(open(file_path))
        try:
            validate(instance=obj, schema=schema)
            return True
        except Exception as e:
            return False



if __name__=='__main__':
    data = {'errno': 0, 'data': {'total': 1, 'pages': 1, 'limit': 10, 'page': 1, 'list': [{'id': 1436722, 'goodsSn': '12491264512421', 'name': 'yangu_612', 'categoryId': 0, 'brandId': 0, 'gallery': [], 'keywords': '', 'brief': '', 'isOnSale': True, 'sortOrder': 100, 'picUrl': '', 'isNew': True, 'isHot': True, 'unit': '’件‘', 'counterPrice': 8888.0, 'retailPrice': 0.0, 'addTime': '2023-06-13 13:56:57', 'updateTime': '2023-06-13 13:56:57', 'deleted': False}]}, 'errmsg': '成功'}
    # print(Schema_utils.generate_jsonschema_file("schema.json",data))
    print(Schema_utils.schema_validate_by_file(data, "../schema.json"))
    