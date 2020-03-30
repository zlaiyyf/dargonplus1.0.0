from app.extensions import db
from  datetime import datetime






class Essay1734(db.Model):
    """
    两办通知
    """
    __tablename__ = 'essay1734'
    id = db.Column(db.Integer, primary_key=True)  #

    essayid=db.Column(db.String(128),  nullable=False,)
    # 内容題目
    title = db.Column(db.Text,  nullable=False,)
    content = db.Column(db.Text, nullable=False)
    note=db.Column(db.String(128), default=None)
    time=db.Column(db.String(32), default=None)

    # 最近更新
    updata_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "两办通知:{} 时间:{}".format(self.title, self.updata_time)
class Essay1713(db.Model):
    __tablename__ = 'essay1713'
    id = db.Column(db.Integer, primary_key=True)  #
    essayid=db.Column(db.String(128),  nullable=False,)
    # 内容題目
    title = db.Column(db.Text,  nullable=False,)
    content = db.Column(db.Text, nullable=False)
    note=db.Column(db.String(128), default=None)
    time=db.Column(db.String(32), default=None)
    # 最近更新
    updata_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "两办通知:{} 时间:{}".format(self.title, self.updata_time)
class Essay1735(db.Model):
    __tablename__ = 'essay1735'
    id = db.Column(db.Integer, primary_key=True)  #
    essayid=db.Column(db.String(128),  nullable=False,)
    # 内容題目
    title =db. Column(db.Text,  nullable=False,)
    content = db.Column(db.Text, nullable=False)
    note=db.Column(db.String(128),default=None)
    time=db.Column(db.String(32), default=None)

    # 最近更新
    updata_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "两办通知:{} 时间:{}".format(self.title, self.updata_time)
class Essay1736(db.Model):
    __tablename__ = 'essay1736'
    id = db.Column(db.Integer, primary_key=True)  #
    essayid=db.Column(db.String(128),  nullable=False,)
    # 内容題目
    title = db.Column(db.Text,  nullable=False,)
    content = db.Column(db.Text, nullable=False)
    note=db.Column(db.String(128), default=None)
    time=db.Column(db.String(32), default=None)

    # 最近更新
    updata_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "两办通知:{} 时间:{}".format(self.title, self.updata_time)
class Essay1754(db.Model):
    __tablename__ = 'essay1754'
    id = db.Column(db.Integer, primary_key=True)  #
    essayid=db.Column(db.String(128),  nullable=False,)
    # 内容題目
    title = db.Column(db.Text,  nullable=False,)
    content = db.Column(db.Text, nullable=False)
    note=db.Column(db.String(128), default=None)
    time=db.Column(db.String(32), default=None)

    # 最近更新
    updata_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "两办通知:{} 时间:{}".format(self.title, self.updata_time)
class Essay1737(db.Model):
    __tablename__ = 'essay1737'
    id = db.Column(db.Integer, primary_key=True)  #
    essayid=db.Column(db.String(128),  nullable=False,)
    # 内容題目
    title =db. Column(db.Text,  nullable=False,)
    content = db.Column(db.Text, nullable=False)
    note=db.Column(db.String(128), default=None)
    time=db.Column(db.String(32), default=None)

    # 最近更新
    updata_time =db. Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "两办通知:{} 时间:{}".format(self.title, self.updata_time)