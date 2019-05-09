from django.apps import AppConfig
import os

# 修改App在后台的是显示内容
# default_app_config的值来源于apps.py的类名
default_app_config = 'index.IndexConfig'


# 获取当前的APP名
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


# 重写IndexConfig
class IndexConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '网站首页'
