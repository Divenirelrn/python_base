a = [1,2,3,4,5,6]
#排序
print(sorted(a))
print(list(reversed(a)))

#数值特征
print(sum(a))
print(max(a))
print(min(a))

#组合
print(dict(zip(a, range(6))))
print(list(enumerate(a)))

#map & filter
print(list(map(lambda x: x * 2, [1,2,3,4,5])))
print(list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8,9])))

#all&any
a = [0, False, "", 0, 0, 0]
print(any(a)) #只有全部为False，才返回False
#if any i == 0 for i in a
any(i == 0 for i in a)

a = [1, True, "a", 1, 1, 1]
print(all(a)) #只有全为True，才返回True
#if all i == 0 for i in a
all(i == 0 for i in a)

#强制类型转换
int('10')
int('110011', 2)
str()
bin()