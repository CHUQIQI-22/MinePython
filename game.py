# import random
# answer = random.randint(1,10)
# counts=3
# _4555counts = 3
# while counts>0:
#     temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
#     guess = int(temp)
#     if guess == answer:
#         print("你是小甲鱼心里的蛔虫嘛？！")
#         print("哼，猜中了也没奖励！")
#         break
#     else:
#         if guess > answer:
#             print("大了")
#         else:
#             print("小了")
#     counts = counts - 1
# print("游戏结束，不玩啦^-^")

print("'")
print("xxxxx'\\")
#
a = 1
while a < 10:
    b = 1
    while b <= a:
        print(a,"*",b,"=",a*b, end=" ")
        b += 1
    print()
    a += 1

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,"*",x,"=",n//x,end=" ")
            break
    else:
        print(n,"是一个素数")
print("\n")
A = [0] * 3
print(A)
for n in range(3):
    A[n]= [0] * 2
print(A)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = [n[1] for n in matrix]
print(x)

words = ["greet","fishc","brilliant","excellent","fantasitic"]
s = [i for i in words if i[0] =="f" ]
print(s)

s="上海自来水上海"
t=s.find("海")
print(t)
a=s.rfind("海")
print(a)

x = [1,2,3,4,5]
del x[:]
print(x)

