
#推荐算法--协作型过滤学习

#第一步：构造数据集：表达不同用户的偏好
#方法一：使用嵌套的字典(内存中，不适合规模巨大的数据）

#一个涉及影评者及其对几部电影评分情况的字典
critics={'Lisa Rose':{'Lady in the Water':2.5,'Snakes on a Plane':3.5,
                      'Just my Luck':3.0,'Superman Returns':3.5,
                      'You, Me and Dupree': 2.5,'The Night listener':3.0},
         'Gene Seymour':{'Lady in the Water':3.0,'Snakes on a Plane':3.5,
                         'Just my Luck':1.5,'Superman Returns':5.0,
                      'You, Me and Dupree': 3.5,'The Night listener':3.0},
         'Michael Phillips':{'Lady in the Water':2.5,'Snakes on a Plane':3.0,
                             'Superman Returns':3.5,'The Night listener':4.0},
         'Claudia Puig':{'Snakes on a Plane':3.5,'Just my Luck':3.0,
                         'The Night listener':4.5,'Superman Returns':4.0,
                      'You, Me and Dupree': 2.5},
         'Mick LaSalle':{'Lady in the Water':3.0,'Snakes on a Plane':4.0,
                      'Just my Luck':2.0,'Superman Returns':3.0,
                      'You, Me and Dupree': 2.0,'The Night listener':3.0},
         'Jack Matthews':{'Lady in the Water':3.0,'Snakes on a Plane':4.0,
                      'The Night listener':3.0,'Superman Returns':5.0,
                      'You, Me and Dupree': 3.5},
         'Toby':{'Snakes on a Plane':4.5,'Superman Returns':4.0,
                 'You, Me and Dupree': 1.0}}


#第二步;搜索与目标用户喜好相近的人群
         
#基于欧几里得距离的相似度评价
from math import sqrt
def sim_distance(prefs,person1,person2):
    #得到shared_items列表
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    #如果两者没有共同之处，则返回0：
    if len(si)==0:return 0

    #计算所有差值的平方和(欧几里得距离评价）
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                        for item in prefs[person1] if item in prefs[person2]])

    #偏好越近，距离越短，返回值越大
    return 1/(1+sqrt(sum_of_squares))




#基于皮尔逊相关度的相似度评价

#返回p1和p2的皮尔逊相关系数
def sim_pearson(prefs,p1,p2):
    #得到shared_items列表
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1

    #得到列表元素个数
    n=len(si)

    if n==0:return 1

    #对所有偏好求和
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])

    #求平方和
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

    #求乘积之和
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

    #计算皮尔逊评价值
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0

    r=num/den

    return r

            


#从反映偏好的字典中返回最为匹配者

#返回结果的个数和相似度函数均为可选参数
def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other),other) for other in prefs if other != person]

#对列表排序，评价值最高者在最前面
    scores.sort()
    scores.reverse()
    return scores[0:n]




#第三步：利用所有他人评价值的加权平均，为特定用户提供建议
def getRecommendations(prefs,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
        #不和自己作比较
        if other==person:continue
        sim=similarity(prefs,person,other)

        #忽略评价值小于0或为负的情况
        if sim<=0:continue
        for item in prefs[other]:

            #只对自己还未看过的电影进行评价
            if item not in prefs[person] or prefs[person][item]==0:
                #相似度*评分
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim

                #相似度之和
                simSums.setdefault(item,0)
                simSums[item]+=sim

    #建立一个归一化的列表
    rankings=[(total/simSums[item],item)for item,total in totals.items()]
    
    #返回经过排序的列表
    rankings.sort()
    rankings.reverse()
    return rankings


#匹配商品，将上述方法中的物品与人员对调
def transformPrefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})

           #将物品与人员对调
            result[item][person]=prefs[person][item]
    return result

