
a = [1,2,4,6,8]

#列表增加元素
a.append(9)
a.extend([0,3])
a.insert(0, 5)
print(a)

#列表删除元素
a.remove(8)
a.pop(3)
del a[0]
print(a)

#拼接
a += [2,3,4] #不推荐
a *= 3
print(a)

#判断
print(3 in a)

#元素操作
print(a.count(3))
print(a.index(3, 1, 9))

#排序
a.reverse()
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a = [{'name':'homer', 'age':39}, {'name':'bart', 'age':10}, {'name':'aart', 'age':20}, {'name':'aart', 'age':10}]
a.sort(key=lambda x: x["age"])
print(a)

#拷贝
b = a
print(id(b), id(a))
b = a[:] #浅拷贝
print(id(b))

#列表转化为字符串
a = ["a", "b", "c", "d", "e"] #元素必须为str类型
print("".join(a))