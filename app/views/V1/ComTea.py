# 评教
from flask_restful import Resource, fields, marshal_with

from flask_restful import reqparse
from .JWCookies import *

from spider import comtea

resource_fields = {
    # 'cookies': fields.,

    'code':fields.Integer,
    'message':fields.String,
    'key':fields.String,
    'cookies':ONoDeal,

    'data':{
    'tea':ONoDeal,
    'notea':fields.Integer,
    'usesname':fields.String
}
    # 'date_updated': fields.DateTime(dt_format='rfc822'),
}



class ComTeaDao(object):
    def __init__(self, mes='ok',code=200,tea=[],cookies=None,usesname=None,key=None,notea=0):

        self.message = mes
        self.code = code
        self.notea=notea
        self.cookies=cookies

        self.key=key
        self.tea=tea

        self.usesname=usesname



class ComTea(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('key', type = str, required = True,
                                    help = 'No args provided')

        self.reqparse.add_argument('openid', type=str)

        self.reqparse.add_argument('account', type=str, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('cookies', type=INoDeal, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('type', type=str, required=True,
                                   help='No args provided')
        self.args = self.reqparse.parse_args()
        args = self.args
        key = args['key']
        openid = args['openid']
        account = args['account']
        jw_cookies = args['cookies']
        self._type=args['type']#0查看1提交
        self.com_tea = comtea(cookies_dict=jw_cookies, usesname=account)

    @marshal_with(resource_fields)
    def post(self):

        if self._type=='1':
            com_tea_re = self.com_tea.post_com_tea()

            if com_tea_re['status']:
                    return ComTeaDao(tea=com_tea_re['com_tea_list'], cookies=com_tea_re['cookies'], notea=com_tea_re['mes'])
            return ComTeaDao(code=1131,mes='未到评教时间')
        else:
            com_tea_re = self.com_tea.get_comtea()
            if com_tea_re['status']:
                return ComTeaDao(tea=com_tea_re['com_tea_list'], cookies=com_tea_re['cookies'], notea=com_tea_re['mes'])
            return ComTeaDao(code=1131, mes='未到评教时间')


