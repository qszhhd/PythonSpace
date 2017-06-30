#Filename: spider4.py  20170629

#!/usr/python3
import sys
import re
import urllib.request
def gethtml(url):
    page=urllib.request.urlopen(url)
    content=page.read()
    return content

#获得系统的编码


##content=gethtml("http://www.baidu.com")
content=gethtml("http://search.sina.com.cn/?q=%E9%A6%99%E6%B8%AF&c=news&from=channel&ie=utf-8")

type1 = sys.getfilesystemencoding()

rhtml =r'<h2><a href="http:.*?"'
img=re.compile(rhtml)
##content = content.decode(type)
content=content.encode('utf-8 BOM')#python3
content=content.decode('utf-8',errors='ignore')#python3
##content = content.decode(type1)
urls=re.findall(img,content)

rtitle =r' target="_blank">.*?</a> '
img2=re.compile(rtitle)
##content = content.decode(type)
##content=content.decode('utf-8',errors='ignore')#python3
titles=re.findall(img2,content)


i=0;
for url in urls:
    i=i+1;
    print(url)
    
j=0;
for title in titles:
    j=j+1;
##    a=title;
##    a=a.decode(type)
##    print(a)
##    print(title.encode('utf-8'))
##    print(title.encode('utf-8'))
##    print(title))
    print(title.encode('utf8').decode('unicode-escape'))
