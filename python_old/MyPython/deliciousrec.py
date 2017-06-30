import sys
sys.path.append('D:\Python\Lib\email')

import pydelicious

#得到近期张贴的编程方面的热门链接，以XML格式返回
pydelicious.get_popular(tag='programming')

#get_uslposts:返回给定URL的所有张贴记录
#get_userposts；返回给定用户的所有张贴记录

from pydelicious import get_popular,get_userposts,get_urlposts

def initializeUserDict(tag,count=5):
    user_dict={}
    #获取前count个最受欢迎的链接张贴记录
    for p1 in get_popular(tag=tag)[0:count]:
        #查找所有张贴该链接的用户
        for p2 in get_urlposts(p1['href']):
            user=p2['user']
            user_dict[user]={}
        return user_dict
