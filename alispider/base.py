# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(__file__))
from codeocr import Codeocr
import base64

class Base():

    def __init__(self):
        self.academicUrl = 'http://bkjwsxu.cn:34569/'
        # self.

    @classmethod
    def codeOcr(self,repcontext):
        codeOcr=Codeocr(repcontext)
        code=codeOcr.yzm_ocr()
        return code
    @classmethod
    def academicurl(self):
        return self().academicUrl

    @classmethod
    def getpath(self):
        return os.getcwd()


if __name__ == "__main__":


    print()
    # import requests
    # import re
    # headers={
    #     'Host': 'bkjwsxu.cn:34567',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    #     'Accept': 'image/webp,*/*',
    #     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Connection': 'keep-alive',
    #     'Referer': 'http://bkjwsxu.cn:34567/ZNPK/KBFB_DayJCSel.aspx',
    #     'Pragma': 'no-cache',
    #     'Cache-Control': 'no-cache',
    # }
    # rep=requests.get(url='http://bkjw.sxu.edu.cn/sys/ValidateCode.aspx?t=636',headers=headers)
    # print('网页二进制')
    # print(rep.content)
    # # pa=re.compile(".*b'(.*?)<!DOCTYPE html PUBLIC .*")
    # # a=pa.search(str(rep.content))
    # # print(a.group(1))
    # # ba=str.encode(a.group(1))
    # with open('1.png','wb') as f:
    #     f.write(rep.content)
    # with open("1.png", 'rb') as f:
    #     print('读取二进制')
    #     ba=f.read()
    #     print(ba)
    #     base64_data = base64.b64encode(ba)
    #     s = base64_data.decode()
    #     print('读取二进制base64编码')
    #     print('data:image/jpeg;base64,%s' % s)
    #     # print(s)
    #     # print(';;;;;;;;;;;;;;;;;;;;;;;;;;')
    #     # print('data:image/jpeg;base64,%s' % s)
    #
    # base64_data = base64.b64encode(rep.content)
    # s = base64_data.decode()
    # print('wyeb二进制base64编码')
    # print('data:image/jpeg;base64,%s' % s)


# E:\龙城山大plus1.0.0\image\cur\2020-03-04\201702701159\15832910417351108.png