# 自习室
from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse
from spider import my_curriculum
from .JWCookies import *
from ..V1 import StudyRoom
from app.extensions import db

resource_fields = {
    # 'cookies': fields.,

    'code':fields.Integer,
    'message':fields.String,


    'data':{
    'room':ONoDeal,

}
    #
}

class CurriculumDao(object):
    def __init__(self, mes='ok',code=200,room=[]):

        self.message = mes
        self.code = code
        self.room=room

class _StudyRoom(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('key', type = str, required = True,
                                    help = 'No args provided')
        self.reqparse.add_argument('openid', type=str)
        self.reqparse.add_argument('zc', type=str, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('xqs', type=str, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('jc', type=str, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('js', type=str, required=True,
                                   help='No args provided')
        self.args = self.reqparse.parse_args()
    @marshal_with(resource_fields)
    def post(self):
        args = self.args
        key = args['key']
        openid = args['openid']
        zc=args['zc']
        xqs=args['xqs']
        jc=args['jc']
        js = args['js']
        studyroom=StudyRoom.query.filter_by(zc=zc,xqs=xqs,jc=jc,js=js).first()
        if studyroom:
            study_str=studyroom.studyroom
            # str.split()
            study_list=study_str.split('\n\n')
            # print(study_list)
            return CurriculumDao(room=study_list)
        return CurriculumDao(code=1151)
