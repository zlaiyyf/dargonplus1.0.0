# -*- coding: UTF-8 -*-
from app import create_app
from flask_script import Manager,Shell
import os
from flask_migrate import MigrateCommand
# 从环境变量中获取config_name
# config_name = os.environ.get('FLASK_CONFIG') or 'default'
from app.extensions import db
# 生成app
# app = create_app(config_name)
app = create_app('development')

manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)
if __name__ == '__main__':
    manager.run()