#练习1:创建字典（键值对）
student={"name":"田娇","age":20,"score":85}
print(student["name"])
print(student["age"])
print(student["score"])
#字典列表（工作中最常用的结构）
students=[{"name":"张三","score":90},{"name":"李四","score":75},{"name":"田娇","score":88}]
for s in students:
    print(s["name"]+"的分数是"+str(s["score"]))#括号是反过来的([{}])
#练习时间
book={"name":"我们八月见","author":"马尔克斯","process":"已读完"}
print(book["name"]) #""不可以省略
books=[{"name":"我们八月见","author":"马尔克斯","process":"已读完"},
{"name":"墓园的花要常浇水","author":"瓦莱莉.佩兰","process":"已读完"},
{"name":"飞鸟集","author":"泰戈尔","process":"未读完"}]
for b in books:
    print(b["name"]+"作者是"+str(b["author"])+str(b["process"]))
#非常棒！晚安田娇 今天教培面试很terrible，外企标注过了但是2个小时路程。
#我很纠结，可我知道我一定会去，哪怕就是去感受一下。
#晚上还临时给润泽上了一节课，我觉得给她上课很开心，希望她也这么觉得。
#虽然今天好像没什么值得庆祝开心的事，但是还是很厉害 晚安田娇




