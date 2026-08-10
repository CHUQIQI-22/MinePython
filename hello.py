
# ============================================
# Python 基础练习合集
# 涵盖：循环、字符串操作、密码检查、字典、BMI
# ============================================

# ===== 猜数字游戏 =====
# 预设目标数字为 3，用户循环输入猜测，直到猜中为止
flag = True
inputNum = 3
while flag:
    inputNum = int(input("请输入数字："))
    if inputNum == 3:
        print("猜对了")
        flag = False           # 猜中后退出循环
    elif inputNum > 3:
        print("太大了")
    else:
        print("太小了")

# ===== 字符串操作 =====
# 统计字母 'e' 的出现次数，并将字符串转为大写
s = input("请输入一句话：")
print(f"e在句子中出现的次数：", s.count("e"))   # 统计字符 'e' 出现次数
print(s.upper())                                 # 转为大写
print("\n")

# ===== 密码强度检查 =====
print("密码强度检查")
password = input("请输入密码")
sc = list(password)      # 将字符串转为字符列表（此行未使用，可能是预留）
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("密码符合要求：包含了数字且长度大于8")
else:
    print("密码长度要大于8且包含数字")

# ===== 字典操作 =====
# 创建学生信息字典，访问并添加新字段
student = {"name": "zhuaizhuai", "age": 5, "city": "suzhou"}
print(student["name"], student["age"])      # 访问字典中的值
student["hobby"] = "吃猫条"                  # 添加新的键值对
print(student)                               # 打印字典

# ===== BMI 计算函数 =====
# 定义函数计算身体质量指数
h = float(input("请输入身高（m）："))
w = float(input("请输入体重（kg）："))

def bmi(h, w):
    """根据身高(m)和体重(kg)计算 BMI = 体重/身高²"""
    result = w / h ** 2
    return result

v = bmi(h, w)
print(f"BMI={v:.1f}")

#PythonDraw.py
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("blue")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()




