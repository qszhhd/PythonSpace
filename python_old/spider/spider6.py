#Filename: spider4.py  20170629

#!/usr/python3
#coding:utf-8
import re
import urllib.request
def gethtml(url):
    page=urllib.request.urlopen(url)
    content=page.read()
    return content

content=gethtml("http://search.sina.com.cn/?q=%E9%A6%99%E6%B8%AF&c=news&from=channel&ie=utf-8")


rtitle =r' target="_blank">.*?</a> '
img2=re.compile(rtitle)
##content=content.decode('utf-8')#python3
content=content.decode('utf-8',errors='ignore')#python3
titles=re.findall(img2,content)

rhtml =r'<h2><a href="http:.*?"'
img=re.compile(rhtml)
##content=content.decode('utf-8',errors='ignore')#python3
urls=re.findall(img,content)

i=0;
for url in urls:
    i=i+1;
    print(url)
    

for title in titles:
##    a=title.encode('utf-8')
##    print(title.encode('utf-8'))
    print(title)
##    print(title)
##    print(title.encode('utf8').decode('unicode-escape'))
