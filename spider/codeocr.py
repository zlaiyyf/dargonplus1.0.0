# -*- coding:utf-8 -*-
import re
from PIL import Image
import pytesseract
from io import BytesIO

class Codeocr():

# tesseract
    def __init__(self,path):

        self.img_path = path
        self.read_captcha()
        self.image_transfer()
        self.image_zaodian()

# 获取图片文件
    def yzm_ocr(self):
        text = pytesseract.image_to_string(self.chuli)
        self.f.close()
        # print(text)
        result = ''.join(re.findall(r'[A-Za-z0-9]', text))
        if len(result)==4:
            return result
        else:
            return []
    def read_captcha(self):
        f=BytesIO(self.img_path)
        image = Image.open(f)   # 打开图片
        file_name = self.img_path #获取文件名，此为图片标签
        self.image_arry=image
        self.f=f
    # 转换为灰度图像
    def image_transfer(self):
        """
        :param image_arry:图像list，每个元素为一副图像
        :return: image_clean:清理过后的图像list
        """

        image = self.image_arry
        image = image.convert('L') # 转换为灰度图像，即RGB通道从3变为1
        im2 = Image.new("L", image.size, 120)
        for y in range(image.size[1]): # 遍历所有像素，将灰度超过阈值的像素转变为255（白）
            for x in range(image.size[0]):
                pix = image.getpixel((x, y))
                if int(pix) >170:  # 灰度阈值
                    im2.putpixel((x, y), 255)
                else:
                    im2.putpixel((x, y), pix)
        self.image_clean=im2
    # 获取灰度转二值的映射table
    def get_bin_table(self,threshold=170):
        """
        获取灰度转二值的映射table
        :param threshold:
        :return:
        """
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        return table
    # 判断是否应该去除
    def sum_9_region(self,img, x, y):
        """
        9邻域框,以当前点为中心的田字框,黑点个数
        :param x:
        :param y:
        :return:
        """
        # todo 判断图片的长宽度下限
        cur_pixel = img.getpixel((x, y))  # 当前像素点的值
        width = img.width
        height = img.height

        if cur_pixel == 1:  # 如果当前点为白色区域,则不统计邻域值
            return 0

        if y == 0:  # 第一行
            if x == 0:  # 左上顶点,4邻域
                # 中心点旁边3个点
                sum = cur_pixel \
                      + img.getpixel((x, y + 1)) \
                      + img.getpixel((x + 1, y)) \
                      + img.getpixel((x + 1, y + 1))
                return 4 - sum
            elif x == width - 1:  # 右上顶点
                sum = cur_pixel \
                      + img.getpixel((x, y + 1)) \
                      + img.getpixel((x - 1, y)) \
                      + img.getpixel((x - 1, y + 1))

                return 4 - sum
            else:  # 最上非顶点,6邻域
                sum = img.getpixel((x - 1, y)) \
                      + img.getpixel((x - 1, y + 1)) \
                      + cur_pixel \
                      + img.getpixel((x, y + 1)) \
                      + img.getpixel((x + 1, y)) \
                      + img.getpixel((x + 1, y + 1))
                return 6 - sum
        elif y == height - 1:  # 最下面一行
            if x == 0:  # 左下顶点
                # 中心点旁边3个点
                sum = cur_pixel \
                      + img.getpixel((x + 1, y)) \
                      + img.getpixel((x + 1, y - 1)) \
                      + img.getpixel((x, y - 1))
                return 4 - sum
            elif x == width - 1:  # 右下顶点
                sum = cur_pixel \
                      + img.getpixel((x, y - 1)) \
                      + img.getpixel((x - 1, y)) \
                      + img.getpixel((x - 1, y - 1))

                return 4 - sum
            else:  # 最下非顶点,6邻域
                sum = cur_pixel \
                      + img.getpixel((x - 1, y)) \
                      + img.getpixel((x + 1, y)) \
                      + img.getpixel((x, y - 1)) \
                      + img.getpixel((x - 1, y - 1)) \
                      + img.getpixel((x + 1, y - 1))
                return 6 - sum
        else:  # y不在边界
            if x == 0:  # 左边非顶点
                sum = img.getpixel((x, y - 1)) \
                      + cur_pixel \
                      + img.getpixel((x, y + 1)) \
                      + img.getpixel((x + 1, y - 1)) \
                      + img.getpixel((x + 1, y)) \
                      + img.getpixel((x + 1, y + 1))

                return 6 - sum
            elif x == width - 1:  # 右边非顶点
                # print('%s,%s' % (x, y))
                sum = img.getpixel((x, y - 1)) \
                      + cur_pixel \
                      + img.getpixel((x, y + 1)) \
                      + img.getpixel((x - 1, y - 1)) \
                      + img.getpixel((x - 1, y)) \
                      + img.getpixel((x - 1, y + 1))

                return 6 - sum
            else:  # 具备9领域条件的
                sum = img.getpixel((x - 1, y - 1)) \
                      + img.getpixel((x - 1, y)) \
                      + img.getpixel((x - 1, y + 1)) \
                      + img.getpixel((x, y - 1)) \
                      + cur_pixel \
                      + img.getpixel((x, y + 1)) \
                      + img.getpixel((x + 1, y - 1)) \
                      + img.getpixel((x + 1, y)) \
                      + img.getpixel((x + 1, y + 1))
                return 9 - sum
    # 去除噪点
    def image_zaodian(self):

        i=self.image_clean
        width = i.width
        height = i.height
        table = self.get_bin_table()
        out = i.point(table, '1')
        N=1
        if N:
            for w in range(width):
                for h in range(height):
                    ys = i.getpixel((w,h))
                    sum=self.sum_9_region(out ,w,h)
                    if sum<=4:
                        out.putpixel((w, h), 1)
                    else:
                        out.putpixel((w, h), 0)
                    N-=1
            self.chuli=out




if __name__ == "__main__":
    import requests

    headers = {
        'Host': 'bkjwsxu.cn:34567',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept': 'image/webp,*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Referer': 'http://bkjwsxu.cn:34567/ZNPK/KBFB_DayJCSel.aspx',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    rep = requests.get(url='http://bkjwsxu.cn:34567/sys/ValidateCode.aspx?', headers=headers)
    image = Image.open(BytesIO(rep.content))
    image.save('1.png')
    codeOcr = Codeocr(rep.content)
    # print(codeOcr.yzm_ocr())