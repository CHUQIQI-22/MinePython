# ============================================
# 复习练习合集（第六周 ~ 第七周）
# 涵盖：字符串操作、字典、函数、猜数字
# ============================================

# ================= 第六周 =================

# 字符串操作：统计字符出现次数并转为大写
value = input("请输入一段文字：")
print(f"a出现次数：", value.count("a"))   # 统计字母 'a' 的出现次数
print(value.upper())                       # 将字符串全部转为大写

# 密码强度检查：要求长度 >= 8 且包含至少一个数字
password = input("请输入密码：")
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("密码符合要求：包含数字且长度大于8")
else:
    print("密码需要包含数字且长度大于8")

print("\n")

# ================= 第七周 =================

# 字典操作：创建学生信息字典，增删改查
student = {"name": "zhuaizhuai", "age": "5", "city": "suzhou"}
print(student["name"], student["age"])      # 通过键访问字典值
student["hobby"] = "吃猫条"                  # 新增键值对
print(student)                               # 打印完整字典

# 字符频率统计：遍历字符串，统计每个字符出现的次数
value = input("请输入一段文字：")
zd = {}                                      # 空字典，用于存储字符→次数映射
for char in value:
    if char in zd:                           # 如果字符已在字典中
        zd[char] = zd[char] + 1              # 次数 +1
    else:                                    # 如果字符首次出现
        zd[char] = 1                         # 初始化为 1
print(zd)

# BMI 计算函数：根据身高(m)和体重(kg)计算身体质量指数
def bmi(h, w):
    """计算 BMI 值，公式：体重(kg) / 身高(m)²"""
    result = w / h ** 2
    return result

h = float(input("请输入身高（m）："))
w = float(input("请输入体重（kg）："))
v = bmi(h, w)
print(f"BMI={v:.1f}")

# 闰年判断函数：能被 4 整除但不能被 100 整除，或能被 400 整除
def greet(year):
    """判断给定年份是否为闰年"""
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "是闰年"
    else:
        return "不是闰年"

value = int(input("请输入年份："))
print(greet(value))

# 猜数字游戏：用户输入数字与预设值比较，猜中为止
flag = True
value = int(input("请输入一个数字："))
sc = 5                                       # 预设目标数字

def greet(value):
    """比较输入值与目标值，返回提示信息"""
    if value == sc:
        return "猜对了"
    if value > sc:
        return "太大了"
    else:
        return "太小了"

print(greet(value))

# 循环直到猜中为止
while flag:
    if value == sc:
        flag = False                         # 猜中后退出循环
    else:
        # 注意：此处缺少重新输入的逻辑，猜测是需要补充 value = int(input(...))
        pass


#这是一行注释

