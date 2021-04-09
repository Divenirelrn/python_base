import random

#0~1之间的随机实数
print(random.random())
#制定区间的随机实数
print(random.uniform(1.1, 3.5))
#0~1之间的随机整数
print(random.randint(1, 10))
#从序列中随机选择一个
print(random.choice("i love xiaojun"))
#随机打乱序列
a = [1,2,3,4,5]
random.shuffle(a)
print(a)

#随机数种子
for i in range(10):
    random.seed(0) #每次产生的随机数序列相同
    random.random()