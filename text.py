# num1 = input("请输入第一个整数：")
# num2 = input("请输入第二个整数：")
# if num1 < num2:
#     print("第一个数比第二个数小")
# if num1 > num2:
#     print("第一个数比第二个数大")
# if num1 == num2:
#     print("第一个数和第二个数一样大")


# if num1 < num2:
#     print("第一个数比第二个数小")
# elif num1 > num2:
#     print("第一个数比第二个数大")
# else:
#     print("第一个数和第二个数一样大")

# while True:
#     print("ilovefishc")
#     break


a = 0
while a != "e":
    a=(input("请输入成绩："))
    if a == "e":
        break
    sc=int(a)
    if sc < 60:
        print("D")
    if 60 <= sc < 80:
        print("C")
    if 80 <= sc < 90:
        print("B")
    if 90 <= sc < 100:
        print("A")
    if sc == 100:0
        print("S")
