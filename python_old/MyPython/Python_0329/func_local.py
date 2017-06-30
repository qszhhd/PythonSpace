#!/usr/bin/python
#Filename:func_local.py  20170329
def func(x):
    print('x is',x)
    x=34;
    print('Change local x to',x)

x=65;
func(x)
print('x is still',x)
