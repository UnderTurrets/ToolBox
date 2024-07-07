'''
Created by Han Xu
email:736946693@qq.com
'''
import os
import re
import requests
from urllib.parse import urlparse

class normalizer:
    def __init__(self,current_dir):
        self.cur_dir=current_dir

    def __call__(self, *args, **kwargs):
        self.process(self.cur_dir)


    def process_markdown_file(self,current_dir, md_file_name):
        os.chdir(current_dir)

        # 图片素材文件夹
        filename_noExt=os.path.splitext(md_file_name)[0]
        img_dir = 'imgRes'+filename_noExt if len('imgRes'+filename_noExt)<=200 else 'imgRes'+filename_noExt[:200]

        # 创建目录
        if os.path.exists(img_dir)==False:
            os.makedirs(img_dir)

        with open(md_file_name, 'r', encoding='utf-8') as f:
            md_content = f.read()

        img_pattern = re.compile('!\[.*?\]\((http.*?)\)', re.IGNORECASE)
        img_matches = img_pattern.findall(md_content)

        for img_url in img_matches:
            img_name = os.path.basename(urlparse(img_url).path)
            img_path = os.path.join(img_dir, img_name)

            img_dir_safe = img_dir.replace(' ', '%20')

            response = requests.get(img_url)
            with open(img_path, 'wb') as img_file:
                img_file.write(response.content)

            md_content = md_content.replace(img_url, f'{img_dir_safe}/{img_name}')

        with open(md_file_name, 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f'处理完成：{md_file_name}')

    def process(self,directory):

        if os.path.isdir(directory)==True:
            os.chdir(directory)
            obj_list=os.listdir(directory)


            for obj in obj_list:

                if obj==".git":continue

                elif obj.endswith('.md')==True:
                    self.process_markdown_file(directory,obj)
                elif os.path.isdir(os.path.join(directory,obj))==True:
                    self.process(os.path.join(directory, obj))

        elif os.path.isdir(directory)==False and directory.endswith('.md'):
            path_name=os.path.dirname(directory)
            file_name = os.path.basename(directory)
            self.process_markdown_file(path_name,"")


if __name__ == '__main__':
    # replace the directory you want to rename
    target_directory = r"D:\Desktop\demo"
    normalizer(current_dir=target_directory)()

