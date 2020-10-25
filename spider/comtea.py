from base import Base
import requests

from bs4 import BeautifulSoup


class comtea():
    def __init__(self, cookies_dict, usesname):
        self.jw_url = Base.academicurl()
        self.cookies = requests.utils.cookiejar_from_dict(cookies_dict)
        self.cookies_dict = cookies_dict
        self.usesname=usesname
    def get_comtea(self):
        """

        :return: {'status': False, 'mes': '', 'com_tea_list': [], 'usesname': '201702701159', 'cookies': {'ASP.NET_SessionId': 'asiukd2s131jnlohnlt53dvt', 'myCookie': '', 'name': 'value'}}

        """
        # http://bkjw.sxu.edu.cn/jxkp/Stu_wskp.aspx
        geturl = self.jw_url + '/jxkp/Stu_wskp.aspx'
        posturl=self.jw_url+'/jxkp/Stu_wskp_rpt.aspx'
        postheader = {
            'Host': 'bkjw.sxu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'image/webp,*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://bkjw.sxu.edu.cn/jxkp/Stu_wskp.aspx',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        pjsjheader = {
            'Host': 'bkjw.sxu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'image/webp,*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://bkjw.sxu.edu.cn/SYS/menu.aspx',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        pjsj = requests.get(url=geturl, headers=pjsjheader,cookies=self.cookies)
        soup = BeautifulSoup(pjsj.text, 'lxml')
        text_sj = soup.find_all('option')
        fhleibiao = []
        # 平时text_sj为no，评教过后卫0不能评教，评教期间可以

        if not text_sj:
            return {'status': False, 'mes': '', 'com_tea_list': fhleibiao, 'usesname': self.usesname,
                    'cookies': self.cookies_dict}
        # print(pjsj.text)
        # print(text_sj)
        # print(text_sj['value'])
        data = {
            # 'hid_2018101':'% CA % B1 % BC % E4 % C7 % F8 % B6 % CE % A3 % BA2019 - 06 - 06 + 00 % 3A00 - -2019 - 06 - 28 + 00 % 300',
            'sel_lc': text_sj[0]['value'],
            'records': ' ',
        }
        repkaosi = requests.post(url=posturl, headers=postheader, data=data,cookies=self.cookies)
        xxsoup = BeautifulSoup(repkaosi.text, 'lxml')


        # [{
        #     'course': '21100093|大数据综合应用课程设计别人吧而不是',
        #     'tea': '赵亮',
        #     'status': 0
        # },]
        # try:
        xx = xxsoup.find_all('tr')

        index=-1
        if len(xx) == 1:
            return {'status': False, 'mes': '', 'com_tea_list': fhleibiao, 'usesname': self.usesname,
                    'cookies': self.cookies_dict}
        for i in xx:
            # print(i)
            index += 1
            if index == 0:
                pass
            else:
                leibiao = {'course': '',
                'tea': '',
                'status': ''}
                td = i.find_all('td')
                leibiao['course']=td[1].get_text()
                leibiao['tea'] = td[2].get_text()
                if td[3].get_text()=='查看':
                    # 0wei
                    leibiao['status'] = 1
                else:
                    leibiao['status'] = 0
                fhleibiao.append(leibiao)
        return {'status':True,'mes':'','com_tea_list':fhleibiao,'usesname':self.usesname,'cookies':self.cookies_dict}
        # except:
    def post_com_tea(self):
        jw_url = self.jw_url
        post_url=jw_url+ '/jxkp/Stu_wskp_rpt.aspx'
        kaosiheader = {
            'Host': 'bkjw.sxu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'image/webp,*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://bkjw.sxu.edu.cn/jxkp/Stu_wskp.aspx',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        pjsjheader = {
            'Host': 'bkjw.sxu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'image/webp,*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://bkjw.sxu.edu.cn/SYS/menu.aspx',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        pjsj = requests.get(url=jw_url + '/jxkp/Stu_wskp.aspx', headers=pjsjheader,cookies=self.cookies)
        soup = BeautifulSoup(pjsj.text, 'lxml')
        text_sj = soup.find_all('option')
        if not text_sj:
            return {'status': False, 'mes': '', 'com_tea_list': [], 'usesname': self.usesname,
                    'cookies': self.cookies_dict}
        # print(text_sj)
        # print(text_sj['value'])
        data = {
            'sel_lc': text_sj[0]['value'],
            'records': ' ',
        }
        repkaosi = requests.post(url=post_url, headers=kaosiheader, data=data,cookies=self.cookies)
        xxsoup = BeautifulSoup(repkaosi.text, 'lxml')
        lj = []
        xx = xxsoup.find_all('tr')
        index=-1
        # weidao
        if len(xx) == 1:
            return {'status': False, 'mes': '', 'com_tea_list': [], 'usesname': self.usesname,
                    'cookies': self.cookies_dict}
        for i in xx:
            # 去除第一个
            index += 1
            leibiao = []
            # leibi
            # Stu_WSKP_pj.aspx?xnxq=20181&s=1&kcdm=600004&jsdm=0001426&kclx=01&lb=20&kclb=0&zj_flag=1&pjlc=2018101&skbj=600004-122
            # Stu_WSKP_pj.aspx?xnxq=20181&s=1&kcdm=600004&jsdm=0001426&kclx=01&lb=20&kclb=0&zj_flag=1&pjlc=2018101&skbj=600004-122
            if index==0:
                pass
            else:
                tag_td = i.find_all('td')
                if tag_td[3].a.string == '未评':
                    zf = tag_td[3].a['onclick']
                    lj.append(zf.split('\'')[1])

        weipj = 0
        for xlj in lj:
            pj12header = {
                'Host': 'bkjw.sxu.edu.cn',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }
            rep = requests.get(url=jw_url + '/jxkp/' + xlj, headers=pj12header,cookies=self.cookies)
            rep1 = BeautifulSoup(rep.text, 'lxml')
            # print(rep.text)
            value = rep1.find_all('input')
            if len(value) == 1:
                # print(rep1)
                weipj += 1
            else:
                bu_data = {}
                value1 = rep1.find_all('form')
                for jd in value1[0].children:
                    # print(value1[0].children)
                    # print(len(value1[0].children))
                    if jd.name == 'input':
                        # print(jd['name'])
                        if 'value' in jd.attrs:
                            bu_data[jd['name'].strip()] = jd['value'].strip()
                        else:

                            bu_data[jd['name']] = ''
                bu1 = {
                    'cj0': '9.50',
                    'sel_scorecj0': '',
                    'cj1': '9.50',
                    'sel_scorecj1': '',
                    'cj2': '9.50',
                    'sel_scorecj2': '',
                    'cj3': '9.50',
                    'sel_scorecj3': '',
                    'cj4': '9.50',
                    'sel_scorecj4': '',
                    'cj5': '9.50',
                    'sel_scorecj5': '',
                    'cj6': '9.50',
                    'sel_scorecj6': '',
                    'cj7': '9.50',
                    'sel_scorecj7': '',
                    'cj8': '9.50',
                    'sel_scorecj8': '',
                    'cj9': '9.50',
                    'sel_scorecj9': '',
                    'sel_yj': '',
                    'txt_count': '10',
                    'hidschoolcode': '10108',
                    'score': '9.50|9.50|9.50|9.50|9.50|9.50|9.50|9.50|9.50|9.50|',
                    'item': '144|145|150|151|152|153|154|155|156|157|',
                    'djdm': '01|01|01|01|01|01|01|01|01|01|',
                }
                datapj = {**bu_data, **bu1}

                pjssjheader = {
                    'Host': 'bkjw.sxu.edu.cn',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                    'Accept-Encoding': 'gzip, deflate',
                    'Referer': 'http://bkjw.sxu.edu.cn/jxkp/' + xlj,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Content-Length': '637',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Pragma': 'no-cache',
                    'Cache-Control': 'no-cache',
                }
                pj_rep = requests.post(
                    url=jw_url + '/jxkp/Stu_WSKP_pj.aspx?s=' + datapj['txts'] + '&id=' + datapj['txtuser'] + '&pjry=' +
                        datapj['txtlb'] +
                        '&xn=' + datapj['txtxn'] + '&xq=' + datapj['txtxq'] + '&js=' + datapj['txtjs'] + '&kclx=' +
                        datapj['txtkclx'] + '&kc=' + datapj['txtkc'] + '&lb=' + datapj['txtlb'] + '&kclb=' + datapj[
                            'txtkclb'] + '&tsave_flag='
                    , headers=pjssjheader, data=datapj,cookies=self.cookies)
        re_data=self.get_comtea()
        re_data['mes']=weipj
        return re_data

if __name__ == "__main__":
    # {'ASP.NET_SessionId': 'poogfwtrlnmhznfl2v30kuof', 'myCookie': '', 'name': 'value'}
    test=comtea(cookies_dict={'ASP.NET_SessionId': 'asiukd2s131jnlohnlt53dvt', 'myCookie': '', 'name': 'value'},usesname='201702701159')
    print(test.post_com_tea())
