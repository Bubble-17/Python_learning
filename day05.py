#练习1:定义一个函数
def say_hello(name):
    print("你好，"+name+"!")
say_hello("田娇")
say_hello("张三")

#练习2：有返回值的函数
def add(a,b):
    return a-b
result=add(3,5)
print(result)

#计算平均分
def get_average(scores):
    total=sum(scores)
    return total/len(scores)
scores=[85,90,78,92]
print("平均分："+str(get_average(scores)))

#练习时间
def check_score(score):
    if score >=90:
        print("优秀")
    elif score >=75:
        print("良好")
    elif score>=60:
        print ("及格")
    else:
        print("不及格")
check_score(98)
check_score(76)
check_score(54)#我靠！！田娇，你真厉害。我刚才自己写出来的代码，唯一的问题是没有缩进，以及if,elif,else后面用：而不是，
#仅此格式问题。切记，if,elif,else语句用：结尾。且语句结束下一行要缩进
#真的很棒，晚安田娇。明天早上8点要起来给永丽代课。C’est le vie!
