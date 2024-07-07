# Created by Han Xu
# email:736946693@qq.com
import requests
import urllib.parse
import os
import re
import urllib.request
import urllib.error
from tqdm import tqdm




opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'),
                     ("referer", "https://www.pixiv.net/"),]
urllib.request.install_opener(opener)

class pixiv_spider():
    def __init__(self):
        """
        @:brief
        @:return
        """
        search_target_dic = {
            "1": "Rank",
            "2": "Keyword"
        }
        print(search_target_dic)
        self.searchTarget = ""
        while (True):
            self.searchTarget = input("Type in the target you want to search.\n")
            if (self.searchTarget in search_target_dic):
                break
            else:
                print("It seems that you have typed in a wrong answer.Please try again.")

        search_mode_dic = {
            "1": "Simple:Recommended and Fast because the downloaded images are vague.You can view the simple image and select what you love",
            "2": "Specific:Not Recommended and Slow because the downloaded images are clear"}
        print(search_mode_dic)
        self.searchMode = ""
        while (True):
            self.searchMode = input("Type in the requirement of download-mode.\n")
            if (self.searchMode in search_mode_dic):
                break
            else:
                print("It seems that you have typed in a wrong answer.Please try again.")

        self.path = input("type in the path where you want to reserve the images:\n")
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48',
            "referer": "https://www.pixiv.net/",
        }

        self.maximages = int(input("Type in the number of images you want:\n"))


        if (self.searchTarget == "1"):
            DateMode_dict = {"1": "daily", "2": "weekly", "3": "monthly", "4": "rookie", "5": "daily_ai", "6": "male",
                             "7": "female"}
            print(DateMode_dict)
            DateMode = ""
            while (True):
                DateMode_key = input("type in the searchMode you want\n")
                if (DateMode_key in DateMode_dict):
                    DateMode = DateMode_dict[DateMode_key]
                    break
                else:
                    print("It seems that you have typed in a wrong answer.Please try again.")

            self.paginator = int(self.maximages / 50) + 1
            self.date = input("Type in the date you want to search.Follow the format like this:20230423\n")
            self.url_front = "https://www.pixiv.net/ranking.php?mode={}&date={}&format=json&p=".format(DateMode,
                                                                                                       self.date)

        elif (self.searchTarget == "2"):
            heat_dic = {"0":"0","1": "500", "2": "1000", "3": "5000", "4": "10000", }
            print(heat_dic)
            heat_require = ""
            while (True):
                DateMode_key = input("Type in the requirement of heat.Larger the number is,Less the results are.\n")
                if (DateMode_key in heat_dic):
                    heat_require = heat_dic[DateMode_key]
                    break
                else:
                    print("It seems that you have typed in a wrong answer.Please try again.")

            self.url_front = "https://www.pixiv.net/ajax/search/artworks/"
            self.paginator = int(self.maximages / 60) + 1

            self.keyword = input("type in the keywords used to search in pixiv:\n")
            while(True):
                if (heat_require=="0"):
                    break
                else:
                    self.keyword = self.keyword + " " + heat_require + "users入り"
                    break

    def get_urls(self):
        """
        @:brief Get the URLs that you need to visit.
        @:return return a list of the URLs
        """
        urls = []
        if (self.searchTarget=="1"):
            for i in range(1, self.paginator + 1):
                urls.append(self.url_front + str(i))
            return urls
        elif(self.searchTarget=="2"):
            keyword = urllib.parse.quote(self.keyword)
            params = []
            for i in range(1, self.paginator + 1):
                params.append(
                    "{}?word={}&order=date_d&mode=all&p={}&s_mode=s_tag&type=all&lang=zh&version=c4032a21df2a82afb72b3fd753afb10a037befb5".format(
                        keyword,
                        keyword,
                        i))
            for i in params:
                urls.append(self.url_front + i)
        return urls

    def get_path(self):
        """
        @:brief Get the path where you want to reserve the images.
        @:return
        """
        dirname = os.getcwd() + "/" + self.path
        dirname_origin = dirname
        int_index = 0
        while (True):
            IsExist = os.path.exists(dirname)
            if (IsExist == False):
                os.mkdir(dirname)
                IsCreate = True
                break
            else:
                int_index += 1
                dirname = dirname_origin + "({})".format(int_index)

        return dirname + "/"

    def get_images_urls(self, urls):
        """
        @:brief Get the URLs of images.
        @:return a list of URLs of images
        """
        images_urls = []
        for each_url in urls:
            print("The url of keyword:{}".format(each_url))
            response = requests.get(each_url, headers=self.headers)
            if (response.status_code != 403) and (response.status_code != 404):
                url_txt = response.text
                pattern_string = "\"url\":\"https:[^\"]+jpg"
                image_list = re.findall(string=url_txt, pattern=re.compile(pattern_string))

                for i in image_list:
                    if i and len(images_urls) < self.maximages:
                        i = i[i.rfind("img"):i.rfind("_p0")]
                        i = i.replace("\\", "")
                        if (self.searchMode == "1"):
                            images_urls.append("https://i.pximg.net/img-master/" + i + "_p0_master1200.jpg")

                        elif (self.searchMode == "2"):
                            images_urls.append("https://i.pximg.net/img-original/" + i + "_p0.jpg")
            else:
                print("the invalid url:{}!".format(each_url))
                continue
        return images_urls

    def get_images(self, images_urls):
        """
        @:brief download the images into the path you set just
        @:return
        """
        m = 1
        for img_url in images_urls:
            image_path=""
            try:
                image_path = self.path + str(m) + img_url[img_url.rfind("."):]

                with tqdm(unit="B", unit_scale=True, unit_divisor=1024, miniters=1, mininterval=1,
                          desc=img_url.split("/")[-1]) as t:
                    urllib.request.urlretrieve(url=img_url, filename=image_path, reporthook=lambda a, b, c: t.update(b))

                print("\n第{}张图片的URL是:\n{}".format(m, img_url))
                print('**********第' + str(m) + '张图片下载完成********')
                print("保存于:\n{}".format(image_path))
                continue

            except urllib.error.HTTPError:
                if (img_url[-3:] == "jpg"):
                    stable_url_png = img_url[:-3] + "png"
                    del img_url
                    img_url = stable_url_png

                elif (img_url[-3:] == "png"):
                    stable_url_jpg = img_url[:-3] + "jpg"
                    del img_url
                    img_url = stable_url_jpg

                image_path = self.path + str(m) + img_url[img_url.rfind("."):]

                with tqdm(unit="B", unit_scale=True, unit_divisor=1024, miniters=1, mininterval=1,
                          desc=img_url.split("/")[-1]) as t:
                    urllib.request.urlretrieve(url=img_url, filename=image_path, reporthook=lambda a, b, c: t.update(b))

                print("\n第{}张图片的URL是:\n{}".format(m, img_url))
                print('**********第' + str(m) + '张图片下载完成********')
                print("保存于:\n{}".format(image_path))
                continue

            except BaseException as error:
                print(error)
                print("There are some problems with the url:{}".format(img_url))
                continue

            finally:
                m+=1

        print('下载完成!')
        return

    def __call__(self, *args, **kwargs):
        """
        @brief the constrcution of the class
        @:return
        """
        self.path = self.get_path()
        urls = self.get_urls()
        image_urls = self.get_images_urls(urls=urls)
        self.get_images(image_urls)
        return
