"""
Created by Han Xu
email:736946693@qq.com
"""
import os

class renamer:
    def __init__(self,current_dir):
        self.cur_dir=current_dir

    def __call__(self, new_name, target_type="*", order_key=None):
        self.rename_byType(new_name,target_type,order_key)

    def rename_byType(self, new_name, target_type="*", order_key=None):
        # 切换到指定目录
        os.chdir(self.cur_dir)

        # 获取目录下的所有文件
        files = os.listdir(self.cur_dir)
        # 跳过一些系统文件
        while (files.count(r"desktop.ini") != 0):
            files.remove(r"desktop.ini")
        # 排序
        files = sorted(files, key=order_key)

        index = 1
        # 遍历所有文件并重命名
        for file in files:

            if os.path.isdir(file) == False and file.rfind(".") != -1:

                # 获取文件后缀名
                file_type = file[file.rfind(".") + 1:]

                if target_type == "*" or target_type == file_type:
                    target_name = new_name + f"{index}." + file_type
                    os.rename(file, target_name)
                    print(f"{self.cur_dir}"
                          f"{file}-------->{target_name}", sep="\n")

                index = index + 1

        return


if __name__ == "__main__":
    ex=renamer(r"D:\Desktop\C & C++")
    ex(new_name="demo",target_type="jpg",order_key=lambda x: int(x[ x.rfind(".")-1 : x.rfind(".")+1] ) )


