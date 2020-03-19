# 考场

from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse
from .JWCookies import *
from spider import kaochan



resource_fields = {
    # 'cookies': fields.,

    'code':fields.Integer,
    'message':fields.String,
    'key':fields.String,
    'cookies':ONoDeal,
    'data':{
    'image':fields.String,
    'dir':fields.String,
    'usesname':fields.String
    }
}


class ExamRoomDao(object):
    def __init__(self, mes='ok',code=200,cookies=None,image=[],dir=None,usesname=None,key=None,jwmes=''):

        self.message = mes
        self.code = code
        self.cookies=cookies
        self.key=key
        self.image=image
        self.dir=dir
        self.usesname=usesname

class ExamRoom(Resource):
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
        mycurriculum = kaochan(cookies_dict=jw_cookies, usesname=account)
        getmycurriculum = mycurriculum.inquire_kaochan()
        return ExamRoomDao(cookies=getmycurriculum['cookies'],
                           image=getmycurriculum['filename'],
                           dir=getmycurriculum['dir'],
                           usesname=getmycurriculum['usesname'])