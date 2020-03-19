# 教务网验证码，课表yzm
from flask_restful import Resource, fields, marshal_with

from flask_restful import reqparse
from .JWCookies import *

from spider import jw_yzm,get_img




resource_fields = {
    # 'cookies': fields.,
    'code':fields.Integer,
    'message':fields.String,
    'key':fields.String,
    'cookies':ONoDeal,
    'data':{
    'image':fields.String
}
    # 'date_updated': fields.DateTime(dt_format='rfc822'),
}



class CodeDao(object):
    def __init__(self, mes='ok',code=200,cookies=None,key=None,image=''):
        self.message = mes
        self.code = code
        self.key=key
        self.image=image
        self.cookies = cookies


class JwCode(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('key', type = str, required = True,
                                    help = 'No args provided')
        self.reqparse.add_argument('openid', type=str)
        self.args = self.reqparse.parse_args()

    @marshal_with(resource_fields)
    def get(self):
        args = self.args
        key = args['key']
        openid = args['openid']
        yzm = jw_yzm()
        return CodeDao(image=yzm['image'],cookies=yzm['cookies'])

    @marshal_with(resource_fields)
    def post(self):
        args = self.args
        key = args['key']
        openid = args['openid']
        yzm = jw_yzm()
        return CodeDao(image=yzm['image'],cookies=yzm['cookies'])
class CurCode(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('key', type = str, required = True,
                                    help = 'No args provided')
        self.reqparse.add_argument('openid', type=str)
        self.args = self.reqparse.parse_args()

    @marshal_with(resource_fields)
    def get(self):
        args = self.args
        key = args['key']
        openid = args['openid']
        yzm = get_img()
        return CodeDao(image=yzm['image'],cookies=yzm['cookies'])

    @marshal_with(resource_fields)
    def post(self):
        args = self.args
        key = args['key']
        openid = args['openid']
        yzm = get_img()
        return CodeDao(image=yzm['image'],cookies=yzm['cookies'])