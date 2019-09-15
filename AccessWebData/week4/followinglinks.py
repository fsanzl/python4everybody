#!/usr/bin/python3
# Use words.txt as the file name
# Use the file name mbox-short.txt as the file name
import re
from bs4 import BeautifulSoup
import urllib.request

def spider(direccion,count):
    if 
        count=count+1
        html = urllib.request.urlopen(direccion)
        soup=BeautifulSoup(html,'html.parser')
        tags = soup('a')
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Darrel.html').read()
tags = soup('a')
linkn=1
for tag in tags:
    if linkn<18:
        linkn=linkn+1
        continue
    else:
        spider(tag,4)
        break

def spider(direccion,count):
    count=count+1
    html = urllib.request.urlopen(direccion)
    soup=BeautifulSoup(html,'html.parser')
    tags = soup('a')





html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Darrel.html').read()
tags = soup('a')

for tag in tags:
    count=count+int(tag.contents[0])
    count=count+1
    if count = 18:
        break
print(count)
