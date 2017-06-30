#!/usr/bin/python
#Filename: apihelper.py  20170411
def info(object,spacing=20,collapse=1):
    '''Print methods and doc_strings.

       Takes module,class,function,list,dict.'''
    methodList=[method for method in dir(object) if callable(getattr(object,method))]
    processFunc=collapse and (lambda s:' '.join(s.split())) or(lambda s:s)
    print('\n'.join(['%s %s'%(method.ljust(spacing),processFunc(str(getattr(object,method).__doc__)))
                     for method in methodList]))

if __name__=='__main__':
    print(info.__doc__)
    
    
   
