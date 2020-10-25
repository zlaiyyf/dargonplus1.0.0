import requests
from base import Base
from bs4 import BeautifulSoup
import json
import time
from Model import *

#1.用户自定义异常类型，只要该类继承了Exception类即可，至于类的主题内容用户自定义，可参考官方异常类
class uererror(Exception):
    "this is user's Exception for check the length of name "
    def __init__(self):
        pass
        # self.leng = leng
    def __str__(self):
        print("账号密码错误")
# 获得验证码和cookies
def getcode():
    headers={
        "Host":"myportal.sxu.edu.cn",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
        "Accept":"image/webp,*/*",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding":"gzip, deflate",
        "Connection":"keep-alive",
        "Referer":"http://myportal.sxu.edu.cn/"
    }
    url=Base.academicurl()+'captchaGenerate.portal'
    img_rep=requests.get(url=url,headers=headers)
    yzm=Base.codeOcr(img_rep.content)
    # print(img_rep.content)
    cookies=img_rep.cookies
    return {'cookies':cookies,'yzm':yzm}
def verification():
    getcode_re = getcode()
    # 获取4个验证码字母
    while True:
        if getcode_re['yzm']:
            break
        else:
            getcode_re = getcode()
    url =  Base.academicurl()+'captchaValidate.portal'
    param={
        "captcha": getcode_re["yzm"],
        "what": "captcha",
        "value": getcode_re["yzm"],
        "sf_request_type": "ajax",
    }
    headers={
        "Host":"myportal.sxu.edu.cn",
        "User-Agent":"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding":"gzip, deflate",
        "Connection":"keep-alive",
        "Referer":"http://myportal.sxu.edu.cn/"
    }
    rep=requests.get(url=url,params=param,cookies=getcode_re["cookies"],headers=headers)
    return {'rep':rep.text,'cookies':getcode_re["cookies"]}
    # print(rep.text)
def login():
    verification_re=verification()
    while True:
        if verification_re['rep']:
            verification_re = verification()
            # print('xxx',verification_re)
        else:
            # print('xxxxx',verification_re)
            break
    url = Base.academicurl()+'userPasswordValidate.portal'
    headers={
        "Host": "myportal.sxu.edu.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "173",
        "Origin": "http://myportal.sxu.edu.cn",
        "Connection": "keep-alive",
        "Referer": "http://myportal.sxu.edu.cn/index.portal",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
    }
    data={
             "Login.Token1": "201702701159",
             "Login.Token2": "zl467548",
             "goto": "http: // myportal.sxu.edu.cn / loginSuccess.portal",
               "gotoOnFail": "http://myportal.sxu.edu.cn/loginFailure.portal",
    }
    rep=requests.post(url=url,data=data,headers=headers,cookies=verification_re['cookies'])
    if '用户不存在' in rep.text:
        raise uererror
    else:
        cookies_j = requests.utils.dict_from_cookiejar(verification_re['cookies'])
        cookies_i = requests.utils.dict_from_cookiejar(rep.cookies)
        cookies= requests.utils.cookiejar_from_dict(dict(cookies_j,**cookies_i), cookiejar=None, overwrite=True)

        return {'cookies':cookies}

    # print(rep.text)
def get_json():
    with open(Base.getpath()+"/record.json", 'r') as load_f:
        load_dict = json.load(load_f)
        return load_dict
def save_json(data_dict):
    now_time=time.strftime('%Y-%m-%d %M-%I-%S' , time.localtime())
    data_dict['time']=now_time
    with open(Base.getpath()+"/record.json", "w") as f:
        json.dump(data_dict, f)
        print("保存文件完成...")

def geteasy():
    login_re=login()
    cookies=login_re['cookies']
    url=Base.academicurl()+'index.portal'
    param={
        ".f": "f3758",
        ".pmn": "view",
        "groupid": "all",
        "action": "bulletinsMoreView",
        "search": "true",
        ".ia": "false",
        ".pen": "pe1713",
    }
    headers={
        "Host": "myportal.sxu.edu.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://myportal.sxu.edu.cn/index.portal",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
    }
    # print(cookies)
    # 请求两次才能到主页
    rep=requests.get(url=url,headers=headers,cookies=cookies)
    print(cookies)
    return {'cookies':cookies}


    # print(rep.text)
