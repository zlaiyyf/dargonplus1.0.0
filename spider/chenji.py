
from base import Base
import requests
import os
import time
from bs4 import BeautifulSoup


class chenji():
    def __init__(self,cookies_dict,usesname):
        self.jw_url=Base.academicurl()
        self.path=Base.chenjipath()
        self.cookies = requests.utils.cookiejar_from_dict(cookies_dict)
        self.cookies_dict=cookies_dict
        self.time_path=time.strftime("%Y-%m-%d", time.gmtime())
        self.usesname=usesname
        self.dir_path=self.path+'/'+self.time_path+"/"+str(usesname)

        if os.path.isdir(self.dir_path):
            pass
        else:
            os.makedirs(self.dir_path)
    def inquire_chenji(self,data):
        """

        :param data:
        :return: {'status': True,
        'image': [{'name': '学年学期：2017-2018学年第一学期', 'url': '15809617943356736'}, {'name': '学年学期：2017-2018学年第二学期', 'url': '15809617947354834'}, {'name': '学年学期：2017-2018学年第二学期', 'url': '15809617949959082'}, {'name': '学年学期：2018-2019学年第一学期', 'url': '15809617956456624'}, {'name': '学年学期：2018-2019学年第二学期', 'url': '15809617958361456'}, {'name': '学年学期：2018-2019学年第二学期', 'url': '15809617966660946'}, {'name': '学年学期：2019-2020学年第一学期', 'url': '15809617968560646'}, {'name': '学年学期：2019-2020学年第一学期', 'url': '15809617975361802'}],
        'mes': [],
        'dir': '2020-02-06',
        'usesname': 201702701159,
        'cookies': {'ASP.NET_SessionId': 'w0fduve5245duifa5enbrnlo', 'myCookie': '', 'name': 'value'}}

        """
        dlheader = {
            'Host': 'bkjw.sxu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://bkjw.sxu.edu.cn/MAINFRM.aspx',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        picture_header = {
            'Host': 'bkjw.sxu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'image/webp,*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://bkjw.sxu.edu.cn/xscj/Stu_MyScore_rpt.aspx',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        post_data=data
        # print(post_data)
        dl = requests.post(self.jw_url+'/xscj/Stu_MyScore_rpt.aspx', headers=dlheader, data=post_data,cookies=self.cookies)
        soup = BeautifulSoup(dl.text, 'lxml')
        tags_table=soup.find_all('table')
        # print('----------')
        # print(dl.text)
        return_from={
        'status':False,
        'image': [],
        'mes': [],
        'dir':self.time_path,
        'usesname':self.usesname,
        'cookies':self.cookies_dict
      }
        if tags_table:
            return_from['status']=True
            score_list=[]
            for tag_table in tags_table:
                # jw_score_url =''
                if  tag_table.next_sibling:
                    if tag_table.next_sibling.name == 'div':
                        # print(i.string)
                        img_url = self.jw_url + '/xscj/' + tag_table.next_sibling.img['src']
                        picture_data = requests.get(url=img_url, headers=picture_header,cookies=self.cookies)
                        file_name=str(int(time.time()*10000000))
                        score_name = tag_table.get_text()
                        score_list.append({'name':score_name,'url':file_name})
                        with open(self.dir_path+'/{}.png'.format(file_name), 'wb') as f:
                            f.write(picture_data.content)
            return_from['image']=score_list
            tag_tablemain=soup.find('table',{'id':'tableReportMain'})
            # align=right
            if tag_tablemain:
                tag_td_list=tag_tablemain.find_all('td',{'align':'right'})
                for tag_td in tag_td_list:
                    return_from['mes'].append(tag_td.get_text())
            return return_from
        #     id=tableReportMain


        else:
            return return_from


        # theExportData text-align:center;width:873

        
        # pass






if __name__ == "__main__":
    data={ "SJ":"0",
"btn_search":"%BC%EC%CB%F7",
"SelXNXQ":"0",
"zfx_flag":"0",
"shownocomputjd":"1",
"zxf":"0",
"hidparam_xh":"",}
    test=chenji(cookies_dict={'ASP.NET_SessionId': 'ui0okyz14ds2mb5yfjv5grd2', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print(test.inquire_chenji(data=data))
    test=chenji(cookies_dict={'ASP.NET_SessionId': 'ui0okyz14ds2mb5yfjv5grd2', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print(test.inquire_chenji(data=data))
    test=chenji(cookies_dict={'ASP.NET_SessionId': 'ui0okyz14ds2mb5yfjv5grd2', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print(test.inquire_chenji(data=data))
    test=chenji(cookies_dict={'ASP.NET_SessionId': 'ui0okyz14ds2mb5yfjv5grd2', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print(test.inquire_chenji(data=data))
    test=chenji(cookies_dict={'ASP.NET_SessionId': 'ui0okyz14ds2mb5yfjv5grd2', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print(test.inquire_chenji(data=data))
    test=chenji(cookies_dict={'ASP.NET_SessionId': 'ui0okyz14ds2mb5yfjv5grd2', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print(test.inquire_chenji(data=data))
    test=chenji(cookies_dict={'ASP.NET_SessionId': 'ui0okyz14ds2mb5yfjv5grd2', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print(test.inquire_chenji(data=data))
    test=chenji(cookies_dict={'ASP.NET_SessionId': 'ui0okyz14ds2mb5yfjv5grd2', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print(test.inquire_chenji(data=data))
    test=chenji(cookies_dict={'ASP.NET_SessionId': 'ui0okyz14ds2mb5yfjv5grd2', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print(test.inquire_chenji(data=data))
    test=chenji(cookies_dict={'ASP.NET_SessionId': 'ui0okyz14ds2mb5yfjv5grd2', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print(test.inquire_chenji(data=data))
    test=chenji(cookies_dict={'ASP.NET_SessionId': 'ui0okyz14ds2mb5yfjv5grd2', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print(test.inquire_chenji(data=data))
    test=chenji(cookies_dict={'ASP.NET_SessionId': 'ui0okyz14ds2mb5yfjv5grd2', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print(test.inquire_chenji(data=data))
    test=chenji(cookies_dict={'ASP.NET_SessionId': 'ui0okyz14ds2mb5yfjv5grd2', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print(test.inquire_chenji(data=data))
    test=chenji(cookies_dict={'ASP.NET_SessionId': 'ui0okyz14ds2mb5yfjv5grd2', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print(test.inquire_chenji(data=data))

    # t=time.gmtime()
    # print(time.time())
    # print(os.path.isdir(time.strftime("%Y-%m-%d", t)))
    # print(time.strftime("%Y-%m-%d", t))
    # print([])

