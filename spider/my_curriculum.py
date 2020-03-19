

from base import Base
import requests
import os
import time
from bs4 import BeautifulSoup
import hashlib
import random

class my_curriculum():
    def __init__(self,cookies_dict,usesname):
        self.jw_url = Base.academicurl()
        self.path = Base.curpath()
        self.cookies = requests.utils.cookiejar_from_dict(cookies_dict)
        self.cookies_dict = cookies_dict
        self.time_path = time.strftime("%Y-%m-%d", time.gmtime())
        self.usesname = usesname
        self.dir_path = self.path + '/' + self.time_path + "/" + str(usesname)

        if os.path.isdir(self.dir_path):
            pass
        else:
            os.makedirs(self.dir_path)
    def get_curriculum(self):
        xq_dict=self.get_xq()
        xq_value=xq_dict['value']
        xq_name=xq_dict['name']
        postheader={
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
        # 'A','B','C','D','E','F','G','H','J','K','M','N','P','Q','R','S','T','W','X','Y','Z','abcdefhijkmnprstwxyz2345678
        rodom=''.join(random.sample(['A','B','C','D','E','F','G','H','J','K','M','N','P','Q','R','S','T','W','X','Y','Z',
                                     'z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'
                                     ], 15))
        m = hashlib.md5()
        m.update(('10108'+str(xq_value)+rodom).encode('utf-8'))
        hidsjyzm=m.hexdigest().upper()[:32]
        # print(hidsjyzm,rodom)
        imgheader = {
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
        rad0_data={
         'Sel_XNXQ':xq_value,
            'rad':"0",
            'px':"0",
            'txt_yzm':"",
            'hidyzm':xq_dict['yzm'],
            'hidsjyzm':hidsjyzm,
            'hidparam_xh':"",
         }
        post_rep=requests.post(url=self.jw_url+'/znpk/Pri_StuSel_rpt.aspx?m='+rodom,data=rad0_data,headers=postheader,cookies=self.cookies)
        rad0_soup=BeautifulSoup(post_rep.text, 'lxml')
        # print(post_rep.text)
        img_src=rad0_soup.find('img')['src']

        rad0_img=requests.get(self.jw_url+'/znpk/'+img_src,headers=imgheader,cookies=self.cookies)
        rad0file_name = str(int(time.time() * 10000000))
        tags_td = rad0_soup.find_all('td', {'align': 'left','width':'1060px'})
        mes = []
        for td in tags_td:
            mes.append(td.get_text())
        with open(self.dir_path + '/{}.png'.format(rad0file_name), 'wb') as f:
            f.write(rad0_img.content)


        rad0_data['rad']=1
        post_rep = requests.post(url=self.jw_url + '/znpk/Pri_StuSel_rpt.aspx?m=' + rodom, data=rad0_data,
                                 headers=postheader, cookies=self.cookies)
        rad0_soup = BeautifulSoup(post_rep.text, 'lxml')

        # print(post_rep.text)
        img_src = rad0_soup.find('img')['src']

        rad0_img = requests.get(self.jw_url + '/znpk/' + img_src, headers=imgheader, cookies=self.cookies)
        rad1file_name = str(int(time.time() * 10000000))
        with open(self.dir_path + '/{}.png'.format(rad1file_name), 'wb') as f:
            f.write(rad0_img.content)
        # print({'0':rad0file_name,'1':rad1file_name},mes)
        return {'status': True,
        'fiename': {'0':rad0file_name,'1':rad1file_name},
        'mes': mes,
        'dir': self.time_path,
        'usesname': self.usesname,
        'cookies': self.cookies_dict}

        # print(img_src)
    def get_xq(self):
        url = self.jw_url + '/znpk/Pri_StuSel.aspx'
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
        repkaosi = requests.get(url=url, headers=header, cookies=self.cookies)
        soup = BeautifulSoup(repkaosi.text, 'lxml')
        # print(soup)
        #                                             <option value='20190'>2019-2020学年第一学期</option>
        tag_select = soup.find('select', {'name': 'Sel_XNXQ'}).option
        tag_input = soup.find('input',{'name':"hidyzm"})

        headers = {
            'Host': 'bkjw.sxu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'image/webp,*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://bkjw.sxu.edu.cn/_data/login.aspx',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        # rep = requests.get(url=self.jw_url + '/sys/ValidateCode.aspx', headers=headers,cookies=self.cookies)
        # print(rep.text)
        return {
            'yzm':tag_input['value'],
            'value':tag_select['value'],
            'name':tag_select.get_text()
        }
        # print(tag)
        # # value = tag['value']
if __name__ == "__main__":
    test=my_curriculum(cookies_dict={'ASP.NET_SessionId': 'asiukd2s131jnlohnlt53dvt', 'myCookie': '', 'name': 'value'},usesname=201702701159)
    # print(test.get_xq())
    print(test.get_curriculum())
    print(  ''.join(random.sample(['A','B','C','D','E','F','G','H','J','K','M','N','P','Q','R','S','T','W','X','Y','Z',
                                     'z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'
                                     ], 15)))