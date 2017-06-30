#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
#告诉Python解释器，按照UTF-8编码读取源代码
n=123;f=456.789;
s1='Hello, world';s2='Hello, \'Adam\'';s3='Hello,"Bart"';s4='''hello,
Lisa!'''
print(n,f,s1,s2,s3,s4)
print('中文测试')
print('Hello,%s'%'world')
print('\'Hello,%s'%'world')
print('Hi,%s,you have $%d。'%('Michale',10000))
print('%d-%02d-%3d'%(1,3,2))  
print('Age:%s\nGender:%s\nIs Student:%s'%(25,'Female',True))
print('growth rate:%d %%'% 7)
G1=72;G2=85;r=(G2-G1)/G1;print('%.1f'%r);

L=[['Apple','Google','Microsoft'],['Java','Python','Ruby','PHP'],['Adam','Bart','Lisa']]
print(L[0][0],L[1][1],L[2][2])
Height=172;Weight=60;
BMI=Weight*Weight/Height;
print(BMI)
if BMI>32:
    print('overfat')
elif 28<BMI:#不用写28<BMI<32
    print('fat')
elif 25<BMI:
    print('heavy')
elif 18.5<BMI:
    print('normal')
else:
    print('too weak')
    