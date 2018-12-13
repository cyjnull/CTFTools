# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys, io

url = "http://ctf5.shiyanbar.com/jia/index.php"
url_check = "http://ctf5.shiyanbar.com/jia/index.php?action=check_pass"
s = requests.session()

respons = s.get(url)

soup = BeautifulSoup(respons.text, features="html.parser")
a = soup.find("div", attrs={"name": "my_expr"}).get_text()
a = a.replace("x", "*")

response = s.post(url_check, data={"pass_key": eval(a)})

response.encoding = response.apparent_encoding

soup1 = BeautifulSoup(response.text, features="html.parser")
b = soup1.find("div", attrs={"id": "templatemo_content"})

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

print(b)