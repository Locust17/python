#---------------------------------------
#豆瓣电影
#客户端映射
#客户端发起请求，服务端相应一个html框架。再次请求时，返回数据

#pip install requests
#国内源

#1
# import requests
# query = input("输入一个你喜欢的明:")
# url = "https://cn.bing.com/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6"
#
# dic = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
# }
#
# resp = requests.get(url,headers=dic) #处理一个小小的反爬
# #print(resp) #直接返回200
# print(resp.text)#拿到页面源代码

# #2----get请求
# import requests
# query = input("输入一个你喜欢的明:")
# url = "https://sogou.com/web?query={query}"
#
# dic = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
# }
#
# resp = requests.get(url,headers=dic) #处理一个小小的反爬
# print(resp) #直接返回200
# print(resp.text)#拿到页面源代码

# #3------post请求
# import requests
#
# url = "https://fanyi.baidu.com/mtpe-individual/multimodal#/"  #翻译网络地址有问题
#
# s = input("请输入你所要翻译的单词:")
# dat = {
#     "kw": s
# }
# # 发送post请求，发送的数据必须放在字典里面，通过data参数进行传递
# resp = requests.post(url,data=dat)
# #print(resp.text)
# print(resp.json()) #将服务器返回的内容直接处理成json() ==> dic
#
