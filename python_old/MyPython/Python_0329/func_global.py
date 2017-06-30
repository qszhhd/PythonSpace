#!/usr/bin/python
#Filename:func_global.py  20170329
y=3;
def func():
    global x
    print('x is',x)
    z=x+y;
    print('z is',z)
    x=2
    print('Change x to',x)

x=50
func()
print('Value of x is',x)
print('Value of y is',y)
