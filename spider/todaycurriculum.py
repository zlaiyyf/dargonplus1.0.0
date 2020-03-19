from .base import Base
import requests
from bs4 import BeautifulSoup

class Todaycurriculum(Base):

    def __init__(self):

        super().__init__()#/ZNPK/KBFB_DayJCSel_rpt.aspx
        self.todayUrl = self.academicUrl+'/ZNPK/KBFB_DayJCSel_rpt.aspx'
        self.codeUrl=self.academicUrl+'/sys/ValidateCode.aspx'
        # print(self.academicUrl)
        # def work(self):
        #     pass
    def codeOcr(self,repcontext):
        return super().codeOcr(repcontext)

    def stuRemind(self,classnum,sel_zc,selxqs):
        codeHeaders={
            'Host': 'bkjw.sxu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept': 'image/webp,*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Referer': 'http://bkjw.sxu.edu.cn/ZNPK/KBFB_DayJCSel.aspx',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        while True:
            coderes=requests.get(url=self.codeUrl,headers=codeHeaders)
            code=self.codeOcr(coderes.content)
            # print(code)
            if code:
                headers = {
                    'Host': 'bkjw.sxu.edu.cn',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                    'Accept-Encoding': 'gzip, deflate',
                    'Referer': 'http://bkjw.sxu.edu.cn/ZNPK/KBFB_DayJCSel.aspx',
                    'Connection': 'keep-alive',
                    # 'Cookie': 'name=value; name=value; myCookie=; ASP.NET_SessionId=' + str(cookie),
                    'Upgrade-Insecure-Requests': '1',
                    'Pragma': 'no-cache',
                    'Cache-Control': 'no-cache',
                }
                postData = {
                    'Sel_XNXQ': self.Sel_XNXQ,
                    'Sel_ZC': sel_zc,
                    'selxqs': selxqs,
                    'Sel_JC':'',
                    'Sel_XQ': '',
                    'Sel_XZBJ2_XQ': '	',
                    'Sel_XZBJ2_YX': 'Nothing',
                    'xzbj2_input_bjmc': '	',
                    'Sel_XZBJ': classnum,
                    'sel_bm': 'Nothing',
                    'Sel_JS': '',
                    'sel_cddw': '',
                    'Sel_KC': '',
                    'rad': '3',
                    'txt_yzm': code,# 验证码
                }
                curriculumres=requests.post(
                    url=self.todayUrl,
                    data=postData,
                    headers=headers,
                    cookies=coderes.cookies
                )

                curriculumSoup=BeautifulSoup(curriculumres.text,'lxml')

                if '验证码错误' in curriculumSoup.text:

                    continue
                else:
                    curriculumList=[]
                    curriculum_tag=curriculumSoup.find_all('table')
                    if len(curriculum_tag)==2:
                        #tr定位不对每8个td一行
                        tr_tag_list=curriculum_tag[1].find_all('td')
                        tr_Grouping_list=[tr_tag_list[i:i+8] for i in range(0,len(tr_tag_list),8)]
                        del tr_Grouping_list[0]
                        for tr_Grouping in tr_Grouping_list:
                            curriculum_dict={
                                'num':tr_Grouping[0].text,
                                'course':tr_Grouping[1].text,
                                'classnum':tr_Grouping[2].text,
                                'peoplenum':tr_Grouping[3].text,
                                'teacher':tr_Grouping[4].text,
                                'session':tr_Grouping[5].text,
                                'location':tr_Grouping[6].text,
                                'classname':tr_Grouping[7].text

                            }
                            curriculumList.append(curriculum_dict)
                            # print(curriculum_dict)
                        return curriculumList
                    else:
                        return curriculumList

            else:
                continue
    def teaRemind(self):
        pass


if __name__ == "__main__":
    a=Todaycurriculum()
    b=a.stuRemind()
    print(b)