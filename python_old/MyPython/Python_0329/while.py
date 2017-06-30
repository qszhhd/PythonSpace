#!/usr/bin/python
#Filename:while.py  20170329
number=23
running=True

while running:
    guess=int(input('Please input an integer:'))
    if guess==number:
        print('Congratulations!')
        running=False
    elif guess<number:
        print('It is a little higher than that!')
    else:
        print('It is a little lower than that!')
else:
    print('The loop is over!')

print('Done.')
    
    
