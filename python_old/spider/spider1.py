#!/usr/bin/python
#Filename: spider.py  20170629
import urllib.request 
##content = urllib.request.urlopen('http://search.sina.com.cn/?q=%E9%A6%99%E6%B8%AF&c=news&from=channel&ie=utf-8').read()  

import html.parser
class MyParser(html.parser.HTMLParser):
    def __init__(self):
        html.parser.HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    print(value)
if __name__=='__main__':
    content = '<html><body><a href="http://www.weibo.com" target="_blank">WeiboSite</a></body></html>'
    my = MyParser()
    my.feed(content)
