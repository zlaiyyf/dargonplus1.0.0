from .base import Base
import requests
from bs4 import BeautifulSoup

class update(Base):


    def __init__(self):
        super().__init__()  # /ZNPK/KBFB_DayJCSel_rpt.aspx
        self.todayUrl = self.academicUrl + '/ZNPK/KBFB_DayJCSel_rpt.aspx'#/ZNPK/KBFB_DayJCSel.aspx


    def update(self):
        kbfbUrl=self.academicUrl+'/ZNPK/KBFB_DayJCSel.aspx'
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
        kbfbRes=requests.get(url=kbfbUrl,headers=headers)
        bkfbSoup=BeautifulSoup(kbfbRes.text,'lxml')

        zc_tag=bkfbSoup.find('select',{'name':"selxqs"})
        zc_op=zc_tag.find_all('option')
        zc_list=[]
        for zc in zc_op:
            zc_dict = {}
            zc_dict['id']=zc['value']
            zc_dict['name']=zc.get_text()
            zc_list.append(zc.get_text())
            # zc_dict[zc['value']]=
            # print(zc.get_text(),zc['value'])
        print(zc_list)
    def upclassmessage(self):
        import re
        kbfbUrl = self.academicUrl + '/ZNPK/Private/List_XZBJ.aspx?'
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
        xq_class={}
        for xq in range(1,3):
            print(xq)
            class_dict={}
            data = {
                'xnxq':'20190',
                'xzbj':'',
                'yx':'Nothing',
                'xq':xq,
            }
            kbfbRes = requests.get(url=kbfbUrl, headers=headers, params=data)
            patt = re.compile(".*?innerHTML='(.*?)';</script>.*")
            mes = re.search(patt, kbfbRes.text, )
            bkfbSoup = BeautifulSoup(mes.group(1), 'lxml')
            bkfb_tag=bkfbSoup.find_all('option')
            for bkfb in bkfb_tag:
                if  bkfb.get_text():
                    class_dict[bkfb['value']]=bkfb.get_text()
                    # print(bkfb)
            # print(class_dict)
            xq_class[str(xq)]=class_dict
        # print(xq_class)
        return xq_class