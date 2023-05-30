import os.path


def get_project_dir(sub_path):
    # __file__代表__init_.py,os.path.dirname代表这个文件的当前目录
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),sub_path)
