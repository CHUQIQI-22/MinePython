


flag=True
inputNum=3
while flag:
    inputNum=int(input("请输入数字："))
    if inputNum==3:
        print("猜对了")
        flag=False
    elif inputNum>3:
        print("太大了")
    else:
        print("太小了")
s=input("请输入一句话：")
print(f"e在句子中出现的次数:",s.count("e"))
print(s.upper())
print("\n")



print("密码强度检查")
password=input("请输入密码")
sc=list(password)
if len(password)>=8:
    if "0" in sc or "1" in sc or "2" in sc or "3" in sc or "4" in sc or "5" in sc or "6" in sc or "7" in sc or "8" in sc or "9" in sc:
        print("密码强度高")
    else:
        print("密码需包含数字")
else:
    print("密码长度要大于8且包含数字")

student={"name":"zhuaizhuai","age":5,"city":"suzhou"}
print(student["name"],student["age"])
student["hobby"]="吃猫条"
print(student)

h=float(input("请输入身高（m）："))
w=float(input("请输入体重（kg）："))
def bmi(h,w):
    result=w/h**2
    return result
v=bmi(h,w)
print(f"BMI={v:.1f}")




