from flask_restful import Resource, fields, marshal_with

from flask_restful import reqparse
from .JWCookies import *

from ..V1 import Essay1713,Essay1734,Essay1735,Essay1736,Essay1754,Essay1737
from app.extensions import db

resource_fields = {
    # 'cookies': fields.,

    'code':fields.Integer,
    'message':fields.String,
    'key':fields.String,


    'data':{
    'essay_list':ONoDeal,
    'fin':fields.Boolean,
        'sort':fields.String,
        'next_num':fields.Integer

}
    # 'date_updated': fields.DateTime(dt_format='rfc822'),
}

class EssayDao(object):
    def __init__(self, mes='ok',code=200,sort=None,essay_list=[],key=None,fin=False,next_num=0):

        self.message = mes
        self.code = code
        self.key=key

        self.essay_list=essay_list
        self.fin=fin
        self.sort=sort
        self.next_num=next_num

class Essay(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('key', type = str, required = True,
                                    help = 'No args provided')

        self.reqparse.add_argument('openid', type=str)

        self.reqparse.add_argument('sort', type=str, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('page', type=int, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('num', type=int, required=True,
                                   help='No args provided')

        self.args = self.reqparse.parse_args()

    @marshal_with(resource_fields)
    def post(self):
        args = self.args
        key = args['key']
        openid=args['openid']
        sort = args['sort']
        page=args['page']
        # str.strip()
        num = args['num']
        num=10

        if sort=='1734':
            _paginate = (Essay1734.query.order_by(Essay1734.id.desc())).paginate(page=page, per_page=num)

        elif sort=='1713':
            _paginate = (Essay1713.query.order_by(Essay1713.id.desc())).paginate(page=page, per_page=num)

        elif sort=='1735':
            _paginate = (Essay1735.query.order_by(Essay1735.id.desc())).paginate(page=page, per_page=num)

        elif sort=='1736':
            _paginate = (Essay1736.query.order_by(Essay1736.id.desc())).paginate(page=page, per_page=num)

        elif sort =='1754':
            _paginate = (Essay1754.query.order_by(Essay1754.id.desc())).paginate(page=page, per_page=num)

        elif sort =='1737':
            _paginate = (Essay1737.query.order_by(Essay1737.id.desc())).paginate(page=page, per_page=num)

        else:
            return EssayDao(code=1161,mes='未知类型')
        # print(_paginate.items)
        page_list=[]
        for _paginate_item in _paginate.items:
            page_list.append({'essay_id':_paginate_item.id,'essay_ab_title':_paginate_item.title,'essay_time':_paginate_item.time})
        return EssayDao(essay_list=page_list,fin=_paginate.has_next ,sort=sort,next_num =_paginate.next_num)
        # jw_chenji=chenji(cookies_dict=jw_cookies,usesname=account)


resource_field1s = {
    # 'cookies': fields.,

    'code':fields.Integer,
    'message':fields.String,
    'key':fields.String,


    'data':{
    'title':fields.String,
    'content':fields.String,
    'sort':fields.String,
    'id':fields.Integer

}
    # 'date_updated': fields.DateTime(dt_format='rfc822'),
}

class DetailsDao(object):
    def __init__(self, mes='ok',code=200,sort=None,title=None,content=None,key=None,id=None):

        self.message = mes
        self.code = code
        self.key=key

        self.title=title
        self.content = content
        self.id=id
        self.sort=sort

class Details(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('key', type = str, required = True,
                                    help = 'No args provided')

        self.reqparse.add_argument('openid', type=str)

        self.reqparse.add_argument('sort', type=str, required=True,
                                   help='No args provided')
        self.reqparse.add_argument('id', type=int, required=True,
                                   help='No args provided')


        self.args = self.reqparse.parse_args()

    @marshal_with(resource_field1s)
    def post(self):
        args = self.args
        key = args['key']
        openid=args['openid']
        sort = args['sort']
        id=args['id']
        if sort=='1734':
            essay = Essay1734.query.get(id)

        elif sort=='1713':
            essay = Essay1713.query.get(id)


        elif sort=='1735':
            essay = Essay1735.query.get(id)


        elif sort=='1736':
            essay = Essay1736.query.get(id)


        elif sort =='1754':
            essay = Essay1754.query.get(id)


        elif sort =='1737':
            essay = Essay1737.query.get(id)


        else:
            return EssayDao(code=1171,mes='未知类型')
        if essay:
            return DetailsDao(title=essay.title,content=essay.content,id=id,sort=sort)
        else:
            return EssayDao(code=1172,mes='没有')

        # jw_chenji=chenji(cookies_dict=jw_cookies,usesname=account)
if __name__ == "__main__":
    pass
    # essay_list(sort='1713',lastid=-1)