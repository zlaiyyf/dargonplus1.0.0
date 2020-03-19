from .V1 import api_db
from ..models import *

DEFAULT_BLUEPRINT = (

    (api_db ,'/v1'),

)

# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
