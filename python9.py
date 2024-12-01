#从一个数循环到另一个，使用range
# for i in range(111111,211111):
#     print(i)

#------------访问文件，并且寻找png的文件
# #for f in files if 'fish' in f ...
# import os
# path = "D:\\DHCP" # 这里的 `r` 前缀表示原始字符串，避免反斜杠被转义，将 `你的用户名` 替换成真实用户名
# # #path = r'D:/DHCP'
# # path = r"D:\DHCP"
# files = os.listdir(path)
# print(files)
#
# for f in files:
#     if 'IMG' in f and f.endswith('.jpg'):  #两种判断一种是这个在不在f，另一种判断是.jpg结尾
#         print('Found it!' + f)
#         #os.startfile(r'D:\DHCP\IMG_20240523_114548.jpg') #打开文件函数
#         os.startfile("D:\\DHCP\\"+f)  #将查找的文件，以及前置地址拼接打开
#
# #未显示

#----------------------------------------------------------------------------------

#模糊搜索文件

import os
part = os.listdir("C:\\Users\\xiao\\Desktop")
print(part)
print("\n")

for f in part:
    if ('b' in f or 'xss' in f or 'os' in f )and (not f.endswith('.png')):  #1.需要元组括号括起来，2.每一句的or都需要一个完整的判断：'os' in f or 'b' in f or 'xss' in f
        print("D:\\Users\\xiao\\Desktop\\"+f)
        
        
#-----------------------------------------
