
# 蹭课

from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse
from .JWCookies import *
from spider import get_curriculum


resource_fields = {
    # 'cookies': fields.,

    'code':fields.Integer,
    'message':fields.String,
    'key':fields.String,
    'cookies':ONoDeal,

    'data':{
    'cur':ONoDeal,

}
    # 'date_updated': fields.DateTime(dt_format='rfc822'),
}

class OtherCurriculumDao(object):
    def __init__(self, mes='ok',code=200,cookies=None,cur=[],key=None):

        self.message = mes
        self.code = code
        self.cookies=cookies
        self.key=key
        self.cur=cur





class OtherCurriculum(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('key', type = str, required = True,
                                    help = 'No args provided')
        self.reqparse.add_argument('openid', type=str)


        self.reqparse.add_argument('cookies', type=INoDeal, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('postdata', type=INoDeal, required=True,
                                   help='No args provided')
        self.args = self.reqparse.parse_args()
    @marshal_with(resource_fields)
    def post(self):
        args = self.args
        cookies = args['cookies']
        postdata=args['postdata']
        cur=get_curriculum(cookies_dict=cookies,data=postdata)
        # print(cur)
        if cur['status']:
            return OtherCurriculumDao(cookies=cur['cookies'],cur=cur['image'])
        else:
            return OtherCurriculumDao(code=1141,mes='验证码错误',)