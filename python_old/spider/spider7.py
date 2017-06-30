#!/usr/python3
#coding:utf-8
import requests
url="http://www.starbaby.cn/zhinan/609987"
req =requests.get(url)
req.encoding='utf-8' #显式地指定网页编码，一般情况可以不用
print(req.text)
