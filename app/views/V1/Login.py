# 教务网登录和验证
from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse
from .JWCookies import *
from spider import check_jwyzm
import requests
resource_fields = {
    # 'cookies': fields.,
    'code':fields.Integer,
    'message':fields.String,
    'cookies':ONoDeal,
    'data':{
    'key':fields.String,
    'openid':fields.String
}
    # 'date_updated': fields.DateTime(dt_format='rfc822'),
}


class LoginDao(object):
    def __init__(self, mes='ok',code=200,cookies=None,openid=None,key=None):
        self.message = mes
        self.code = code
        self.cookies=cookies
        self.openid=openid
        self.key=key

class Login(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        self.reqparse.add_argument('account', type=str, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('password', type=str, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('yzm', type=str, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('cookies', type=INoDeal, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('openid', type=str, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('key', type=str,
                                   help='No args provided')
        self.args = self.reqparse.parse_args()
        # super(Login, self).__init__()
    @marshal_with(resource_fields)
    def post(self):
        args=self.args
        account=args['account']
        password=args['password']
        yzm=args['yzm']
        # print(yzm)
        print(account,password)

        key=args['key']
        openid=args['openid']
        jw_cookies=args['cookies']
        # print(jw_cookies)

        """
        这里应该用户注册
        """
        jw_status=check_jwyzm(cookies_dict=jw_cookies,username=account,password=password,yzm=yzm)
        # print(jw_status)
        if jw_status['status']:
            return LoginDao( cookies=jw_status['cookies'],openid=openid)
        elif '验证码' in jw_status['mes']:
            return LoginDao(code=1113, mes=jw_status['mes'])
        else:
            return LoginDao(code=1112,mes=jw_status['mes'])

def WX_Get_Openid(code):
    openUrl = 'https://api.weixin.qq.com/sns/jscode2session'
    data = {
        'appid': 'wx749ef52c6d11db56',
        'secret': '930e868e777208addf5310df70d43627',
        'js_code': code,
        'grant_type': 'authorization_code'
    }
    res = requests.get(url=openUrl, params=data, )

    rep_json = res.json()
    # print(rep_json)
    if 'errcode' not in rep_json:
        return rep_json
    else:
        return False

resource_fields1 = {
    # 'cookies': fields.,
    'code':fields.Integer,
    'message':fields.String,
    'key':fields.String,
    'openid':fields.String

}
class WxLoginDao(object):
    def __init__(self, mes='ok',code=200,key=None,openid=None):
        self.message = mes
        self.code = code
        self.openid=openid
        self.key=key

# 微信登录

class WxLogin(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        self.reqparse.add_argument('code', type=str, required=True,
                                   help='No args provided')

        self.args = self.reqparse.parse_args()


    @marshal_with(resource_fields1)
    def post(self):
        args = self.args
        code = args['code']
        print(code)
        get_openid=WX_Get_Openid(code)
        print(get_openid)
        if get_openid:
            return WxLoginDao(key=None,openid=get_openid['openid'])
        else:
            return WxLoginDao(code=1101,mes='获取code错误')



