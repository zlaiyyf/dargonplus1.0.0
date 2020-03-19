
from base import Base
import requests
import os
import time
from bs4 import BeautifulSoup

class kaochan():
    def __init__(self,cookies_dict,usesname):
        self.jw_url = Base.academicurl()
        self.path = Base.kaochanpath()
        self.cookies = requests.utils.cookiejar_from_dict(cookies_dict)
        self.cookies_dict = cookies_dict
        self.time_path = time.strftime("%Y-%m-%d", time.gmtime())
        self.usesname = usesname
        self.dir_path = self.path + '/' + self.time_path + "/" + str(usesname)

        if os.path.isdir(self.dir_path):
            pass
        else:
            os.makedirs(self.dir_path)



    def inquire_kaochan(self):
        """
        
        :return: {'status': True, 'filename': '15809803952744808', 'mes': '2019-2020学年第一学期', 'dir': '2020-02-06', 'usesname': 201702701159, 'cookies': {'ASP.NET_SessionId': 'da3crwq0xw2pqfzcghz5noup', 'myCookie': '', 'name': 'value'}}

        """
        jw_url=self.jw_url
        url=jw_url+'/KSSW/stu_ksap_rpt.aspx'
        header={
            'Host': 'bkjw.sxu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://bkjw.sxu.edu.cn//KSSW/stu_ksap.aspx',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '69',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        sel_xnxq=self.get_sel_xnxq()
        data={
            'sel_xnxq':sel_xnxq['value'],
            'sel_lcxz': '',
            'sel_lc': '',
            'btnsearch': '%BC%EC%CB%F7',
            'hidparam_xh': '',
        }
        repkaosi=requests.post(url=url,data=data,headers=header,cookies=self.cookies)
        soup=BeautifulSoup(repkaosi.text,'lxml')
        tag_img=soup.find('img')
        return_form={
            'status': False,
            'filename': '',
            'mes': '',
            'dir': self.time_path,
            'usesname': self.usesname,
            'cookies': self.cookies_dict
        }
        if tag_img:
            text_url = tag_img['src']#http://bkjw.sxu.edu.cn/
            text_url1= self.jw_url+'/KSSW/' + text_url
            kaosiheader = {
                'Host': 'bkjw.sxu.edu.cn',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                'Accept': 'image/webp,*/*',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'http://bkjw.sxu.edu.cn/KSSW/stu_ksap_rpt.aspx',
                'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
            }
            repkaosi1 = requests.get(url=text_url1, headers=kaosiheader,cookies=self.cookies)
            file_name = str(int(time.time() * 10000000))
            name = sel_xnxq['xq']
            return_form['status'] = True
            return_form['mes']=name
            return_form['filename']=file_name
            with open(self.dir_path + '/{}.png'.format(file_name), 'wb') as f:
                f.write(repkaosi1.content)
            return return_form

        else:
            return return_form

    def get_sel_xnxq(self):
        # http://bkjwsxu.cn:34567/KSSW/stu_ksap.aspx
        url = self.jw_url + '/KSSW/stu_ksap.aspx'
        header = {
            'Host': 'bkjw.sxu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://bkjw.sxu.edu.cn/SYS/menu.aspx',

            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }

        repkaosi = requests.get(url=url,headers=header, cookies=self.cookies)
        soup = BeautifulSoup(repkaosi.text, 'lxml')
        # print(soup)
        #                                             <option value='20190'>2019-2020学年第一学期</option>
        tag=soup.find('select',{'name':'sel_xnxq'}).find('option')
        # print(tag)
        value=tag['value']
        # return {
        #     'value': '20190',
        #     'xq': '2019-2020学年第一学期'
        # }

        return {
            'value':value,
            'xq':tag.get_text()
        }

if __name__ == "__main__":
#     data={'SJ':'0',
# 'btn_search':'%BC%EC%CB%F7',
# 'SelXNXQ':'0',
# 'zfx_flag':'0',
# 'shownocomputjd':'1',
# 'zxf':'0',
# 'hidparam_xh':'',}
    test=kaochan(cookies_dict={'ASP.NET_SessionId': 'da3crwq0xw2pqfzcghz5noup', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    print('ccc')
    print(test.inquire_kaochan())
    # t=time.gmtime()
    # print(time.time())
    # print(os.path.isdir(time.strftime("%Y-%m-%d", t)))
    # print(time.strftime("%Y-%m-%d", t))
    # print([])
