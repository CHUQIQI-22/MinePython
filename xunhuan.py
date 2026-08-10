# ============================================
# 文件行数统计脚本
# 读取 todo.txt，统计行数和字符总数
# ============================================

lines = 0            # 行数计数器
totalCount = 0       # 总字符数计数器

# 以只读模式打开 todo.txt 文件
with open("todo.txt", "r", encoding="utf-8") as f:
    # 逐行读取文件内容
    for line in f:
        print(line)                       # 打印每一行内容
        lines += 1                        # 行数 +1
        totalCount += len(line.rstrip())  # 去除末尾换行符后累计字符数

# 输出统计结果：总行数 和 总字符数（不含换行符）
print("行数：", lines, "总字符数：", totalCount)
