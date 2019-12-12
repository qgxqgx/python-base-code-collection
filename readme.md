

#### utf-8 的文件申明

```
#coding=utf-8
```


#### 判断平台是否为 mac os

```
import platform

sysstr = platform.system()
if(sysstr =="Windows"):
    print ("Call Windows tasks")
elif(sysstr == "Linux"):
    print ("Call Linux tasks")
elif(sysstr == "Darwin"):
    print ("Call Mac os tasks")
else:
    print ("Other System tasks")
```

#### pip 安装慢

如果更新 pip 很慢的话，可以使用这个命令来制定镜像源更新 pip
```
pip install -i http://pypi.doubanio.com/simple pip -U
```
其他可切换的源
```
http://pypi.douban.com/  豆瓣
http://pypi.hustunique.com/  华中理工大学
http://pypi.sdutlinux.org/  山东理工大学
http://pypi.mirrors.ustc.edu.cn/  中国科学技术大学
```