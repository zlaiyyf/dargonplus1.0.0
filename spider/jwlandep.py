
import hashlib




def md5_encrypt(password,username,yzm):
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    password = m.hexdigest()#hexdigest为md5加密
    string = username + password.upper()[:30] + '10108'
    n = hashlib.md5()
    n.update(string.encode('utf-8'))
    encr = n.hexdigest().upper()[:30]
    c = hashlib.md5()
    c.update(yzm.encode('utf-8').upper())
    yzm=c.hexdigest()
    a=hashlib.md5()
    string1=yzm[:30].upper() + '10108'
    a.update(string1.encode('utf-8'))
    encr1=a.hexdigest().upper()[:30]
    return encr,encr1       #ener账号密码ener验证码

#mmjiaomi
def Expression(password):
    hu=0
    for i in password:
        if 48 <= ord(i) <= 57:
            huo = 8
        elif 97 <= ord(i) <= 122:
            huo = 4
        elif 65 <= ord(i) <= 90:
            huo = 2
        else:
            huo = 1
        hu |= huo
    return hu

#mmzh比较
def Inuserzh(username,password):
    if str(password).lower() in str(username).lower():
        return '1'
    else:
        return '0'

def Land_chuli(username,password,yzm):
    #md5
    md5=md5_encrypt(password=password,username=username,yzm=yzm)
    express=Expression(password=password)
    inuserzh=Inuserzh(username=username,password=password)
    return md5[0],md5[1],express,inuserzh,len(password)#账号密码,验证码,express,in