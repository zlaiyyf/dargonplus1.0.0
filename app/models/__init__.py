
from app.extensions import db


from .StudyRoom import StudyRoom
from .Users import Users



#
# from .users import User
# from .formid import Formid
# from .accesstoken import Accesstoken
# from .expiredformid import Expiredformid
# from .teacher import  Teacher
# from .classmessage import Classmessage
#
#
#



# from .post import Post









# #定义多对多的第三张表
# #收藏
# collections = \
#     db.Table('collections',
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id'),primary_key=True),
#     db.Column('posts_id', db.Integer, db.ForeignKey('posts.id'),primary_key=True)
# )



