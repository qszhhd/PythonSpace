#----编写函数----
##import math
##def resolve(a,b,c):
##    delta=pow(b,2)-4*a*c
##    result=[0,0]#在使用list前要先定义，而且如果定义成result=[]，无法使用索引访问
##    if delta>=0:
##        result[0]=(math.sqrt(delta)-b)/(2*a)#sqrt不能直接调用，必须用math.sqrt()
##        result[1]=(-math.sqrt(delta)-b)/(2*a)
##        return 'x1=%.2f,x2=%.2f'%(result[0],result[1])
##    else:
##        result[0]=(math.sqrt(abs(delta))*1j-b)/(2*a)
##        result[1]=(-math.sqrt(abs(delta))*1j-b)/(2*a)
##    return result
##
##print(resolve(5,4,1))
#----编写函数----



#----正则表达式----
##import re
##text1='或许你不相信 我很满意这样的结局 或许你不相信 我没有一丝的埋怨和悔意'
##text2='虽然你是我的最初 虽然你是我的最终 虽然你是我的唯一 You are my only one. You are my only only one'
##text3='Hi,I am Shirley Hilton.I am his wife.'
##m=re.findall(r'你.*?的',text2)
##if m:
##    print(m)
##else:
##    print('not match')


#字符串前面的r,是raw的意思，表示对字符串不进行转义
#正则表达式的作用：从一大段文字中抓取信息；判断输入文本是否符合规范；进行分类

###正则表达式中的专用字符称作“元字符”，如\b、\d、.、\S
###如果确实要匹配.或者*字符本身，而不是它们所代表的元字符，那就需要用\.或\*,\本身也需要用\\

###“\w”：匹配字母或数字或下划线或汉字（我试验下了，发现3.x版本可以匹配汉字，但2.x版本不可以）
###“\s”：匹配任意的空白符
###“\d”：表示数字
###“\b”：表示开头或结束位置

###“\W”：匹配任意不是字母或数字或下划线或汉字的字符
###“\S”：不是空白符的任意字符
###“\D”：表示任意非数字的字符
###“\B”：表示非开头或结束位置


###“^”：匹配字符串的开始
###“$”：匹配字符串的结束

###“.”：除换行符以外的任意字符。
###“[]”：表示其中任意一个字符
###“[^]”：除[]内字符外的任意字符

###“*”：前面的字符可以重复任意多次（包括0次），只要满足这样的条件，都会被表达式匹配上默认“*”是贪婪匹配；如果用懒惰匹配，则为“.*?”
###“+”：与*类似的符号+，表示的则是1个或更长。*表示的任意长度包括0，也就是没有数字的空字符也会被匹配出来。
###“?”：字符重复零次或一次
###“{n}”：字符重复n次
###“{n,}”：字符重复n次或更多次
###“{n,m}”：重复n到m次

###表示任意长度的数字，就可以用[0-9]*或者\d*
###匹配出所有的数字串，应当用[0-9]+或者\d+
###要限定长度，就用{}代替+，括号里写上想要的长度。比如11位的数字：\d{11}
###想要再把第一位限定为1，就在前面加上1，后面去掉一位：1\d{10}


#-----正则表达式练习1----
###要求：从下面一段文本中，匹配出所有s开头，e结尾的单词。
##import re
##text='site sea sue sweet see case sse ssee loses'
##m=re.findall(r'\bs\S*?e\b',text)
##if m:
##     print(m)
##else:
##    print('not match')
#-----正则表达式练习1结束----

#-----正则表达式练习2----
##要求：写一个正则表达式，能匹配出多种格式的电话号码，包括(021)88776543   010-55667890  02584453362    0571 66345673
####import re
####text='写一个正则表达式，能匹配出多种格式的电话号码，包括(021)88776543, 格式塔 010-55667890,02584453362,0571 66345673,(02188776543,1234,0123456,0122334544323232'
####m=re.findall('[(]?0\d{2,3}[-) ]*\d{8}|\d+',text)#我的回答
######m=re.findall('\(?0\d{2,3}[-) ]?\d{7,8}',text)#官方答案
####
####if m:
####    print(m)
####else:
####    print('not match')
    
##m=re.findall('\(0\d{2,3}\)\d{7,8}|0\d{2,3}[- ]?\d{7,8}|\d+',text)#完善版答案  其实不完善
    
#进一步完善：这个表达式虽然能匹配出所有正确的数据（一般情况下，这样已经足够），但理论上也会匹配到错误的数据。
#因为()应当是成对出现的，表达式中对于左右两个括号并没有做关联处理，例如(02188776543这样的数据，我们不想要，但也会被匹配出来
#可以把()的情况单独分离出来，用"|"连接的两个表达式,正则表达式变为：\(0\d{2,3}\)\d{7,8}|0\d{2,3}[ -]?\d{7,8}
#使用“|”时，要特别提醒注意的是不同条件之间的顺序。匹配时，会按照从左往右的顺序，一旦匹配成功就停止验证后面的规则
#假设要匹配的电话号码还有可能是任意长度的数字（如一些特殊的服务号码），你应该把|\d+这个条件加在表达式的最后。如果放在最前面，某些数据就可能会被优先匹配为这一条件。
    
#----正则表达式练习2结束----

#----正则表达式结束----
