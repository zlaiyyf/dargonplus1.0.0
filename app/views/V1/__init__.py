from flask import Blueprint
from flask import Flask ,make_response,abort
from flask_restful import Api
import json

from app.models import *
from .Login import Login,WxLogin
from .Grade import Grade
from .Curriculum import Curriculum
from .ExamRoom import ExamRoom
from .ComTea import ComTea
from .VeCode import JwCode,CurCode
from  .StudRoom import _StudyRoom
from .OtherCurriculum import OtherCurriculum
from .Essay import Essay,Details
from .Weather import Weather
api_db= Blueprint(
                "api",
               __name__,

               )


api = Api(api_db,catch_all_404s=True)


@api_db.errorhandler(TypeError)
def handle_flask_error(error):
    print(error)
    # response 的 json 内容为自定义错误代码和错误信息
    # response ={
    #     'body': "A resource with that ID no longer exists.",
    #     'status': 410,
    #     'headers': "Any extra information you want.",
    # },
    data={
        'code':410,
        'message': "Type错误",
    }
    resp = make_response(json.dumps(data), 200)
    resp.headers.extend({'Content-Type':'application/json'})
    # response 返回 error 发生时定义的标准错误代码
    # response.status =500

    return resp
@api.representation('application/json')
def output_json(data, code, headers=None):
    if code !=200 :
        data.update(code=code)
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp



api.add_resource(Login, '/login')
api.add_resource(WxLogin,'/wxlogin')
api.add_resource(Grade, '/grade')
api.add_resource(Curriculum,'/cur')
api.add_resource(ExamRoom,'/examroom')
api.add_resource(ComTea,'/comtea')
api.add_resource(JwCode,'/jwcode')
api.add_resource(CurCode,'/curcode')
api.add_resource(OtherCurriculum,'/ocur')
api.add_resource(_StudyRoom,'/stu')
api.add_resource(Essay,'/essay')
api.add_resource(Details,'/tails')
api.add_resource(Weather,'/wea',)