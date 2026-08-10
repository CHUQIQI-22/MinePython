

#DaydayupQ4.py
def dayUP(df):
    dayup=1
    for i in range(365):
        if i%7 in [6,0]:
            dayup = dayup * (1-0.01)
        else:
            dayup = dayup * (1+df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是:{:.3f}".format(dayfactor))


weekStr="星期一星期二星期三星期四星期五星期六星期日"
weekId=eval(input("请输入星期数字（1-7）:"))
pos=(weekId-1)*3
print(weekStr[pos:pos+3])