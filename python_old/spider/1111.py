#!/usr/python3
import sys
import re
import urllib.request
def gethtml(url):
    page=urllib.request.urlopen(url)
    content=page.read()
    return content

content=gethtml("http://search.sina.com.cn/?q=%E9%A6%99%E6%B8%AF&c=news&from=channel&ie=utf-8")
