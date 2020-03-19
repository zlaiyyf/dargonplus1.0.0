from flask_restful import Resource, fields, marshal_with

from flask_restful import reqparse
from .JWCookies import *

from spider import chenji


resource_fields = {
    # 'cookies': fields.,

    'code':fields.Integer,
    'message':fields.String,
    'key':fields.String,
    'cookies':ONoDeal,

    'data':{
    'image':ONoDeal,
    'dir':fields.String,
        'usesname':fields.String,
    'mes':ONoDeal
}
    # 'date_updated': fields.DateTime(dt_format='rfc822'),
}


class GradeDao(object):
    def __init__(self, mes='ok',code=200,cookies=None,image=[],dir=None,usesname=None,key=None,cj_mes=[]):

        self.message = mes
        self.code = code
        self.cookies=cookies
        self.key=key
        self.image=image
        self.dir=dir
        self.usesname=usesname
        self.mes=cj_mes


class Grade(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('key', type = str, required = True,
                                    help = 'No args provided')

        self.reqparse.add_argument('openid', type=str)

        self.reqparse.add_argument('account', type=str, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('cookies', type=INoDeal, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('postdata', type=INoDeal, required=True,
                                   help='No args provided')
        self.args = self.reqparse.parse_args()

    @marshal_with(resource_fields)
    def post(self):
        args = self.args
        key = args['key']
        openid=args['openid']
        account = args['account']
        postdata = args['postdata']

        # str.strip()
        jw_cookies = args['cookies']
        jw_chenji=chenji(cookies_dict=jw_cookies,usesname=account)
        jw_get_grade=jw_chenji.inquire_chenji(data=postdata)
        # print(jw_get_grade['status'])
        # print(jw_get_grade)
        if jw_get_grade['status']:

            return GradeDao(cookies=jw_get_grade['cookies'],
                            image=jw_get_grade['image'],
                            dir=jw_get_grade['dir'],
                            usesname=jw_get_grade['usesname'],
                            cj_mes=jw_get_grade['mes']
                            )
        else:
            return GradeDao(code=1112,mes='教务网出错')
