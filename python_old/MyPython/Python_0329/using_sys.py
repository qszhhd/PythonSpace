#!/usr/bin/python
#Filename:using_sys.py 20170329

import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)
    
print('\n\nThe PYTHONPATH is',sys.path,'\n')


