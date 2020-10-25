# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(__file__))
from codeocr import Codeocr
import base64

class Base():

    def __init__(self):

        self.academicUrl = '教务链接'# 例如：http://bkjw.sxu.edu.cn/
        # print(self.academicUrl)
        self.message=''
        self.Sel_XNXQ='20190'
        self.Sel_ZC='01'
        self.selxqs='2'
        # self.path='E:/龙城山大plus1.0.0/spider'/wEWAgKvk+gMApnB768G---/wEdAAJkNs91HJOZ0bENtcnXyXlVZ5IuKWa4Qm28BhxLxh2oFA==
        self.EVENT='/wEdAAJkNs91HJOZ0bENtcnXyXlVZ5IuKWa4Qm28BhxLxh2oFA=='
        #路径
        self.ChenjiPath='E:/龙城山大plus1.0.0/image/gd'
        self.KaochanPath='E:/龙城山大plus1.0.0/image/er'
        self.CurPath='E:/龙城山大plus1.0.0/image/cur'
    @classmethod
    def codeOcr(self,repcontext):
        codeOcr=Codeocr(repcontext)
        code=codeOcr.yzm_ocr()
        return code
    @classmethod
    def academicurl(self):
        return self().academicUrl

    @classmethod
    def event(self):
        return self().EVENT

    @classmethod
    def chenjipath(self):
        return self().ChenjiPath

    @classmethod
    def curpath(self):
        return self().CurPath
    @classmethod
    def kaochanpath(self):
        return self().KaochanPath


if __name__ == "__main__":
    pass

