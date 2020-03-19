# 我的课表
from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse
from .JWCookies import *
from spider import my_curriculum


resource_fields = {
    # 'cookies': fields.,

    'code':fields.Integer,
    'message':fields.String,
    'key':fields.String,
    'cookies':ONoDeal,

    'data':{
    'image':ONoDeal,
    'mes':fields.List(fields.String),
    'dir':fields.String,
    'usesname':fields.String
}
    # 'date_updated': fields.DateTime(dt_format='rfc822'),
}

class CurriculumDao(object):
    def __init__(self, mes='ok',code=200,cookies=None,image=[],dir=None,usesname=None,key=None,jwmes=''):

        self.message = mes
        self.code = code
        self.cookies=cookies
        self.key=key
        self.image=image
        self.dir=dir
        self.usesname=usesname
        self.mes=jwmes

class Curriculum(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('key', type = str, required = True,
                                    help = 'No args provided')
        self.reqparse.add_argument('openid', type=str)
        self.reqparse.add_argument('account', type=str, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('cookies', type=INoDeal, required=True,
                                   help='No args provided')
        # self.reqparse.add_argument('postdata', type=INoDeal, required=True,
        #                            help='No args provided')
        self.args = self.reqparse.parse_args()
    @marshal_with(resource_fields)
    def post(self):
        args = self.args
        key = args['key']
        openid = args['openid']
        account = args['account']
        jw_cookies = args['cookies']
        mycurriculum=my_curriculum(cookies_dict=jw_cookies,usesname=account)
        getmycurriculum=mycurriculum.get_curriculum()
        return CurriculumDao(cookies=getmycurriculum['cookies'],
                             image=getmycurriculum['fiename'],
                             jwmes=getmycurriculum['mes'],
                             dir=getmycurriculum['dir'],
                             usesname=getmycurriculum['usesname'])

