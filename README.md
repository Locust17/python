# python

# a = 1
# b = 2
# c = "hello world"
# d = "重庆人文科技学院"
# e = "信息安全"
# f = "Hello World"
# g = "HELLO WORLD"
# h = 1.1
# i = 1.6
# k = 1.5
# m = 1.0
# n = 2.2
#
# print(a)
# print(b)
# print(a + b)
# print(m / a)
# print(b // h)
#
# print(c)
# print(c[4])
# print(c[2:5])
#
# print(d)
# print(e)
# print(d + e)
#
# print(f)
# print(g)
# print(f + g)
# print("hel\\lo wo\nrld")

# string1 = "我是第一个字符串"
# print(string1[0:4])

#define sum1 = a sum2 = b

# #加法
# def get_sum(sum1,sum2):
#     result = sum1 + sum2
#     return result
#
# # a = 1
# # b = 3
# # c = a + b
# # print(c)
#
# print(get_sum(2,3))
#
# print(get_sum(sum1= 3,sum2= 5))

#-----------------------------------------------------------------------

# class Person:
#     def __init__(self,name,height,weight):
#         self.name = name
#         self.height = height
#         self.weight = weight
#
#     def say_name(self):
#         print("我的名字叫"+self.name)
#
#     def say_hello(self,terget_name):
#         #print("我叫"+self.name+",很高兴认识你"+terget_name)
#         print("我叫"+self.name+",很高兴认识你"+terget_name)
#
# person1 = Person("老张",170,100)
# person2 = Person("老王", 160,80)
#
# person1.say_hello("老邓")
# person1.say_name()
# person2.say_name()


#----------------------------------------------------------------------------------------

# a = 7.0
# # 1 == 1.0
#
# b = 3
#
# print(int(a))
#
# #Number
# # int(integer)
# # float
# # complex

#-----------------------------------------------
# import math
# a = -2.6
# b = 2.6
# c = 2.4
# # abs absolute  绝对值
# print(abs(a))

# round     四舍五入
# print(round(a))
# print(round(b))
# print(round(c))
#
# #pow         指数
# print(pow(a,2))
# print(pow(b,3))
#
# # ceil        向上取整
# print(math.ceil(a))
# print(math.ceil(b))
#
# # floor       向下取整
# print(math.floor(a))
# print(math.floor(b))
#
# -----------------------------------

# string1 = "hello world"
#
# #len length 长度
# print(len(string1))
#
# # capitalize
# print(string1.capitalize())
#
# # upper        全部大写
# print(string1.upper())
#
# #lower
# print(string1.lower())
#
# # replace    替换
# print(string1.replace("world","worldasdasdasdsad"))
#
# #find
#
# print(string1.find("hello"))
#
#
# --------------------------------------

#
# # boolean 布尔
# a = True
# b = False
#
# string1 = "HELLO WORLD!"
# string2 = "hello WORLD!"
#
# #isupper  判断是否全部大写
# print(string1.isupper())
# print(string2.isupper())
#
# def get_sum(num1,num2 = 4):
#     return num1 + num2
#
# print(get_sum(1,6))
# print(get_sum(1))
#
# string1 = "hello world!"
#
# # split 切割
# print(string1.split('o'))
# # endswith 判断字符是否为指定单词结束
# print(string1.endswith("worl"))   # False
# print(string1.endswith("world!"))  # True


# #------------------------------------------
#
# #加法函数
# def Add(num1,num2):
#     return num1 + num2
# #减法函数
# def Subtraction(num1,num2):
#     return num1 - num2
# #乘法函数
# def Muktiplication(num1,num2):
#     return num1*num2
# #除法函数
# def Division(num1,num2):
#     return num1/num2
# #整除法函数
# def Divisible_method(num1,num2):
#     return num1//num2
# #取余函数
# def Take_remainder(num1,num2):
#     return num1%num2
# print(Add(4,2))
# print(Subtraction(4,2))
# print(Muktiplication(4,2))
# print(Division(4,2))
# print(Divisible_method(7,2))
# print(Take_remainder(7,2))
#-------------------------------------------------------
'''
def Add_more(num1,num2,num3,num4):
    return num1+num2+num3+num4
print(Add_more(1,2,3,4))

def multiple(num1,mul1):
    i = 0
    num11 = num1
    for(i=0;i<mul1;i++)
        num11 = num11*num1
    return num11
print(multiple(2,3))
'''

class Person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

    def say_name(self):
        print("我的名字叫"+self.name)

    def say_hello(self,target_name):
        print("我叫"+self.anme+",很高兴认识你"+target_name)

person1 = Person("老张",170,100)
person2 = Person("老王",11600,80)

person1.say_hello("老邓")
person1.say_name()
person2.say_name()
