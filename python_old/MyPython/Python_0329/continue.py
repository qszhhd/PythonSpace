#!/usr/bin/python
#Filename:continue.py 20170329

while True:
    s=input('Enter something please:')
    if s=='quit':
        break
    if len(s)<3:
        continue
    print('Input is of sufficient length')

print('Done')
