from flask_restful import Resource, fields, marshal_with

from flask_restful import reqparse
import datetime
from spider.weather import getWeather




resource_fields = {
    # 'cookies': fields.,
    'code':fields.Integer,
    'message':fields.String,
    'key':fields.String,
    'cookies':fields.String,
    'data':{
    'xqs':fields.String,
        'zc':fields.String,
        'to':fields.String,
        'tor':fields.String
}
    # 'date_updated': fields.DateTime(dt_format='rfc822'),
}



class WeatherDao(object):
    def __init__(self, mes='ok',code=200,cookies=None,key=None,xqs=None,zc=None,to=None,tor=None):
        self.message = mes
        self.code = code
        self.key=key
        self.xqs=xqs
        self.zc=zc
        self.to=to
        self.tor=tor
        self.cookies = cookies


class Weather(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('key', type = str, required = True,
                                    help = 'No args provided')
        self.reqparse.add_argument('openid', type=str)
        self.args = self.reqparse.parse_args()


    @marshal_with(resource_fields)
    def post(self):
        args = self.args
        key = args['key']
        openid = args['openid']
        now_tul = datetime.datetime.now().isocalendar()
        start_tul = datetime.date(2020, 1, 24).isocalendar()
        zc = int(now_tul[1]) - int(start_tul[1])
        xqs = int(now_tul[2]) - 1
        weather = getWeather()
        return WeatherDao(zc=zc,xqs=xqs,to=weather[0],tor=weather[1])