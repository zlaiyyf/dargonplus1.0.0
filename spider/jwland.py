import requests
import base64
from base import Base
from bs4 import BeautifulSoup
from jwlandep import Land_chuli

def jw_yzm():
    """
    获取验证码图片和cookies
    :return: {cookies，image}
    """
    jwurl=Base.academicurl()

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
    rep = requests.get(url=jwurl+'/sys/ValidateCode.aspx?t=636', headers=headers)
    base64_data = base64.b64encode(rep.content)
    s = base64_data.decode()
    return {'cookies':requests.utils.dict_from_cookiejar(rep.cookies),'image':'data:image/jpeg;base64,%s' % s}

def check_jwyzm(cookies_dict,username,password,yzm):
    """
    :param cookie:
    :param username:
    :param password:
    :param yzm:
    :return:
    """
    try:
        cookies=requests.utils.cookiejar_from_dict(cookies_dict)
        chuli = Land_chuli(username=username, password=password, yzm=yzm)
        jwurl=Base.academicurl()
        url = jwurl + '/_data/login.aspx'
        data = {
            '__VIEWSTATE': '/wEPDwUJNDU0MDQ0MDI5ZGQ=',
            '__EVENTVALIDATION': Base.event(),
            'pcInfo': 'Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64;+rv:66.0)+Gecko/20100101+Firefox/66.0Windows+NT+10.0;+Win64;+x645.0+(Windows)+SN:NULL',
            'typeName': '%D1%A7%C9%FA',
            'dsdsdsdsdxcxdfgfg': chuli[0],
            'fgfggfdgtyuuyyuuckjg': chuli[1],
            'Sel_Type': 'STU',
            'txt_asmcdefsddsd': username,
            'txt_pewerwedsdfsdff': '',
            'txt_sdertfgsadscxcadsads': '',
            'txt_mm_expression': chuli[2],
            'txt_mm_length': chuli[3],
            'txt_mm_userzh': chuli[4],
        }

        header = {
            'Host': 'bkjw.sxu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://bkjw.sxu.edu.cn/_data/login.aspx',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '526',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        response = requests.post(url=url, headers=header, data=data,cookies=cookies)

        soup = BeautifulSoup(response.text, 'lxml')
        # print(soup)
        # print(response.text)
        dlstatus = soup.find(id="divLogNote").get_text()
        if '稍候' in dlstatus:
            return {'status':True,'mes':dlstatus,'use':{'usename':username,'password':password},'cookies':cookies_dict}
        else:
            return  {'status':False,'mes':dlstatus,'use':{'usename':username,'password':password},'cookies':cookies_dict}
    except :
        cookies = requests.utils.cookiejar_from_dict(cookies_dict)
        chuli = Land_chuli(username=username, password=password, yzm=yzm)
        jwurl = Base.academicurl()
        url = jwurl + '/_data/login.aspx'
        data = {
            '__VIEWSTATE': '/wEPDwUJNDU0MDQ0MDI5ZGQ=',
            '__EVENTVALIDATION': '/wEWAgKvk+gMApnB768G',
            'pcInfo': 'Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64;+rv:66.0)+Gecko/20100101+Firefox/66.0Windows+NT+10.0;+Win64;+x645.0+(Windows)+SN:NULL',
            'typeName': '%D1%A7%C9%FA',
            'dsdsdsdsdxcxdfgfg': chuli[0],
            'fgfggfdgtyuuyyuuckjg': chuli[1],
            'Sel_Type': 'STU',
            'txt_asmcdefsddsd': username,
            'txt_pewerwedsdfsdff': '',
            'txt_sdertfgsadscxcadsads': '',
            'txt_mm_expression': chuli[2],
            'txt_mm_length': chuli[3],
            'txt_mm_userzh': chuli[4],
        }

        header = {
            'Host': 'bkjw.sxu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://bkjw.sxu.edu.cn/_data/login.aspx',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '526',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        response = requests.post(url=url, headers=header, data=data, cookies=cookies)

        soup = BeautifulSoup(response.text, 'lxml')
        # print(soup)
        # print(response.text)
        dlstatus = soup.find(id="divLogNote").get_text()
        if '稍候' in dlstatus:
            return {'status': True, 'mes': dlstatus, 'use': {'usename': username, 'password': password},
                    'cookies': cookies_dict}
        else:
            return {'status': False, 'mes': dlstatus, 'use': {'usename': username, 'password': password},
                    'cookies': cookies_dict}
if __name__ == "__main__":
    # print(requests.utils.dict_from_cookiejar(rep.cookies))

    # {'ASP.NET_SessionId': 'dc5r2i3jhj03ffkbdc4mgkpd', 'myCookie': '', 'name': 'value'}
    get_yzm=jw_yzm()
    print(get_yzm['image'])
    print(get_yzm['cookies'])
    yzm=input('请输入验证码')
    usename=input('请输入账号')
    password=input('请输入密码')
    jwland=check_jwyzm(cookies_dict=get_yzm['cookies'],yzm=yzm,username=usename,password=password)
    print(jwland)
