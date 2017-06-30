#!/usr/bin/python
#Filename:mymodule_demo2.py 20170329

##from mymodule import sayhi,version
# Alternative:
from mymodule import * #import * from mymodule是错误的用法

sayhi()
print('Version',version)
