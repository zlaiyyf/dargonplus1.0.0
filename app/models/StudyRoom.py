from app.extensions import db
from  datetime import datetime






class StudyRoom(db.Model):
    """
    自习室表
    """
    __tablename__ = 'studyroom'
    id = db.Column(db.Integer, primary_key=True)  #

    # 周次 星期数 节次 lou
    zc = db.Column(db.String(10), index=True, nullable=False,)
    xqs = db.Column(db.String(10), index=True,nullable=False)
    jc = db.Column(db.String(10), index=True,nullable=False)
    js = db.Column(db.String(10), index=True,nullable=False)
    # 内容
    studyroom = db.Column(db.Text, nullable=True)

    # 最近更新
    updata_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "js:{} studyroom:{}".format(self.js, self.studyroom)



