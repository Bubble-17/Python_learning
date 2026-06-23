#练习1：创建一个列表
students="张三","李四","王五","田娇"
print(students)#print后面紧跟()
#练习2：取出列表中的某一个（注意：从0开始数）
print(students[0])#第1个，排序的时候用上[]
print(students[1])#第2个
#练习3：用for循环遍历列表
for name in students:#for语句以:结尾，不要忘记:
    print(name+"同学你好")
#练习4：遍历数字范围
for i in range(1,6):#这个i可以随意更换其他字母，后面随之更换即可
    print("第"+str(i)+"次练习")
#下面是自主练习
lists="《外面是夏天》","《醒来的女性》","《第二性》","《生而为人》","《一间自己的房间》"
#我发现分隔符是,列举的时候请用""和,表示一个单位
print(lists)
print(lists[0])
print(lists[1])
for name in lists:#for in 语句
    print("我读过"+name)#+不可以省略，也不可以用and代替
for p in range(1,6):#我靠，不能是l!我以为任意字母都可以，不是的
#我查了是因为l,o长得像数字1和0，为了防止confused不让用
    print("我最近准备读的第"+str(p)+"本书")#我老是忘记str()
#句子里面包含需要执行的数字时请记得用str()把数字转化为字符
print("今天是我学习python的第2天")#这个2不需要执行，是我直接输入的所以不用str()
#晚安田娇
    
 
  

