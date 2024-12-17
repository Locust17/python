#---------------------------------------------------------------
# # 练习4
# import requests
#
# url = "https://jwc.cqrk.edu.cn/"
#
# dic = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
#
# }
#
# pest = requests.get(url, headers=dic)
# print(pest.text)
# pest.close() #关闭pest

#--------------------------------------------------------
#数据解析概述
#1.re解析
#2.bs4解析
#3.xpath解析

#正则表达式
#语法：使用元字符进行排列组合用来匹配字符串，在线网址：https://tool.oschina.net/regex/
#元字符：具有固定意义的特殊符号

'''
.
\w
\s
\d
\n
\t

^
$

\W
\D
\S
a|b
()
[...]
[^...]

.*   #写爬虫用的最多的就是这个惰性匹配
.*?

#我的电话是：10010，syllar的电__话是：10086
#正则表达式:[^a-zA-Z0-9_]\W


1.玩儿.*？游戏
玩儿吃鸡游戏

2.玩儿.*游戏
玩儿吃鸡游戏，晚上一起上游戏，干嘛呢？打游戏

#------------
<div class="jay">周杰伦</div><div class="jj">林俊杰</div>
<div class=".*?">(.*?)</div>
共找到 2 处匹配：
<div class="jay">周杰伦</div>
<div class="jj">林俊杰</div>


dashfdjuoeurioqnmxcvxz/
.*?x
共找到 2 处匹配：
dashfdjuoeurioqnmx
cvx

'''

#正则会写了，那么在python程序中如何使用正则呢？答案就是re模块
#记住re模块的几个功能

import re
#1.findall
list = re.findall(r"\d+","我的电话是：10010，syllar的电__话是：10086")
print(list)

it = re.finditer(r"\d+","我的电话是：10010，syllar的电__话是：10086")
#print(it) #<callable_iterator object at 0x000002096872A530>
for i in it:
    print(i.group())
#2.search
s = re.search(r"\d+","我的电话是：10010，syllar的电__话是：10086")
print(s.group())
#3.match
s = re.match(r"\d+","我的电话是：10010，syllar的电__话是：10086")
print(s.group())  #未显示
#4.finditer
#5.compile()

#预加载正则表达式
obj = re.compile(r"\d+")

ret = obj.finditer("我的电话是：10010，syllar的电__话是：10086")
for i in ret:
