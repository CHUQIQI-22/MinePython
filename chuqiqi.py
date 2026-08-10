# ============================================
# 初期 Python 练习合集
# 涵盖：变量、字符串格式化、列表操作、循环
# ============================================

# =================== 第一周 ===================
print("第一周")

# 定义猫咪信息变量
name = "拽拽"       # 猫咪名字
age = "5"            # 年龄
aihao = "吃猫条"     # 爱好

# 使用逗号分隔打印多个变量
print("我叫", name, "今年", age, "岁", "喜欢", aihao)
print("\n")

# 打印三角形图案
print("  *")
print(" ***")
print("*****")
print("\n")

# 打印乘法口诀表（部分）
print("1*1=1")
print("1*2=2", "2*2=4")
print("1*3=3", "2*3=6", "3*3=9")
print("1*4=4", "2*4=8", "3*4=12", "4*4=16")
print("1*5=5", "2*5=10", "3*5=15", "4*5=20", "5*5=25")
print("\n")


# =================== 第二周 ===================
print("第二周")

# 使用 f-string 格式化输出名片
name1 = "拽拽"       # 猫咪名字
age1 = 5             # 年龄（整数类型）
city = "苏州"        # 所在城市
hobby = "吃猫条"     # 爱好
print("=====猫猫名片=====")
print(f"姓名：{name1}")
print(f"年龄：{age1}")
print(f"城市：{city}")
print(f"爱好：{hobby}")
print(f"明年就{age1 + 1}岁啦")  # f-string 支持表达式计算
print("\n")

# BMI 计算器：输入体重(kg)和身高(m)，计算身体质量指数
tz = float(input("请输入体重(kg): "))     # 体重，转换为浮点数
sg = float(input("请输入身高(m): "))      # 身高，转换为浮点数
BMI = tz / sg ** 2                        # BMI = 体重 / 身高²
print(f"身高：{sg}")
print(f"体重:{tz}")
print(f"BMI:{BMI}")
print("\n")

# 温度转换：摄氏温度 → 华氏温度
HS = float(input("请输入华氏温度（℃）"))   # 输入摄氏温度
SS = HS * 9 / 5 + 32                       # 转换公式：℉ = ℃ × 9/5 + 32
print(f"{HS}℃ ={SS}℉")


# =================== 第三周 ===================
print("=====我的书单====")

# 创建书单列表并遍历打印
books = ["shu1", "shu2", "shu3"]
for book in books:
    print(book)

# 列表操作：追加元素和删除元素
books.append("shu4")     # 在末尾添加 "shu4"
print("添加shu4后：", books)
del books[1]             # 删除索引为 1 的元素（"shu2"）
print("删除后：", books)

# 计算一组分数的总分和平均分
scs = [55, 65, 75, 86, 99]   # 分数列表
total = 0
for a in scs:
    total = total + a         # 累加每个分数
    # total += a              # 简写形式（等效于上句）
print("总分：", total)
print("平均分：", total / len(scs))
