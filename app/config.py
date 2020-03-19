# _*_ coding: utf-8 _*_
import os


# 定义配置基类
class Config:
    # 秘钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'

    # 数据库公用配置
    # # 无警告
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # # 自动提交
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DEBUG = True
    TESTING = True
    EXPLAIN_TEMPLATE_LOADING=True#mysql+pymysql://root:root@localhost:3306/
    #SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://root:root@localhost:3306/xcx'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



    # 额外的初始化操作
    @staticmethod
    def init_app(app):
        pass


# 开发环境配置
class DevelopmentConfig(Config):
    # 秘钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'

    DEBUG = True
    TESTING = True
    EXPLAIN_TEMPLATE_LOADING = True  # mysql+pymysql://root:root@localhost:3306/
    # SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/dragon'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 测试环境配置
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:pzl123456@localhost/test-database'


# 生产环境
class ProductionConfig(Config):
    # 秘钥
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'

    TESTING = True
    EXPLAIN_TEMPLATE_LOADING = True  # mysql+pymysql://root:root@localhost:3306/
    # SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/xcx'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 额外的初始化操作
    @staticmethod
    def init_app(app):
        pass



# 生成一个字典，用来根据字符串找到对应的配置类。
config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}