#-------------------------------------------------------正则表达式单独提取
# import re
#
# s = """
#     <div class='jay'><span id='1'>郭麒麟</span></div>
#     <div class='jj'><span id='1'>宋铁</span></div>
#     <div class='jolin'><span id='1'>大聪明</span></div>
#     <div class='sylar'><span id='1'>范思哲</span></div>
#     <div class='tory'><span id='1'>胡说八道</span></div>
# """
#
# #(?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
# obj = re.compile(r"<div class='.*?'><span id = '(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>", re.S) #re.S  让.能匹配换行符
#
# result = obj.finditer(s)
# for it in result:
#     print(it.group("wahaha"))
#     print(it.group("id"))      #无显示

import re
import requests
import csv
url = "https://movie.douban.com//chart"

headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"

}
resp = requests.get(url,headers=headers)
# print(resp.text)
page_content = resp.text

# #解析数据
obj = re.compile(r'<div class="">.*?<a href="https://move.douban.com/subject/36727829" class="">(?P<name>.*?)'
                 r'.*?<span style="font-size:13px;">.*?<span class="rating_nums">(?P<mun>.*?)</span><span class="p1">(?P<people>)人评价</span>', re.S)

result = obj.finditer(page_content)
f = open("data.csv",mode="w")
csvwriter = csv.writer(f)
for it in result:
    dic = it.groupdict()
    # dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
f.close()
print("over")
