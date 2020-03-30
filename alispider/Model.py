

from datetime import datetime
from sqlalchemy import Column, String, create_engine,Boolean,DateTime,Integer,Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
dbBase = declarative_base()

# 定义User对象:


# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:root@localhost:3306/dragon?charset=utf8',echo=False)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
Session = DBSession()


class Essay1734(dbBase):
    __tablename__ = 'essay1734'
    id = Column(Integer, primary_key=True)  #
    essayid=Column(String(128),  nullable=False,)
    # 内容題目
    title = Column(Text,  nullable=False,)
    content = Column(Text, nullable=False)
    note=Column(String(128), default=None)
    time=Column(String(32), default=None)

    # 最近更新
    updata_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "两办通知:{} 时间:{}".format(self.title, self.updata_time)
class Essay1713(dbBase):
    __tablename__ = 'essay1713'
    id = Column(Integer, primary_key=True)  #
    essayid=Column(String(128),  nullable=False,)
    # 内容題目
    title = Column(Text,  nullable=False,)
    content = Column(Text, nullable=False)
    note=Column(String(128), default=None)
    time=Column(String(32), default=None)

    # 最近更新
    updata_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "两办通知:{} 时间:{}".format(self.title, self.updata_time)
class Essay1735(dbBase):
    __tablename__ = 'essay1735'
    id = Column(Integer, primary_key=True)  #
    essayid=Column(String(128),  nullable=False,)
    # 内容題目
    title = Column(Text,  nullable=False,)
    content = Column(Text, nullable=False)
    note=Column(String(128), default=None)
    time=Column(String(32), default=None)

    # 最近更新
    updata_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "两办通知:{} 时间:{}".format(self.title, self.updata_time)
class Essay1736(dbBase):
    __tablename__ = 'essay1736'
    id = Column(Integer, primary_key=True)  #
    essayid=Column(String(128),  nullable=False,)
    # 内容題目
    title = Column(Text,  nullable=False,)
    content = Column(Text, nullable=False)
    note=Column(String(128), default=None)
    time=Column(String(32), default=None)

    # 最近更新
    updata_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "两办通知:{} 时间:{}".format(self.title, self.updata_time)
class Essay1754(dbBase):
    __tablename__ = 'essay1754'
    id = Column(Integer, primary_key=True)  #
    essayid=Column(String(128),  nullable=False,)
    # 内容題目
    title = Column(Text,  nullable=False,)
    content = Column(Text, nullable=False)
    note=Column(String(128), default=None)
    # 最近更新
    time=Column(String(32), default=None)

    updata_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "两办通知:{} 时间:{}".format(self.title, self.updata_time)
class Essay1737(dbBase):
    __tablename__ = 'essay1737'
    id = Column(Integer, primary_key=True)  #
    essayid=Column(String(128),  nullable=False,)
    # 内容題目
    title = Column(Text,  nullable=False,)
    content = Column(Text, nullable=False)
    note=Column(String(128), default=None)
    time=Column(String(32), default=None)

    # 最近更新
    updata_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "两办通知:{} 时间:{}".format(self.title, self.updata_time)

