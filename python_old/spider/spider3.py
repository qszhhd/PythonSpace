#Filename: spider3.py  20170629

##### coding=utf-8  
####import re  
####import urllib.request
####url = 'http://search.sina.com.cn/?q=%E9%A6%99%E6%B8%AF&c=news&from=channel&ie=utf-8'  # 入口页面, 可以换成别的
####
####content=urllib.request.urlopen(url).read()
######data=data.decode('UTF-8')
######print(data)
####  
#####获取<a href></a>之间的内容  
####print(u'获取链接文本内容:') 
####res = r'<a .*?>(.*?)</a>'  
####mm =  re.findall(res, content,re.S|re.M)
####mm =  re.findall(res, content,re.S|re.M)  
####for value in mm:  
####    print(value)  
####  
#####获取所有<a href></a>链接所有内容  
####print(u'\n获取完整链接内容:')  
####urls=re.findall(r"<a.*?href=.*?<\/a>", content, re.I|re.S|re.M)  
####for i in urls:  
####    print(i) 
####  
#####获取<a href></a>中的URL  
####print(u'\n获取链接中URL:')  
####res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"  
####link = re.findall(res_url ,  content, re.I|re.S|re.M)  
####for url in link:  
####    print(url)  


# coding=utf-8  
import re  
import urllib.request  
  
url = "http://www.csdn.net/"  
content = urllib.request.urlopen(url).read()  
urls = re.findall(r"<a.*?href=.*?<\/a>", content)  
for url in urls:  
    print(unicode(url,'utf-8')) 
      
link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", content)  
for url in link_list:    
    print(url)   
