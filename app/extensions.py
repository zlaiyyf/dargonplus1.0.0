
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(db=db)




# 初始化
def config_extensions(app):
    # bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    # Api.init_app(app)
    # mail.init_app(app)
    # # moment.init_app(app)
    # login_manager.init_app(app)
    # toolbar.init_app(app)
    # cache.init_app(app,config={'CACHE_TYPE':'redis'})

    # ckeditor.init_app(app)
    #一些图片上传的配置
    # configure_uploads(app,photos)
    #设置上传文件大小
    # patch_request_class(app,size=None)

    #指定登录的端点
    # login_manager.login_view = '404'
    #
    # #需要登录时的提示信息
    # login_manager.login_message = '需要先登录'
    # # 设置session保护级别
    # # None：禁用session保护
    # # 'basic'：基本的保护，默认选项
    # # 'strong'：最严格的保护，一旦用户登录信息改变，立即退出登录
    # login_manager.session_protection = 'strong'