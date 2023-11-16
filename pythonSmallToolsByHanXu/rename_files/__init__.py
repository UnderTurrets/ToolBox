"""
Created by Han Xu
email:736946693@qq.com
"""
import os


def rename(directory_path, new_name, target_type):
    # 切换到指定目录
    os.chdir(directory_path)

    # 获取目录下的所有文件
    files = os.listdir(directory_path)

    index = 1  # 如果文件自带下标，这里可以用索引去获取

    # 遍历所有文件并重命名
    for file in files:

        # 跳过一些系统文件
        if file == "desktop.ini":
            continue

        elif os.path.isdir(file) == False and file.rfind(".") != -1:

            # 获取文件后缀名
            file_type = file[file.rfind(".") + 1:]

            if target_type == "*" or target_type == file_type:
                target_name=new_name + f"({index})." + file_type
                os.rename(file, target_name)
                print(f"{directory_path}"
                      f"{file}-------->{target_name}",sep="\n")

            index = index + 1

    return


