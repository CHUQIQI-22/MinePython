from asyncio import print_call_graph

print("第一周")
#第一周内容
name="拽拽"
age="5"
aihao="吃猫条"
print("我叫", name, "今年", age, "岁", "喜欢", aihao)
print("\n")
print("  *")
print(" ***")
print("*****")
print("\n")
print("1*1=1")
print("1*2=2","2*2=4")
print("1*3=3","2*3=6","3*3=9")
print("1*4=4","2*4=8","3*4=12","4*4=16")
print("1*5=5","2*5=10","3*5=15","4*5=20","5*5=25")
print("\n")



print("第二周")
#第二周内容
name1="拽拽"
age1=5
city="苏州"
hobby="吃猫条"
print("=====猫猫名片=====")
print(f"姓名：{name1}")
print(f"年龄：{age1}")
print(f"城市：{city}")
print(f"爱好：{hobby}")
print(f"明年就{age1+1}岁啦")
print("\n")
#BMI计算
tz=float(input("请输入体重(kg): "))
sg=float(input("请输入身高(m): "))
BMI=tz/sg**2
print(f"身高：{sg}")
print(f"体重:{tz}")
print(f"BMI:{BMI}")
print("\n")
#温度转换
HS=float(input("请输入华氏温度（℃ )"))
SS=HS*9/5+32
print(f"{HS}℃ ={SS}℉ ")
#第二周内容

#第三周内容
print("=====我的书单====")
books=["shu1","shu2","shu3"]
for book in books:
    print(book)
books.append("shu4")
print("tianjiashu4",books)
del books[1]
print(books)

scs=[55,65,75,86,99]
total=0
for a in scs:
    total=total+a
    #total += a
print("zongfen",total)
print("pjf",total/len(scs))


    
#第三周内容
