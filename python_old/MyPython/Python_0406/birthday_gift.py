##生日礼物（京东2016实习生真题）
##BF的生日快到了，这一次，小东决定为BF送一份特别的生日礼物为其庆生。作为高智商中的佼佼者，BF在国外求学，因此小东无法与之一起庆生。小东计划送一个生日卡片，并通过特别的包装让BF永远难忘。
##
##她决定把卡片套装在一系列的信封A = {a1,  a2,  ...,  an}中。小东已经从商店中购买了很多的信封，她希望能够用手头中尽可能多的信封包装卡片。为防止卡片或信封被损坏，只有长宽较小的信封能够装入大些的信封，同尺寸的信封不能套装，卡片和信封都不能折叠。
##
##小东计算了邮寄的时间，发现她的时间已经不够了，为此找你帮忙包装，你能帮她吗？
##
##输入
##输入有若干组，每组的第一行包含三个整数n, w, h，1<=n<=5000, 1<=w, h<=10^6，分别表示小东手头的信封数量和卡片的大小。紧随其后的n行中，每行有两个整数wi和hi，为第i个信封的大小，1<=wi, hi<=10^6。
##样例输入
##2 1 1
##2 2
##2 2
##3 3 3
##5 4
##12 11
##9 8
##
##输出
##对每组测试数据，结果第一行中输出最多能够使用的信封数量，结果第二行中按使用顺序输出信封的编号。由于小东有洁癖，她对排在前面的信封比较有好感，若有多个信封可用，她喜欢用最先拿到的信封。另外别忘了，小东要求把卡片装入能够装的最小信封中。
##如果卡片无法装入任何信封中，则在单独的行中输出0。
##
##样例输出
##1
##1
##3
##1 3 2
##
##时间限制
##C/C++语言：1000MS
##其他语言：3000MS
##内存限制
##C/C++语言：65536KB
##其他语言：589824KB

#!/usr/bin/python

stopword=''
str1=''
for number in iter(input,stopword):
    str1+=number+'\n'
    
s=str1.split('\n')

s0=s[0].split(' ')
if len(s0)!=3:
    print('输入参数数量错误!')
elif (1<=int(s0[0])<=5000)&(int(s0[1])>=1)&(1<=int(s0[1])<=10^6):
    n=int(s0[0])#信封数量
    w=int(s0[1])#卡片宽度
    h=int(s0[2])#卡片高度
    

envelop=[[0 for col in range(2)]for row in  range(len(s)-2)]
for i in range(1,len(s)-1):
    if len(s[i].split(' '))!=2:
        n=n-1
        continue
    s1=s[i].split(' ')
    envelop[i-1][0]=int(s1[0])
    envelop[i-1][1]=int(s1[1])
    

print('n=',n,'w=',w,'h=',h)
print(envelop)

#----以上：实现将信封数据封装好

def unique_index(L,W):
    Index=[]
    for item,times in W.items():
        WIndex=[i for (i,j) in enumerate(L) if j==item]
        Index.append(WIndex)
    return Index
    

def find_repeat(L):
    countR={}
    rep={}
    for item in set(L):
        countR[item]=L.count(item)
    for item,times in countR.items():
        if (times>1)&(item!=0):
            rep[item]=times
##            return('%d repeat %d times'%(item,times))
    return rep

def find_min(Win,L):
    min_index=[]
    for item in Win:
        ind=[i for (i,j) in enumerate(L) if (j==(min([L[j] for j in item])))& (i in item)]
        min_index.append(ind)
    return min_index


Index=[0.1 for i in range(len(envelop))]
count=0
for i in range(len(envelop)):
    if (envelop[i][0]>w)&(envelop[i][1]>h):
        Index[i]=i
        count=count+1
print(Index)

del_en=[]
for i in range(len(Index)):
    if Index[i]==0.1:
        del_en.append(i)
        envelop[i]=[int(0),int(0)]
print(del_en)    
print(envelop)
                    
envelop2=envelop

a=[a[0] for a in envelop]
b=[a[1] for a in envelop]
Wrepeat=find_repeat(a)
Hrepeat=find_repeat(b)

print('Wrepeat is',Wrepeat)
print('Hrepeat is',Hrepeat)

##WIndex=[]
##
##for item,times in Wrepeat.items():
##    WIndex.append(a.index(item))
##print(WIndex)

Windex=unique_index(a,Wrepeat)
Hindex=unique_index(b,Hrepeat)
print('Windex is',Windex)
print('Hindex is',Hindex)

print(a)
print(b)
Wmin_index=find_min(Windex,b)
Hmin_index=find_min(Hindex,a)

print('Wmin_index is',Wmin_index)
print('Hmin_index is',Hmin_index)

def con1(L):
    return(list(set(sum(L,[]))))

Index1=con1(Windex+Hindex)

for j in  con1(Windex):
    if j not in con1(Wmin_index):
       Index.remove(j)

for j in  con1(Hindex):
    if j not in con1(Hmin_index):
        Index.remove(j)
        
