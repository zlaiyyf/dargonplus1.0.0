import requests
from bs4 import BeautifulSoup
import re


headers = {
'Host': 'bkjw.sxu.edu.cn',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'Referer': 'http://bkjw.sxu.edu.cn/ZNPK/KBFB_DayJCSel.aspx',
'Cookie': 'name=value; name=value; myCookie=; ASP.NET_SessionId=kbrm23hc3l2jyeqqpnbijch4',
'Upgrade-Insecure-Requests': '1',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
}
# rep=requests.get('http://bkjw.sxu.edu.cn/ZNPK/KBFB_DayJCSel.aspx',headers=headers)
# soup=BeautifulSoup(rep.content,'lxml')
# Sel_ZC=soup.find('select',{'name':"Sel_JS"})
# print(
#     Sel_ZC
# )
# op_list=Sel_ZC.find_all('option')
# print(op_list)
# zc_dict={'value':[],'key':[]}
# for op in op_list:
#     zc_dict['value'].append(op['value'])
#     zc_dict['key'].append(op.get_text())
#     # zc_dict[op['value']]=op.get_text()
# print(rep.cookies)
pata=re.compile(".*?innerHTML='(.*?)';</script>.*?")
rep1=requests.get('http://bkjw.sxu.edu.cn/ZNPK/Private/List_JXL.aspx?id=1',headers=headers)
print(rep1.text)
req=pata.search( rep1.text)
# print(req.group(1))
soup1=BeautifulSoup(req.group(1),'lxml')
op_list=soup1.find_all('option')
print(op_list)
zc_dict={'value':[],'key':[]}
for op in op_list:
    if 'value' in op.attrs:
        # print(op)
        zc_dict['value'].append(op['value'])
        zc_dict['key'].append(op.get_text())
    # zc_dict[op['value']]=op.get_text()
print(zc_dict)