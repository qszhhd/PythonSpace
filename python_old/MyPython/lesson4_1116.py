#--------读文件------
##f=open('data.txt');#打开文件用open，不是file
####data=f.read();#read（）方法从打开的文件中读取字符串。Python字符串可以是二进制数据，而不仅仅是文字。
####data=f.readline();#readline() 读取一行内容
##data=f.readlines() #把内容按行读取至一个list中
##print(data)
##f.close()
#-------读文件结束---


#-----写文件------
##f=open('output.txt','w')
##f.write('a string you want to write');
##data='I will be in a file.\n So cool!'
##f=open('output.txt','a');
##f.write(data)
##f.close()
#---写文件结束-----


#-----读写文件练习1：从一个文件中读出内容，保存至另一个文件------
##f=open('data.txt');
##data=f.readlines()
##f.close()
##
##f=open('output.txt','a')
##f.write('\n')
##f.write(data);#write() argument must be str, not list
##f.close()
#-----读写练习1结束，write()参数必须是字符串


#----读写文件练习2：从控制台输入一些内容，保存至一个文件------
##data1=input()
##f=open('11.txt','w')
##f.write(data1)
##f.close()
#---读写文件练习2结束


#----处理文件-----
##f=open('scores.txt')
##data=f.readlines()#将文件中的内容读入，存入list
##print(data)
##f.close()
##
##results=[]
##for line in data:
##    data1=line.split()#将list中的数据按照空格分开
##    print(data1)
##    sum1=0
##    for score in data1[1:]:
##        sum1+=int(score)
##    result='%s\t:%d\n'%(data1[0],sum1)
##    results.append(result)
##    
##f=open('results.txt','w')
####f.write(results)#write() argument must be str, not list
##f.writelines(results)#将list写入文件
##f.close()
#----处理文件结束----


#----break和continue的使用------
####while循环在条件不满足时结束，for循环遍历完序列后结束。
####在循环条件仍然满足或序列没有遍历完的时候，break彻底跳出循环；
####continue只是略过本次循环的余下内容，直接进入下一次循环。
####无论是continue还是break，其改变的仅仅是当前所处的最内层循环
####如果外层还有循环，并不会因此略过或跳出。    
##i = 0
##while i < 5:
##   i += 1
##   for j in range(3):
##       print(j)
##       if j == 2:
##           break
##   for k in range(3):
##       if k == 2:
##           continue
##       print(k)
##   if i > 3:
##       break
##   print(i)
#---break和continue使用结束------


#----异常处理：try...except语句----
####把可能引发异常的语句放在try-块中，把处理异常的语句放在except-块中。
##try:
##    f=file('non-exist.txt')
##    print('File opened!')
##    f.close()
##except:
##    print('File not exists.')
##print('Done.')
#----异常处理结束---------------


#----Dictionary：d={key1:value1,key2:value2}----
###Dictionary中的键/值对没有顺序，无法用索引访问，要用键来访问
##score={'夜华':['白浅','十里桃花',1],
##       '东华':['凤九','枕上书',2],
##       '连宋':['成玉','步生莲',3]}
##print(score['夜华'])
##
##for name in score:
##    print(score[name])#输出无序#
##
##del score['连宋']
##
##for name in score:
##    print(name,score[name])
#---Dictionary结束---------------


#----保存游戏得分:还是有不完善的地方-------------
####name=input('请输入你的名字：')
####f=open('record.txt')
####lines=f.readlines()#这里必须使用readlines
####print(lines)
####f.close()
####
####scores={}#初始化一个空Dictionary
####for i in lines:
####    s=i.split()#将读入的文件中的每一行数据拆分为list
####    scores[s[0]]=s[1:]#将第一项作为key,其余作为value
####score=scores.get(name)#查找当前玩家数据
####if score is None:#如果没找到，
####    score=[0,0,0]#初始化数据
####    
######for i in lines:
######    score=i.split()
####  
####    
####game_times=int(score[0])
####min_games=int(score[1])
####total_games=score[2]
####
####if game_times>0:#0不能做除数
####    avg_times=float(total_games)/game_times#转换为浮点数除法，整数除法结果默认为整数，而且会四舍五入
####else:
####    avg_times=0
####      
####def guessnum():
####    from random import randint
####    num=randint(1,100)
####    Bingo=0
####    game=0;
####    syn1=0
####    print('Guess What I think?')
####    while Bingo==0:
####        result=int(input())
####        game+=1
####        if result<0:
####            print('本轮游戏结束!')#由于if顺序执行，如果将这个放在if的最后一个，永远都执行不到
####            syn1=1
####            break
####        elif result>num:
####            print('Too big!')
####            Bingo=0
####        elif result<num:
####            print('Too small!')
####            Bingo=0
####        elif result==num:
####            print('Bingo!')
####            Bingo=1
####
####    return game,syn1
####
####
####game_run=0
####syn=0
####record=[]
####while syn==0:
####    #加上玩家名字
####    print('%s,你已经玩了%d轮，最快%d次猜出，平均%.2f次猜出'%(name,game_times,min_games,avg_times))
####    [guess_time,syn]=guessnum()
####    game_run+=1
####    record.append(guess_time)
####    
####    total_games=sum(record)
####    game_times=game_run
####    min_times=min(record)#不知道为什么，判断不对，总是0
######    if game_times==0 or guess_time<min_games:
######        min_games=guess_time
####    
####    if game_times>0:
####        avg_times=float(total_games)/game_times
####    else:
####       avg_times=0
####
####
####      
####f=open('record.txt','w')
######rec=[game_times,min_games,avg_times]
######rec='%s %s %s'%(game_times,min_games,avg_times)#指定格式
####
#####将成绩更新到对应的玩家数据中
####scores[name]=[str(game_times),'',str(min_games),'',str(avg_times)]
####print(scores)
####rec=''#初始化一个空字符串，用于存储数据
####for n in scores:
####    #将成绩格式化存储'
####    line=n+'  '+'  '.join(scores[n])+'\n'
####    rec+=line
####    print(rec)
####
####f.write(rec)#write() argument must be str, not int
####f.close()
#-----保存游戏结束--------------------------------


#----天气游戏：天气网的网址更改了，读到的内容是所有的代码------
import urllib.request
##web=urllib.request.urlopen('http://www.baidu.com')
##content=web.read()
##print(content)

from city import city 

cityname=input('你想查哪个城市的天气？\n')
citycode=city.get(cityname)
print(citycode)

if citycode:
##    url=('http://www.weather.com.cn/data/cityinfo/%s.html'%citycode)
    url=('http://m.weather.com.cn/mweather/%s.shtml'%citycode)
    content=urllib.request.urlopen(url).read().split()
    print(content)
#---天气游戏未完成---------------



#----


    


    

