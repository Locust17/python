# 通过编写程序来获取互联网上的资源
# 百度
# 用程序来模拟浏览器，通过输入一个网址，从该网址中获取到资源或者内容
# python拟定以上需求，特别简单

#一
#爬虫入门1
# from urllib.request import urlopen
#
# url = "http://www.baidu.com"
# resp = urlopen(url)
#
# #print(resp.read())
# print(resp.read().decode("utf-8"))

#泡虫入门2
from urllib.request import urlopen
url = "http://www.baidu.com"
resp = urlopen(url)

with open("mybaidu.html", mode="w") as f:
    f.write(resp.read().decode("utf-8"))
print("over!")

#爬虫入门3
# 1.服务器渲染:在服务器那边直接数据和html集合在一起，统一返回给浏览器
#   在页面源代码中能看到数据
# 2.客户端渲染：
#   第一次请求只有返回一个html骨架，第二次请求拿到数据，进行数据显示
#   在页面源代码中，看不到数据

#熟练使用浏览器抓包工具
#http协议  robots.txt君子协议

#请求

#响应

#请求头和响应有重要内容
