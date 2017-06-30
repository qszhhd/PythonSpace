###--------1113：第1个小游戏------------------
####num=10;
####print('Guess what I think?');
####answer=int(input());#Python3中input()默认输入的都是字符串；
####
####while answer!=num:
####    if answer<num:
####         print("too small！");
####    else:
####         print("too big！");
####print('Bingo!');         
##
##
####按照上述方式写的程序，进入了死循环；原因是：输入7，输出“too small!”；没有终止条件；程序一直输出“too small!”
###改进如下：
##
##from random import randint #引入随机模块，产生随机整数；
##
###num=10;
##num=randint(1,100);
##print('Guess what I think?');
##Bingo=False    #开始循环前设置一个条件
##
##while Bingo==False:
##     answer=int(input())#Python3中input()默认输入的都是字符串；
##     if answer<num:
##         print('%d is Too small!'%answer)
##     elif answer>num:
##         print('%d is Too big!'%answer)
##     else:
##         print('Bingo!%d is right!'%answer)
##         Bingo==True;
###---------第1个小游戏的分割线--------------------

#-----练习：编写函数修改第1个小游戏-------
##def isEqual(num1,num2):
##    if num1<num2:
##        print('%d is too small'%num1);
##        return False
##    elif num1>num2:
##        print('%d is too big'%num1);
##        return False
##    else:
##        print('bingo!%d is right'%num1);
##        return True
##
###return是函数的结束语句，return后面的值被作为这个函数的返回值。
###函数中任何地方的return被执行到的时候，这个函数就会结束
##
###或者利用这个函数修改第1个小游戏：
##
##from random import randint
##num=randint(1,100)
##print('Guess What I Think?')
##
##bingo=False
##while bingo==False:
##    answer=int(input())
##    bingo=isEqual(answer,num)
#------编写函数完成--------------------

#--------练习：高斯大牛在小时候做过的题---------
##sum1=0;
####num=1;
####while num<101:
####    sum1=sum1+num;
####    num=num+1;
####print(sum1);
##
##
##for i in range(1,101): #range(a,b)产生一组从a到b-1的整数序列
##    sum1=sum1+i;
##print(sum1);
#------------Say bye to Gauss-----------------------------


#------练习：输出字符串---------
##print('''He said,"I'm yours!"''');
##print('\\\\_v_//');
##print('''
##Stay hungry,
##stay,foolish.
##        -- Steve Iobs''');
##print('''
##         *
##         ***
##         *****
##         ***
##         *''');
##print('My name is %s.'%'Crossin');
##print('The price is $%.2f.'%5.25);
##print('His age is %d.'%25);
##print("%s's score is %d"%('Mike',87));
#------输出字符串结束-------------

#-----练习：类型转换--------------
## 在python中，以下数值会被认为是False：
##   为0的数字，包括0，0.0
##   空字符串，包括''，""
##   表示空值的None
##   空集合，包括()，[]，{}
##   其他的值都认为是True

##bool(-123)
##bool(0)
##bool('abc')
##bool('False')
##bool('')
##bool( )
##bool(False)
#------类型转换练习结束--------

#-------1113：第2个小游戏---------------------
###字符串比较出错了，得不到想要的结果
##print('Who do you think I am?');
##you=input();
##
##if you=='My Love'or'Flower'or'Princess':
##      print('Oh,yes!');
##elif you=='Pig'or'Idiot':
##      print('No,you are a',you,'!');
##else:
##    print(None);
#---------字符串比较出错了，得不到想要的结果--------------------

#------练习：循环的嵌套----------
##for i in range(0,5):
##        print('*'),
#------和教程15上说的不一样，没实现------

#-----点球小游戏1.0-----------
##from random import choice
##score_you=0;
##score_com=0;
##direction=['left','center','right'];
##for i in range(5):
##    print('====Round %d -You Kick!===='%(i+1))
##    print('Choose one side to shoot:')
##    print('left,center,right')
##    you=input()
##    print('You kicked'+you)
##    com=choice(direction)
##    print('Computer saved'+com)
##    if you!=com:
##       print('Goal!')
##       score_you+=1
##    else:
##       print('Oops...')
##       print('Score:%d(you)-%d(com)\n'%(score_you,score_com))
##             
##    print('====Round %d -You Save!===='%(i+1))
##    print('Choose one side to save:')
##    print('left,center,right')
##    you=input()
##    print('You saved'+ you)
##    com=choice(direction)
##    print('Computer kicked'+com)
##    if you==com:
##        print('Saved!')
##    else:
##        print('Oops...')
##        score_com+=1;
##        print('Score:%d(you)-%d(com)\n'%(score_you,score_com))
#-----点球小游戏完成-------              
    
#-----点球小游戏2.0--------
from random import choice

score=[0,0];
direction=[1,2,3];

def kick():
    print('====You kick!====')
    print('choose one side to shoot:')
    print(1,2,3)
    you=int(input())
    print('You kicked'+str(you))

    com=choice(direction)
    print('Computer saved'+str(com))

    if you!=com:
        print('Goal!')
        score[0]+=1;
    else:
        print('Oops...')
        print('Score:%d(you)-%d(com)'%(score[0],score[1]));

    print('====You save!====')
    print('choose one side to save:')
    print(1,2,3)
    you=int(input())
    print('You saved'+str(you))

    com=choice(direction)
    print('Computer kicked'+str(com))

    if you==com:
        print('Saved!') 
    else:
        print('Oops...')
        score[1]+=1;
        print('Score:%d(you)-%d(com)'%(score[0],score[1]));

for i in range(5):
    print('====Round %d===='%(i+1))
    kick()

while(score[0]==score[1]):
    i+=1;
    print('====Round %d===='%(i+1))
    kick()

if score[0]>score[1]:
    print('You Win!')
else:
    print('You Lose.')

#----点球2.0 增加了胜负判断，平分继续玩，直到分出胜负-----
              
              
    

    

