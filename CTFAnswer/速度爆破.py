#-*-coding:utf-8-*-
__author__ = 'Chennull'

from bs4 import BeautifulSoup
import requests
import hashlib

def get_Flag(content, url, status):
    for i in range(0, 100001):
        hashmd5 = hashlib.md5(str(i).encode("utf-8")).hexdigest()
        hashsha1 = hashlib.sha1(hashmd5.encode("utf-8")).hexdigest()
        if hashsha1 == content:
            i = int(i)
            post_Content = {'inputNumber': i, 'submit': '%E6%8F%90%E4%BA%A4'}  # 如果还有多个参数都构造，中文url编码后的用
            result = status.post(url, data=post_Content)
            # print(result.text)
            soup2 = BeautifulSoup(result.text,"html.parser")
            print(soup2.div.string)
            break


url = 'http://ctf5.shiyanbar.com/ppc/sd.php'
status = requests.session()
html = status.get(url).text
soup = BeautifulSoup(html, "html.parser")
get_Flag(soup.div.string, url, status)