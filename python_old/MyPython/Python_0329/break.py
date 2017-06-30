#!/usr/bi/python
#Filename:break.py 20170329
running=True
while running:
    s=input('Please input a string:')
    if s=='quit':
        break
    print('Length of the string is', len(s))
    print('input continue.')
##else:
##    print('The loop is over!')
print('Done.')
    
