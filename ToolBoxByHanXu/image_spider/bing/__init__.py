# Created by Han Xu
# email:736946693@qq.com
import requests
import urllib.request
import urllib.parse
import os
import re
from tqdm import tqdm

class Spider_bing_image():
    def __init__(self):
        """
        @:brief
        @:return
        """
        self.path=input("type in the path where you want to reserve the images:")
        self.url = 'https://www4.bing.com/images/async?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'}
        self.keyword = input("type in the keywords used to search in bing:")
        self.paginator = int(input("Type in the number of pages you want.Each page has almost 30 images:"))

    def get_urls(self):
        """
        @:brief Get the URLs that you need to visit.
        @:return return a list of the URLs
        """
        keyword = urllib.parse.quote(self.keyword)
        params = []
        for i in range(1, self.paginator + 1):
            params.append(
                "q={}&first={}&count=35&cw=1233&ch=946&relp=35&datsrc=I&layout=RowBased_Landscape&apc=0&mmasync=1&dgState=x*303_y*1355_h*185_c*1_i*36_r*8&IG=6A228D01DCE044E685557DE143D55D91&SFX=2&iid=images.5554".format(
                    keyword,30 * i))
        urls = []
        for i in params:
            urls.append(self.url + i)
        return urls


    def get_path(self):
        """
        @:brief Get the path where you want to reserve the images.
        @:return
        """
        dirname="./"+self.path
        dirname_origin = dirname
        int_index = 0
        while(True):
            IsExist = os.path.exists(dirname)
            if (IsExist==False):
                os.mkdir(dirname)
                IsCreate=True
                break
            else:
                int_index+=1
                dirname=dirname_origin+"({})".format(int_index)

        return dirname+"/"

    def get_image_url(self, urls):
        """
        @:brief Get the URLs of images.
        @:return a list of URLs of images
        """
        image_url = []
        pattern_string="http[^%&]+.jpg"
        pattern = re.compile(pattern=pattern_string)
        for url in urls:
            url_txt = requests.get(url, headers=self.headers).text
            url_list=pattern.findall(url_txt)
            for i in url_list:
                if i:
                    image_url.append(i)
        return image_url

    def get_image(self,image_url):
        """
        @:brief download the images into the path you set just
        @:return
        """
        m = 1
        for img_url in image_url:
            #定义一个flag用于判断下载图片是否异常
            flag=True
            try:
                #urlretrieve() 方法直接将远程数据下载到本地
                print("第{}张图片的URL是{}".format(m,img_url))
                print("保存于{}".format(os.getcwd()+self.path[1:]))

                image_path=self.path + str(m) + '.jpg'

                with tqdm(unit="B", unit_scale=True, unit_divisor=1024, miniters=1, mininterval=1,
                          desc=img_url.split("/")[-1]) as t:
                    urllib.request.urlretrieve(url=img_url, filename=image_path, reporthook=lambda a, b, c: t.update(b))

            except BaseException as error:
                    flag=False
                    print(error)
            if(flag):
                #下载完成提示
                print('**********第'+str(m)+'张图片下载完成********')
                #每下载完后一张,m累加一次
                m = m + 1
        print('下载完成!')
        return

    def __call__(self, *args, **kwargs):
        """
        @brief the constrcution of the class
        @:return
        """
        self.path=self.get_path()
        urls = self.get_urls()
        image_url = self.get_image_url(urls)
        self.get_image(image_url)
        return

if __name__ == "__main__":
    ex=Spider_bing_image()
    ex()
