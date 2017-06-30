#----time模块-----

#----time.time()返回从epoch到当前的秒数（不考虑闰秒）。这个值被称为unix时间戳。
###----epoch，它表示的时间是1970-01-01 00:00:00 UTC
##import time
##starttime=time.time()
##print('start:%f'%starttime)
##for i in range(10):
##    print(i)
##endtime=time.time()
##print('end:%f'%endtime)
##
##print('total time:%f'%(endtime-starttime))
#----time.time()结束-----

#----time.sleep:让程序暂停secs秒;在抓取网页的时候，适当让程序sleep一下，可以减少短时间内的请求，提高请求的成功率。---
##import time
##print(1)
##time.sleep(3)
##print(2)
#----time.sleep()结束----

#----time模块结束---


#----list comprehension:通过一个已有的列表生成一个新的列表
##list_1=[1,2,5,2,10,56,21]
##list_2=[i/3 for i in list_1 if i%3==0]
##print(list_2)
##
###要求：用一行 Python 代码实现：把1到100的整数里，能被2、3、5整除的数取出，以分号（;）分隔的形式输出
##list_3=[i for i in range(1,101)if i%2==0 and i%3==0 and i%5==0]
##print(list_3)
##
##print(';'.join([str(i) for i in range(1,101) if i%2==0 and i%3==0 and i%5==0]))#用';'连接，join函数参数为字符串，因此需要转换类型

#----list comprehension结束----


#----函数参数传递-----
##def func(arg1,arg2):
##    print(arg1,arg2)
##
##func(3,7)
##func(arg2=7,arg1=3)


##def func3(arg1,arg2=3):#定义函数参数默认值
##    print(arg1,arg2)
##
##func3(3)
##func3(arg1=5,arg2=10)

##def calcSum(*args):#可以接受任意数量的参数,将参数作为tuple传入函数内部
####    在变量前加上星号前缀（*），调用时的参数会存储在一个 tuple（元组）对象中，赋值给形参。
####    在函数内部，需要对参数进行处理时，只要对这个 tuple 类型的形参（这里是 args）进行操作就可以了。
####    因此，函数在定义时并不需要指明参数个数，就可以处理任意参数个数的情况。
####    tuple 是有序的，所以 args 中元素的顺序受到赋值时的影响
##    sum=0
##    for i in args:
##        sum+=i;
##    print(sum)
##
##calcSum(123,323,123)
##calcSum(23)
##calcSum(1,2)
##calcSum()
##
##def printAll(**kargs):#不受参数数量、位置的限制，将参数以键值对字典的形式传入，字典是无序的
####    在调用时，参数的顺序无所谓，只要对应合适的形参名就可以
##    for k in kargs:
##        print(k,':',kargs[k])
##
##printAll(a=1,b=2,c=3)
##printAll(x=4,y=5)
        
##def func(x,y=5,*a,**b):#混合使用各种形参传递方式
##    print(x,y,a,b)
##
####函数写法必须遵守：
####带有默认值的形参(arg=)须在无默认值的形参(arg)之后；
####元组参数(*args)须在带有默认值的形参(arg=)之后；
####字典参数(**kargs)须在元组参数(*args)之后。
####
####调用时需要遵守：
####指定参数名称的参数要在无指定参数名称的参数之后；
####不可以重复传递，即按顺序提供某参数之后，又指定名称传递。
##
####而在函数被调用时，参数的传递过程为：
####1.按顺序把无指定参数的实参赋值给形参；
####2.把指定参数名称(arg=v)的实参赋值给对应的形参；
####3.将多余的无指定参数的实参打包成一个 tuple 传递给元组参数(*args)；
####4.将多余的指定参数名的实参打包成一个 dict 传递给字典参数(**kargs)。    
##
##func(1)
##func(1,2)
##func(1,2,3)
##func(1,2,3,4)
##func(x=1)
##func(x=1,y=2)
##func(x=1,y=1,a=1)
##func(x=1,y=1,a=2,b=3)
##func(1,y=1)
##func(1,2,3,4,a=1)
##func(1,2,3,4,k=1,t=2,o=3)
#----函数参数传递结束----


#----变量的作用域-----
##def func():
##  print('X in the beginning of func(x): ', x)
####  x = 2
##  print('X in the end of func(x): ', x)
##
##x = 50
##func()
##print('X after calling func(x): ', x)
#---变量的作用域 结束----

#----pickle模块：可以把任何 Python 对象存储在文件中，再把它原样取出来----
##import pickle
##
###----存储----
##m=['Save me!',123.456,True,'存储测试']
##
##f=open('test.data','wb')#---似乎必须使用'wb','rb';使用'w','r'会报错;是否在python 3中将pickle写入和读出都改为必须使用二进制了呢？
##pickle.dump(m,f)
##f.close()
##
###---取出----
##f=open('test.data','rb')
##test_data=pickle.load(f)
##f.close()
##
##print(test_data)

#----pickle模块结束-----

#----random模块----
##import random
####m=random.choice((1,2,3))
####m=random.randrange(4)
####m=random.sample([2,3,6,1,7,8,10,23,12,12,45],3)#sample不改变原来序列。
####m=random.shuffle([2,3,6,1,7,8,10,23,12,12,45])#shuffle直接改变原有的序列。
####m=random.shuffle('Hello world')
##
##m=random.seed()
##print(m)
##
###----shuffle和seed命令没有实现----
####在随机数中有个seed的概念，需要一个真实的随机数，比如此刻的时间、鼠标的位置等等，以此为基础产生伪随机数。
####在python中，默认用系统时间作为seed。你也可以手动调用random.seed(x)来指定seed

#----random模块结束


#----map函数：可以看作是把一个序列根据某种规则，映射到另一个序列
##作用是把一个函数应用在一个（或多个）序列上，把列表中的每一项作为函数输入进行计算，再把计算的结果以列表的形式返回。
##map 的第一个参数是一个函数，之后的参数是序列，可以是 list、tuple。

##lst_1 = (1,2,3,4,5,6)
##lst_2=list(map(lambda x:x*2,lst_1))#与Python 2不同，在Python 3中，map的结果需要手动转为list
##print(lst_2)
##lst_3 = [1,3,5,7,9,11]
##lst_4 = list(map(lambda x,y:x+y, lst_1,lst_3))
##print(lst_4)
##lst_5 = list(map(None, lst_1, lst_2))#如何输出呢？
##print(lst_5)

#----map函数结束，疑问是map(None,list)


#----reduce函数：把一个序列根据某种规则，归纳为一个输出
#Python3 里，reduce已经被移出内置函数，使用 reduce 需要from functools import reduce 引入
##from functools import reduce
####m=reduce(lambda x,y:x+y,range(1,101))
####print(m)
##
##
##def count1(x,y):
##    global sum1
##    if y==5: 
##        sum1+=1
##    return sum1
##
###function 需要是一个接收2个参数，并有返回值的函数。
####它会从序列里依次取出元素，进行计算。每次计算的结果，会作为下次计算的第一个参数。
##sum1=0
##n=reduce(count1,[1,3,4,2,3,4,2,5,1,2,3,3,3,4,2,4,5])
##print(n)

#----reduce函数结束
    
