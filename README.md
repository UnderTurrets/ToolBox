﻿
# Brief
This is a repo of some smallTools created by python.

# module 1:`image_spider`

- This tool allow you to crawl images from `3` website, which are Pixiv,Bing and Baidu.

## Module:`pixiv`
- Make sure that your internet can visit the foreign websites.
- The module has two ways to crawl images:`Rank` and `keyword`.

### Easy use
```python
import ToolBoxByHanXu.image_spider.pixiv as pixiv
if __name__ == '__main__':
    example=pixiv.pixiv_spider()
    example()
```

### search by `Rank`
- Looking at the following example:
```shell
{'1': 'Rank', '2': 'Keyword'}
Type in the target you want to search.
1
{'1': 'Simple:Recommended and Fast because the downloaded images are vague.You can view the simple image and select what you love', '2': 'Specific:Not Recommended and Slow because the downloaded images are clear'}
Type in the requirement of download-mode.
1
type in the path where you want to reserve the images:
rank20230424
Type in the number of images you want:
5
{'1': 'daily', '2': 'weekly', '3': 'monthly', '4': 'rookie', '5': 'daily_ai', '6': 'male', '7': 'female'}
type in the searchMode you want
1
Type in the date you want to search.Follow the format like this:20230423
20230424
```

### search by `keyword`
```shell
{'1': 'Rank', '2': 'Keyword'}
Type in the target you want to search.
2
{'1': 'Simple:Recommended and Fast because the downloaded images are vague.You can view the simple image and select what you love', '2': 'Specific:Not Recommended and Slow because the downloaded images are clear'}
Type in the requirement of download-mode.
1
type in the path where you want to reserve the images:
秋山澪图片
Type in the number of images you want:
5
{'1': '500', '2': '1000', '3': '5000', '4': '10000'}
Type in the requirement of heat.Larger the number is,Less the results are.
2
type in the keywords used to search in pixiv:
秋山澪
```

## Module:`bing`
- Use the following code to run the module.
```python
import ToolBoxByHanXu.image_spider.bing as bing

if __name__ == '__main__':
    example=bing.Spider_bing_image()
    example()
```
```shell
type in the path where you want to reserve the images:秋山澪
type in the keywords used to search in bing:秋山澪
Type in the number of pages you want.Each page has almost 30 images:1
```

## Module:`baidu` 
- The package can crawl the images at baidu based on the `keyword` offered by you.
- use the following code to use the package
```python
import ToolBoxByHanXu.image_spider.baidu as baidu

if __name__ == '__main__':
    example = baidu.Spider_baidu_image()
    example()
```
```shell
type in the path where you want to reserve the images:秋山澪
type in the keywords used to search in Baidu:秋山澪
Type in the number of pages you want.Each page has 30 images:1
```


# module 2:`normalize_md`
- Usually, when we write the md file, the images in the md file are bundled with the internet. If you want to view the images offline, you should download the images at advanced and modify the image-urls in the md file, **which is awful and takes much time!** This tool allow you to download the internal images in the md file automatically so that you could view the md file without the internet anymore!
- **The algorithm is in-place!You'd better copy the md dir in advance.**

```python
import ToolBoxByHanXu.normalize_md as normal

if __name__ == '__main__':
    # replace the directory you want to rename
    target_directory = r"D:\Desktop\demo"
    normal.normalizer(current_dir=target_directory)()
```
## result:
- before:

![在这里插入图片描述](assets/imgRes/2023-11-16-121919.png)

![在这里插入图片描述](assets/imgRes/2023-11-16-122550.png)

- after:

![在这里插入图片描述](assets/imgRes/2023-11-16-121942.png)

![在这里插入图片描述](assets/imgRes/2023-11-16-121930.png)

# module 3:`rename_files`
- This tool could rename all the files in a directory decided by you. You have `2` choices to rename them.
## rename by order
- If you don't mind the `filename extension`, you could rename all of them at one time.**Given New name and order key**, the code will add the order automatically.

```python
import ToolBoxByHanXu.rename_files as rename

if __name__ == '__main__':
    # replace the directory you want to rename
    example=rename.renamer(r"D:\Desktop\C & C++")
    example(new_name="demo",order_key=lambda x: int(x[ x.rfind(".")-1 : x.rfind(".")+1] ) )
```

## rename by `filename extension`
- For example, if you want to rename all the images, you may type in `jpg` or `png` as followed.

```python
import ToolBoxByHanXu.rename_files as rename

if __name__ == '__main__':
    # replace the directory you want to rename
    example=rename.renamer(r"D:\Desktop\C & C++")
    example(new_name="demo",target_type="jpg")
```

## result:

![在这里插入图片描述](assets/imgRes/2023-11-16-120758.png)

