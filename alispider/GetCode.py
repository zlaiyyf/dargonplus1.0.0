import requests
from base import Base


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
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
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
             "Login.Token1": "201702701119",
             "Login.Token2": "701119",
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
def geteasy():
    login_re=login()
    cookies=login_re['cookies']
    url=Base.academicurl()+'detach.portal'
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
    print(cookies)
    rep=requests.get(url=url,headers=headers,params=param,cookies=cookies)
    rep=requests.get(url=url,headers=headers,params=param,cookies=cookies)
    print(rep.text)
if __name__ == "__main__":
    geteasy()