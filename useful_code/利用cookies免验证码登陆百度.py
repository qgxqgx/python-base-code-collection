from selenium import webdriver  # 从selenium导入webdriver
import os
import platform
import traceback
import time
import pickle
BASE_PATH = os.path.abspath(os.path.dirname(__file__))


if platform.system() == 'Darwin':
    wd = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
else:
    wd = webdriver.Chrome(
        os.path.join(BASE_PATH, 'chromedriver.exe'))  # Optional argument, if not specified will search path.

url = 'https://zhidao.baidu.com/'
print(url)
wd.get(url)

cookie_path = os.path.join(BASE_PATH,'cookies2.txt')
readPath = open(cookie_path , 'r', encoding = 'utf-8')
BDCookies = readPath.read()
readPath.close()

allitem = BDCookies.split(';')

for item in allitem:
    pair = item.split('=')
    print('the pair ===>  ', pair)
    if pair and len(pair) == 2:
        cookie = pair[0].lstrip()
        value = pair[1]
        try:
            print(f'try add cookie "{cookie}"="{value}""')
            wd.add_cookie({
                "domain": "zhidao.baidu.com",
                "name": cookie,
                "value": value,
                "path": '/',
                "expires": None
            })
        except Exception as e:
            traceback.print_exc()

wd.get("https://zhidao.baidu.com")

time.sleep(30)

wd.close()
del wd




