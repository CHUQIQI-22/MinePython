#"""003讲"""
# print('小甲鱼常说：“good good study,day day up!"')
# print("小甲鱼常说：“good good study,day day up!\"")

# print("bruce eckel say:\"life is short ,let\'s learn python.\"")

# dpy = 365
# hpd = 24
# mph = 60
# spm = 60
# spy = dpy * hpd * mph * spm

# print(spy)
# name = input("请输入您的名字：")
# print("你好，", name)

# """004讲"""
# print(r"C:\Users\goods\Desktop")
# print("C:\\Users\\goods\\Desktop")

# print(r"""      ___                     ___          ___          ___
#      /\  \         ___       /\  \        /\__\        /\  \
#     /::\  \       /\  \     /::\  \      /:/  /       /::\  \
#    /:/\:\  \      \:\  \   /:/\ \  \    /:/__/       /:/\:\  \
#   /::\~\:\  \     /::\__\ _\:\~\ \  \  /::\  \ ___  /:/  \:\  \
# /:/\:\ \:\__\ __/:/\/__//\ \:\ \ \__\/:/\:\  /\__\/:/__/ \:\__\
# \/__\:\ \/__//\/:/  /   \:\ \:\ \/__/\/__\:\/:/  /\:\  \  \/__/
#       \:\__\  \::/__/     \:\ \:\__\       \::/  /  \:\  \
#        \/__/   \:\__\      \:\/:/  /       /:/  /    \:\  \
#                 \/__/       \::/  /       /:/  /      \:\__\
#                              \/__/        \/__/        \/__/""")

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j, "x", i, "=", j*i, end=" ")
#     print("\n")

# """005讲"""
# guess = 0
# if guess == 8:
#     print("你是小甲鱼心里的蛔虫嘛？！")
#     print("哼，猜中了也没奖励！")
# else:
#     print("猜错啦，小甲鱼现在心里想的是8！")

# num1 = int(input("请输入第一个整数"))
# num2 = int(input("请输入第二个整数"))
# if num1 > num2:
#     print("第一个数比第二个数大")
# if num1 < num2:
#     print("第一个数比第二个数小")
# if num1 == num2:
#     print("第一个数和第二个数一样大")

# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print("你已经成年啦！")
# else:
#     print("对不起，你还未成年")

# while True:
#     print("ilovefishc.com")
#     break

# while True:
#     a = input("请输入你的分数：")
#     if a == "e":
#         break
#     sc = int(a)
#     if sc < 60:
#         print("D")
#     if 60 <= sc <80:
#         print("C")
#     if 80 <= sc <90:
#         print("B")
#     if 90 <= sc <100:
#         print("A")
#     if sc == 100:
#         print("S")

# """007讲"""
# import random
# print(random.randint(1,10))
# print(random.choice("ilovefishc"))

# import random
# print(random.randrange(0,100,2))
# random.randrange() 用来从指定范围内随机取一个整数，相当于「随机版」的 range()。
# 基本语法
# 它和 range() 的参数写法完全一致，三种形式：
# python
# random.randrange(stop)              # 从 0 到 stop-1
# random.randrange(start, stop)       # 从 start 到 stop-1
# random.randrange(start, stop, step) # 从 start 到 stop-1，按 step 步进
# 返回一个随机整数，区间是 [start, stop)，也就是包含 start、不包含 stop。

# import random
# a = random.sample(range(1,34),6)
# # x = random.sample(range(1,17), 1)
# x = random.randint(1,16)
# print("开奖结果是：", *a)
# print("特别号码是：", x)


# """008讲"""
import decimal
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.3')
print(a + a + a - b)


