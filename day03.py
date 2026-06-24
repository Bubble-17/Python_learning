#练习1：基本判断
score=85
if score>=90:
    print("优秀")
elif score>=80:
    print("良好")
elif score>=60:
    print("及格")
else:
    print("需要加油")
#练习2：判断列表里有没有某人
names=["张三","李四","田娇"]
if "田娇" in names:
    print("找到了！")
#下面是自主练习环节
#创建5个学生成绩
scores={"张三":87, "李四":92,"王五":56,"赵六":60,"田娇":97}#请注意:一定要是英文符号这里{}不能丢
#判断每个人是否及格
for name,score in scores.items():#for in语句循环遍历列表
    if score>=90:#if判断:结尾
        print(name+"优秀")
    elif score>=80:#多个层级用elif与if平级，最后一个用else涵盖其他
        print(name+"良好")
    elif score>=60:
        print(name+"及格")
    else:
        print(name+"不及格")
