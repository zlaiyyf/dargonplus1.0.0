from base import Base
import requests
from bs4 import BeautifulSoup
import base64

def get_img():
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
    rep = requests.get(url=jwurl + '/sys/ValidateCode.aspx?t=636', headers=headers)
    base64_data = base64.b64encode(rep.content)
    s = base64_data.decode()
    return {'cookies': requests.utils.dict_from_cookiejar(rep.cookies), 'image': 'data:image/jpeg;base64,%s' % s}

def get_curriculum(cookies_dict,data):
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    jwurl=Base.academicurl()

    url = jwurl + '/ZNPK/KBFB_DayJCSel_rpt.aspx'
    headers={
        'Host': 'bkjw.sxu.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '174',
        'Origin': 'http://bkjw.sxu.edu.cn',
        'Connection': 'keep-alive',
        'Referer': 'http://bkjw.sxu.edu.cn/ZNPK/KBFB_DayJCSel.aspx',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    rep=requests.post(url=url,headers=headers,cookies=cookies,data=data)
    soup=BeautifulSoup(rep.text,'lxml')
    curriculum_tag=soup.find_all('table')
    if curriculum_tag:
        curriculumList = []
        if len(curriculum_tag) == 2:
            # tr定位不对每8个td一行
            tr_tag_list = curriculum_tag[1].find_all('td')
            tr_Grouping_list = [tr_tag_list[i:i + 8] for i in range(0, len(tr_tag_list), 8)]
            del tr_Grouping_list[0]
            for tr_Grouping in tr_Grouping_list:
                curriculum_last = {
                    'num':'',
                    'course':'',
                    'classnum':'',
                    'peoplenum':'',
                    'teacher':'',
                    'session':'',
                    'location':'',
                    'classname':''
                }
                if len(curriculumList) != 0:
                    curriculum_last = curriculumList[-1]
                # if not tr_Grouping[0].text:
                # #     num为空
                #     pass
                #
                # curriculumList
                curriculum_dict = {
                    'num': tr_Grouping[0].text,
                    'course': tr_Grouping[1].text,
                    'classnum': tr_Grouping[2].text,
                    'peoplenum': tr_Grouping[3].text,
                    'teacher': tr_Grouping[4].text,
                    'session': tr_Grouping[5].text,
                    'location': tr_Grouping[6].text,
                    'classname': tr_Grouping[7].text

                }
                if not tr_Grouping[0].text:
                    curriculum_dict['num'] = curriculum_last['num']
                if not tr_Grouping[1].text:
                    curriculum_dict['course'] = curriculum_last['course']
                if not tr_Grouping[2].text:
                    curriculum_dict['classnum'] = curriculum_last['classnum']
                if not tr_Grouping[3].text:
                    curriculum_dict['peoplenum'] = curriculum_last['peoplenum']
                if not tr_Grouping[4].text:
                    curriculum_dict['teacher'] = curriculum_last['teacher']
                if not tr_Grouping[5].text:
                    curriculum_dict['session'] = curriculum_last['session']
                if not tr_Grouping[6].text:
                    curriculum_dict['location'] = curriculum_last['location']
                if not tr_Grouping[7].text:
                    curriculum_dict['classname'] = curriculum_last['classname']


                # pass
                curriculumList.append(curriculum_dict)
                # print(curriculum_dict)
            return {'status': True,
        'image': curriculumList,
        'mes': '',
        'cookies': cookies_dict}
        else:
            return {'status': True,
        'image': curriculumList,
        'mes': '',
        'cookies': cookies_dict}
    else:
        return {'status': False,
        'image': [],
        'mes': '验证码错误',
        'cookies': cookies}

if __name__ == "__main__":
    getimg=get_img()
    cookies=getimg['cookies']
    image=getimg['image']
    print(image)

    yzm=input('yzzm')
    postData = {
        "Sel_XNXQ": 20191,
        "Sel_ZC": "01",
        "selxqs": 3,
        "Sel_JC": "01",
        "Sel_XQ": "",
        "Sel_XZBJ2_XQ": "	",
        "Sel_XZBJ2_YX": "Nothing",
        "xzbj2_input_bjmc":"	",
        "Sel_XZBJ": "",
        "sel_bm": "Nothing",
        "Sel_JS": "",
        "sel_cddw": "",
        "Sel_KC": "",
        "rad": "3",
        "txt_yzm": ""
    }
    print(get_curriculum(cookies_dict=getimg['cookies'],data=postData))

