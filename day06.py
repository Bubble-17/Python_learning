#学生成绩管理器
def check_level(score):
    """判断等级"""
    if score>=90:
        return"优秀"
    elif score>=80:
        return"良好"
    else:
        return "不及格"
def get_average(scores):
    """计算平均分"""
    return sum(scores)/len(scores)
#学生数据
students=[
    {"name":"张三","english":92,"math":88},
    {"name":"李四","english":75,"math":80},
    {"name":"王五","english":58,"math":65},
    {"name":"田娇","english":95,"math":90}]
print("=======学生成绩报告=======")
for s in students:
    avg=get_average([s["english"],s["math"]])
    level=check_level(avg)
    print(s["name"]+"|英语:"+str(s["english"])+"|数学:"+str(s["math"])+"|均分:"+str(avg)+
    "|等级:"+level)
#全班平均分
all_avg=get_average([get_average([s["english"],s["math"]])for a in students])
print("\n全班平均分:"+str(all_avg))
#今天这个好难，我基本都是照着参考打的。明天早上8点半到10点都在上课，一节润泽的一节帮永丽代的。
#加油田娇，晚安爱你 现在把今天的雅思单词再过一遍就睡觉了



