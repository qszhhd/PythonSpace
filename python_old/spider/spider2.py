#Filename: spider2.py  20170629

#encoding:UTF-8
import urllib.request
 
##url = "http://www.baidu.com"
##data = urllib.request.urlopen(url).read()
##data = data.decode('UTF-8')
##print(data)


####data={}
####data['word']='Jecvay Notes'
#### 
####url_values=urllib.parse.urlencode(data)
####url="http://www.baidu.com/??"
####full_url=url+url_values
#### 
####data=urllib.request.urlopen(full_url).read()
####data=data.decode('UTF-8')
####print(data)

import re
import urllib.request

from collections import deque
 
queue = deque()
visited = set()
 
url = 'http://search.sina.com.cn/?q=%E9%A6%99%E6%B8%AF&c=news&from=channel&ie=utf-8'  # 入口页面, 可以换成别的
 
queue.append(url)
cnt = 0
 
while queue:
  url = queue.popleft()  # 队首元素出队
  visited |= {url}  # 标记为已访问
 
  print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
  cnt += 1
  urlop = urllib.request.urlopen(url)
  if 'html' not in urlop.getheader('Content-Type'):
    continue
 
  # 避免程序异常中止, 用try..catch处理异常
  try:
    data = urlop.read().decode('utf-8')
  except:
    continue
 
  # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
##  linkre = re.compile('href=\"(.+?)\"')
##  linkre = re.compile(r'<tr>(.*?)</tr>')
##  linkre = re.compile(r'<a .*?>(.*?)</a>')
  
  linkre =re.compile(r"<a href=.*?<\/a>")
  for x in linkre.findall(data):
    if 'http' in x and x not in visited:
      queue.append(x)
      print('加入队列 --->  ' + x)
