from datetime import datetime
from sqlalchemy import Column, String, create_engine,Boolean,DateTime,Integer,Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random,requests
from base import Base as base
from bs4 import BeautifulSoup
import time
import re
# 创建对象的基类:
Base = declarative_base()

# 定义User对象:


# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:root@localhost:3306/test?charset=utf8',echo=False)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
Session = DBSession()


class StudyRoom(Base):
    __tablename__ = 'studyroom'
    id = Column(Integer, primary_key=True)  #

    # 周次 星期数 节次 lou
    zc = Column(String(10), index=True, nullable=False,)
    xqs = Column(String(10), index=True,nullable=False)
    jc = Column(String(10), index=True,nullable=False)
    js = Column(String(10), index=True,nullable=False)
    # 内容
    studyroom = Column(Text, nullable=True)

    # 最近更新
    updata_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "js:{} studyroom:{}".format(self.js, self.studyroom)

class zxs():
    def __init__(self,url,host):
        self.base_url=url
        self.host=host
        self.ks_url=self.base_url+'/ZNPK/KBFB_DayJCSel.aspx'
        self.qq_url=self.base_url+'/ZNPK/KBFB_DayJCSel_rpt.aspx'
        #
        # proxy_list = [
        #     {"http": "124.88.67.81:80"},
        #     {"http": "124.88.67.81:80"},
        #     {"http": "124.88.67.81:80"},
        #     {"http": "124.88.67.81:80"},
        #     {"http": "124.88.67.81:80"}
        # ]
        #
        # # 随机选择一个代理
        # proxy = random.choice(proxy_list)
        self.user_agent_list_2 = [

            # Firefox
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
            # Safari
            # chrome
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
            # 360
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",

            # 猎豹浏览器
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            # QQ浏览器
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            # sogou浏览器
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
            # maxthon浏览器
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
            # UC浏览器
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
        ]

        self.header={
            'Host': self.host,
            'User-Agent': random.choice(self.user_agent_list_2),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': '{}/ZNPK/KBFB_DayJCSel.aspx'.format( self.base_url),
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        self.qq_header = {
            'Host': self.host,
            'User-Agent': random.choice(self.user_agent_list_2),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': '{}/ZNPK/KBFB_DayJCSel.aspx'.format(self.base_url),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '171',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        pass

    def mkdir(self, path):
        # # 引入模块
        #
        # # 去除首位空格
        # path = path.strip()
        # # 去除尾部 \ 符号
        # path = path.rstrip("\\")
        #
        # # 判断路径是否存在
        # # 存在     True
        # # 不存在   False
        # isExists = os.path.exists(path)
        # print()
        # # 判断结果
        # if not isExists:
        #     os.makedirs(path)
        #     print('xxx')
        #     return True
        # else:
        #     # 如果目录存在则不创建，并提示目录已存在
            pass

    """
    启动
    """
    def start(self):
        """

        :return:
        """
        pass

    def save(self):
        """
        数据处理
        :return:
        """

    def land(self,data):
        """

        :param data:
        :return: 'cookies':ssion.cookies,'rep':post_rep.text,'yzm':yzm_text
        """
        self.header = {
            'Host': self.host,
            'User-Agent': random.choice(self.user_agent_list_2),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': '{}/ZNPK/KBFB_DayJCSel.aspx'.format(self.base_url),
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        self.qq_header = {
            'Host': self.host,
            'User-Agent': random.choice(self.user_agent_list_2),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': '{}/ZNPK/KBFB_DayJCSel.aspx'.format(self.base_url),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '171',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        # sesion=.get( url = self.ks_url,headers=self.header
        ssion=requests.session()
        rep=ssion.get(url = self.ks_url,headers=self.header)

        yzm_url = '{}/sys/ValidateCode.aspx'.format(self.base_url)
        yzm_hearder={
            'Host': self.host,
            'User-Agent':random.choice(self.user_agent_list_2),
            'Accept':'image/webp,*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': '{}/ZNPK/KBFB_DayJCSel.aspx'.format(self.base_url),
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        yzm_rep=ssion.get(yzm_url,headers=yzm_hearder)
        # print(yzm_rep.cookies)
        # # print(yzm_rep.text)
        # # with open(os.path.dirname(__file__)+'/wb.jpg','wb') as f:
        # #     f.write(yzm_rep.content)
        # # yzm=yzm_ocr(os.path.dirname(__file__)+'/wb.jpg')
        # yzm_text=yzm.yzm_ocr()
        yzm_text=base.codeOcr(yzm_rep.content)
        if yzm_text:
            data['txt_yzm']=yzm_text
            post_rep=ssion.post(url = self.qq_url,data=data,headers=self.qq_header)
            if '验证码错误'in post_rep.text:
                return self.land(data)
            else:
                a={'cookies':ssion.cookies,'rep':post_rep.text,'yzm':yzm_text}
                # print(type(a))
                # print('xxx')
                return  a

        else:
            return self.land(data)
        # repyzm = requests.get(url=yzm_url, headers=yzm_header, cookies=rep.cookies)

    def html_cl(self):

        """
           data={
            'Sel_XNXQ':'20190',
            'Sel_ZC':'01',
            'selxqs':'1',
            'Sel_JC': '03',
            'Sel_XQ': '1',
            'Sel_JXL': '101',
            'Sel_ROOM': '',
            'Sel_XZBJ2_XQ': '',
            'Sel_XZBJ2_YX': 'Nothing',
            'xzbj2_input_bjmc': '',
            'sel_bm': 'Nothing',
            'sel_cddw': '',
            'rad': '3',
            'txt_yzm': 'npwg',
         self.xnaq=xnaq             #学期字典{value，名称}
        self.zc=zc                 # 周次字典
        self.xqs=xqs               #星期字典
        self.xq=xq                 #校区字典
        self.lou=lou               #楼字典
        self.jsdict=jsdict         #教室字典
        self.lou_js=lou_js         #楼value教室字典
        self.xq_lou=xq_lou         #校区   楼
        }
        :return:
        """
        # print(self.xnaq)
        for xnaq_value in self.xnaq:
            xnaq_mc =self.xnaq[xnaq_value]#os.path.dirname(__file__)
            # self.mkdir(os.path.dirname(os.path.abspath(__file__)) + '/{}'.format(xnaq_mc))
            n=0
            print(xnaq_mc)
            for xq_value in self.xq_lou:
                xq_mc=self.xq[xq_value]#xq名称
                # print(xq_mc)
                # print(xq_mc)
                for lou_value in self.xq_lou[xq_value]:
                    lou_mc=self.lou[lou_value]
                    totle_js = self.lou_js[lou_value]
                    """
                    保存
                    """
                    # print(#os.path.dirname(__file__)
                    #     os.path.dirname(os.path.abspath(__file__)),'xxxxxxxxxx',
                    #
                    # )
                    # workbook = xlsxwriter.Workbook(os.path.dirname(os.path.abspath(__file__))+'/{}/{}.xlsx'.format(xnaq_mc,lou_mc))  # 新建excel表
                    # worksheet = workbook.add_worksheet('sheet1')  # 新建sheet（sheet的名称为"sheet1"）
                    headings = ['周次', '星期', '节次','自习室']  # 设置表头
                    row=1
                    # worksheet.write_row('A{}'.format(row), headings)
                    # print(xq_mc,lou_mc)
                    for zc_value in self.zc:
                        zc_mc = self.zc[zc_value]
                        for xqs_value in self.xqs:
                            xqs_mc= self.xqs[xqs_value]
                            for jc_value in self.jc:
                                jc_mc = self.jc[jc_value]
                                data = {
                                    'Sel_XNXQ': xnaq_value,
                                    'Sel_ZC': zc_value,
                                    'selxqs': xqs_value,
                                    'Sel_JC': jc_value,
                                    'Sel_XQ': xq_value,
                                    'Sel_JXL': lou_value,
                                    'Sel_ROOM': '',
                                    'Sel_XZBJ2_XQ': '',
                                    'Sel_XZBJ2_YX': 'Nothing',
                                    'xzbj2_input_bjmc': '',
                                    'sel_bm': 'Nothing',
                                    'sel_cddw': '',
                                    'rad': '3',
                                    # 'txt_yzm': 'npwg',
                                }
                                if n%10:
                                    n += 1
                                    data['txt_yzm']=yzm
                                    try:

                                        rep=requests.post(url=self.qq_url, data=data, headers=self.qq_header,cookies=cookies)
                                    except:
                                        print('遇到错误一已解决')
                                        time.sleep(10)
                                        rep=requests.post(url=self.qq_url, data=data, headers=self.qq_header,cookies=cookies)
                                        try:
                                            rep = requests.post(url=self.qq_url, data=data, headers=self.qq_header,
                                                                cookies=cookies)
                                        except:
                                            print('遇到错误二已解决')
                                            time.sleep(20)
                                            rep = requests.post(url=self.qq_url, data=data, headers=self.qq_header,
                                                                cookies=cookies)
                                            try:

                                                rep = requests.post(url=self.qq_url, data=data, headers=self.qq_header,
                                                                    cookies=cookies)
                                            except:
                                                print('遇到错误三已解决')
                                                time.sleep(60)
                                                rep = requests.post(url=self.qq_url, data=data, headers=self.qq_header,
                                                                    cookies=cookies)
                                    rep_html=rep.text
                                    if '验证码错误' in rep_html:
                                        try:
                                            land_dict = self.land(data)
                                        except:
                                            print('xzm')
                                            time.sleep(10)
                                            land_dict = self.land(data)
                                        # print(land_dict)
                                        yzm = land_dict['yzm']
                                        cookies = land_dict['cookies']
                                        rep_html = land_dict['rep']

                                else:
                                    # print('xx')
                                    try:
                                        land_dict = self.land(data)
                                    except:
                                        print('xzm')
                                        time.sleep(10)
                                        land_dict = self.land(data)
                                    # print(land_dict)
                                    yzm = land_dict['yzm']
                                    cookies = land_dict['cookies']
                                    rep_html = land_dict['rep']
                                    n += 1
                                    # print(yzm, cookies, rep_html)
                                soup=BeautifulSoup(rep_html,'lxml')
                                tr_tag_list=soup.find_all('td',{'width':'16%'})
                                # print(tr_tag)
                                tr_list=[]
                                for tr_tag in tr_tag_list:
                                    tr_list.append(tr_tag.get_text())
                                if '地点' in tr_list:
                                    tr_list.remove('地点')
                                zxs_list=list(set(totle_js).difference(set(tr_list)))
                                # row+=1
                                # worksheet.write_row('A{}'.format(row), [zc_mc,xqs_mc,jc_mc,'  '.join(zxs_list)])
                                # print(zxs_list)
                                # print(tr_list)
                                # print(self.qq_header['User-Agent'])
                                new_user = StudyRoom(zc=zc_value, xqs=xqs_value, jc=jc_value, js=lou_value,
                                                     studyroom='\n\n'.join(zxs_list))

                                # 添加到session:
                                Session.add(new_user)
                                # 提交即保存到数据库:
                                Session.commit()
                                # 关闭session:
                                Session.close()
                                print(xnaq_mc,lou_mc,zc_mc,xqs_mc,jc_mc,'  '.join(zxs_list))
                                # print(workbook.)
                    # print(workbook.)

        wc=input()

    def huoqu(self):

        """
        获取学校楼、教室等资源

        学年，周次，校区，楼，教室
        :return:
        """
        print("第一行为当前正在获取的内容，如果需要输入y不需要输入n。")
        print("正在获取学校信息")

        print("----------------------------------")
        xnaq = {}
        zc={}
        xqs={}
        xq={}
        lou={}
        jsdict={}
        lou_js={}
        xq_lou={}
        jc={}
        shuqu_se=requests.Session()
        # print(self.ks_url, self.header)
        rep=shuqu_se.get( url = self.ks_url,headers=self.header)

        soup=BeautifulSoup(rep.text,'lxml')
        sel_xnaq_tag=soup.find('select',{'name':"Sel_XNXQ"})
        index=1

        for xnaq_tag in sel_xnaq_tag.children:
            if index==1:
                print(xnaq_tag.get_text())

                xnaq[xnaq_tag.get('value')]=xnaq_tag.get_text()
            index+=1
        index = 0
        sel_zc_tag = soup.find('select', {'name':"Sel_ZC"})
        for zc_tag in sel_zc_tag.children:
            if index<=21:
                print(zc_tag.get_text())

                zc[zc_tag.get('value')] = zc_tag.get_text()
            index += 1
        selxqs_tag = soup.find('select', {'name': "selxqs"})
        for xqs_tag in selxqs_tag.find_all('option'):
            print(xqs_tag.get_text())

            xqs[ xqs_tag.get('value')] =  xqs_tag.get_text()
        index=0
        sel_xq_tag = soup.find('select', {'name': "Sel_XQ"})
        # print(sel_xnaq_tag.children)

        for xq_tag in sel_xq_tag.children:

            if xq_tag.get_text():
                if index<2:
                    xq[xq_tag.get('value')] = xq_tag.get_text()
                    index+=1
        jc_sel_tag = soup.find('select', {'name': "Sel_JC"})
        index=0
        for jc_tag in jc_sel_tag.find_all('option'):
            if index<=11:

            # print(xqs_tag)
            # print(jc_tag.get_text())
            # jc_xy = input('是否需要,是输入y，不需要输入n--')
            # if jc_xy == 'y':
                jc[jc_tag.get('value')] = jc_tag.string
            index+=1

        for xq_value in xq:
            # lou_l=[]
            lou_list_xq=[]
            get_lou_url='{}/ZNPK/Private/List_JXL.aspx?id={}'.format(self.base_url,xq_value)
            lou_rep=requests.get(url=get_lou_url,headers=self.header,cookies=rep.cookies)
            pattn=re.compile('.*?>(<.*>)</.*?')
            lou_list=re.findall(pattn, lou_rep.text)
            if lou_list:
                lou_soup=BeautifulSoup(lou_list[0],'lxml')
                lou_op_list=lou_soup.find_all('option')
                # print(lou_soup.find_all('option'))
                for lou_op in lou_op_list:
                    js = []
                    if '楼' in lou_op.get_text():
                        if lou_op.get('value'):
                            lou[lou_op.get('value')]=lou_op.get_text()
                            lou_list_xq.append(lou_op.get('value'))
                            js_url='{}/ZNPK/Private/List_ROOM.aspx?id={}'.format(self.base_url,lou_op.get('value'))
                            js_rep=requests.get(url=js_url,headers=self.header,cookies=rep.cookies)
                            # print(js_rep.text)
                            js_list = re.findall(pattn, js_rep.text)
                            # print(js_list)
                            if js_list:
                                js_soup = BeautifulSoup(js_list[0], 'lxml')
                                js_op_list = js_soup.find_all('option')
                                # print(lou_soup.find_all('option'))
                                for js_op in js_op_list:
                                    if js_op.get('value'):
                                        jsdict[js_op.get('value')] = js_op.get_text()
                                        js.append(js_op.get_text())
                            lou_js[lou_op.get('value')]=js
                xq_lou[xq_value]=lou_list_xq
        print('获取信息成功')
            # print(cs_soup.find_all('option'))
            # print(lou_rep.text)
        self.xnaq=xnaq
        # print(zc)#学期字典{value，名称}
        self.zc=zc                # 周次字典
        self.xqs=xqs               #星期字典
        self.xq=xq                #校区字典
        self.lou=lou               #楼字典
        self.jsdict=jsdict         #教室字典
        self.lou_js=lou_js         #楼value教室字典
        self.xq_lou=xq_lou        #校区   楼
        self.jc=jc                 #节次
        print( self.xnaq)
        print(self.zc)
        print(self.xqs)
        print( self.xq)
        print(self.lou)
        print(self.jsdict)
        print(self.lou_js)
        print(self.xq_lou)
        print(self.jc)

if __name__ == '__main__':

     Base.metadata.create_all(engine)
     jw_url = 'bkjw.sxu.edu.cn'
     #
     # # print('你的输入:{}'.format(jw_url))
     # # print('http://bkjw.sxu.edu.cn'.strip('//'))
     # # if jw_url=='bkjw.sxu.edu.cn':
     # #     print("该测试地址不可使用")
     # # else:
     a = zxs('http://' + jw_url, jw_url)
     a.huoqu()
     print()
     a.html_cl()
     # # new_user = User(name='20170211s111',password='ccasscaca',sign='46\n8',)
     # new_user = StudyRoom(zc='01',xqs='01',jc='01',js='2222',studyroom='我的无奈的绝望\ncsdcsdcscs\n成都市v测试')
     #
     # # 添加到session:
     # Session.add(new_user)
     # # 提交即保存到数据库:
     # Session.commit()
     # #关闭session:
     # Session.close()
     # # for instance in Session.query(wxuser).filter(wxuser.puid == 'f24d4532'):
     # #      print(instance.puid, )
     # use = Session.query(User).filter(User.name == '201702701159').first()
     #
     # print(use)