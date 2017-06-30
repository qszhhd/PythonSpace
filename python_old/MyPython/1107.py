import math 
# def my_quadratic(a,b,c):
   # delta=b*b-4*a*c;
   # if delta>=0:
       # x1=(math.sqrt(delta)-b)/(2*a); 
       # x2=(-math.sqrt(delta)-b)/(2*a);
       # return x1,x2;
   # else:
       # x1=(math.sqrt(-delta)*1j-b)/(2*a); #Python中，虚数i:1j; 2i:2j;
       # x2=(-math.sqrt(-delta)*1j-b)/(2*a);
       # return x1,x2;
# s1=my_quadratic(2,3,1);
# s2=my_quadratic(1,3,-4);
# print(s1,s2)

# def fact(n):
    # if n==1:
        # return 1
    # return n*fact(n-1)
    
# print(fact(100))
# print(fact(1000)) #函数溢出堆栈

##-----尾递归：在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
##-----这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
##-----尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
##-----大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

# def fact(n):
    # return fact_iter(n, 1)

# def fact_iter(num, product):
    # if num == 1:
        # return product
    # return fact_iter(num - 1, num * product)
    
    
#-----汉诺塔的移动：设A上有n个盘子；则先将A上的n-1个全部转移到B上，然后将最后一个给C；再将B上的n-1个给C；
# def hanoi(n,a,b,c):
    # if n==1:
        # print(a,'-->',c)
    # else:
        # hanoi(n-1,a,c,b)#将前n-1个盘子从a移动到b上
        # hanoi(1,a,b,c)#将最底下的最后一个盘子从a移动到c上
        # hanoi(n-1,b,a,c)#将b上的n-1个盘子移动到c上
# n=int(input('请输入汉诺塔的层数：'))
# hanoi(n,'a','b','c')


# -----Python的高级特性：Slice(切片)
# L=['A','B','ABC',1,3,2.5]
# print('L[0:3]=',L[0:3]);
# print('L[3:5]=',L[3:5]);
# print('L[1:6]=',L[1:6]);

# R=list(range(100));
# print('R[:10]=',R[:10]);
# print('R[91:]=',R[91:]);
# print('R[-10:]=',R[-10:]);
# print('R[-10:-5]=',R[-10:-5]);
# print('R[10:20]=',R[10:20]);
# print('R[:10:2]=',R[:10:2]);
# print('R[::5]=',R[::5]);

##-----列表生成式
# L=['Hello','World','Apple']
# print([s.lower() for s in L])

L1=['Hello','World',18,'Apple',None]
L2=[]
for s in L1:
    if isinstance(s,str)==True:
        L2.append(s)
print([s.lower()for s in L2])
        
# print([s.lower() for s in L1 & isinstance(s, str)==True])

##-----generator:杨辉三角
def triangles(max):
    while n<max
    a=1;b=(1 1);
    