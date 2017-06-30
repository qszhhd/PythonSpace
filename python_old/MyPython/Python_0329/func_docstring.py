#!/usr/bin/python
#Filename:func_docstring.py 20170329
def printMax(x,y):
    '''This function prints maximum between x and y.

x and y must be integers.'''
    x=int(x)#convert to integers,if possible
    y=int(y)
    if x>y:
        print(x,'is Maximum.')
    else:
        print(y,'is Maximum.')

print(3,5)
print(printMax.__doc__)
