#!/usr/bin/python
#Filename:if.py 20170329
number=23
guess=int(input('Please Enter an integer:'))

if guess==number:
    print('Congratulations!')
    print('(but you do not with any prizes.)')
elif guess<number:
    print('No,it\'s a little higher than that')
else:
    print("No,it\'s a little lower than that")

print('Done')
# This last statement is always executed, after the if statement is executed