# 分类别获取
def easy_detail(cookies,sort,f):
    url = Base.academicurl() + 'detach.portal'
    param = {
        ".f": "f"+f,
        ".pmn": "view",
        "groupid": "all",
        "action": "bulletinsMoreView",
        "search": "true",
        ".ia": "false",
        ".pen": "pe"+sort,
    }
    headers = {
        "Host": "myportal.sxu.edu.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://myportal.sxu.edu.cn/index.portal",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
    }
    rep=requests.get(url=url,headers=headers,params=param,cookies=cookies)
    soup_index=BeautifulSoup(rep.text,'lxml')
    tag_li_list = soup_index.find_all('li')
    easy_list=[]
    old_easy=get_json()
    index=-1
    new_first_bulletinId=old_easy[sort]
    # for tag_li in tag_li_list[::-1]:
    for tag_li in tag_li_list[::-1]:
        if "item-readed" in tag_li.get('class'):
            continue
            # print("读过了")
        tag_a=tag_li.find_all('a')[1]
        title=tag_a.get_text()
        tag_span=tag_li.find('span',attrs={'style':"float:left;"})
        time_=tag_span.get_text().strip()
        href=tag_a['href']
        bulletinId=href.split('&')[-1].split('=')[1]
        #
        # if "item-readed" in tag_li.get('class'):
        #     print("读过了")
        #     print(title)
        index += 1
        if index == 0:
            new_first_bulletinId = bulletinId
        if old_easy[sort]==bulletinId:
            old_easy[sort] = new_first_bulletinId
            save_json(old_easy)
            break
        else:
            easy_list.append({
                'title':title,
                'href':href,
                'bulletinId':bulletinId,
                 'time':time_
            })
        # print(bulletinId)
    # easy=easy_list[0]
    for easy in easy_list:
        easy_url=Base.academicurl()+'detach.portal?'+easy['href']
        easy_rep=requests.get(url=easy_url,headers=headers,cookies=cookies)
        # bulletin-contentpe1735
        soup_easy = BeautifulSoup(easy_rep.text,'lxml')
        # print(soup_easy)
        tag_content=soup_easy.find('div',attrs={'id':'bulletin-contentpe'+sort})
        esay_content = tag_content.get_text()
        tag_title = soup_easy.find('div',attrs={'class':'bulletin-title'})
        # tag_note = soup_easy.find_all('div',attrs={'class':'bulletin-info"'})[1]
        bulletinId=easy['bulletinId']
        new_user = eval('Essay'+sort)(essayid=bulletinId,
                             title=tag_title.get_text().strip(),
                             content=esay_content.strip(),time=easy['time'])

        # 添加到session:
        Session.add(new_user)
        # 提交即保存到数据库:
        Session.commit()
        # 关闭session:
        Session.close()
        print(tag_title.get_text().strip())
        # huoqu old_first new_first
        # print(esay_content)
def start():
    """
    两办：1713 3756
    其他：1734 3757
    本科:1735 3758
    研究生：1736 3759
    科技:1754 3761
    社科：1737 3760
    :return:
    """
    cookies=geteasy()['cookies']
    sort_list=[{'sort':'1713','f':'3756'},{'sort':'1734','f':'3757'},{'sort':'1735','f':'3758'},
               {'sort':'1736','f':'3759'},{'sort':'1754','f':'3761'},{'sort':'1737','f':'3760'}]
    for sort in sort_list:
        easy_detail(cookies=cookies,sort=sort['sort'],f=sort['f'])

if __name__ == "__main__":
    # save_json({'1713':'',
    #            '1734':'',
    #            '1735':'',
    #            '1736':'',
    #            '1754':'',
    #            '1737':''})
    start()
    # _list=[1,2,3]
    # for i in _list[::-1]:
    #     print(i)