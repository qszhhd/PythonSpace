#Filename: spider4.py  20170629

#!/usr/python3
import re
import urllib.request
def gethtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html

def getimg(html):
##    reg = r'src="(.*?\.jpeg)"'
    reg =r"<a href=.*?<\/a>"
    img=re.compile(reg)
    html=html.decode('utf-8')#python3
    imglist=re.findall(img,html)
    x = 0
    for imgurl in imglist:
        b=urllib.request.urlretrieve(imgurl,'%s.html'%x)
        x = x+1
        return b
        
html=gethtml("http://www.baidu.com")
print(getimg(html))
