a = {1: "liruonan", 2: "lixiaokou", 3: "xiaojun"}

#查找
print(a.get(1))
print(a.get(5, "not found"))

print(1 in a)

#删除
a.pop(1)
print(a)

#拷贝
b = a.copy()
print(b)

#清除
a.clear()
print(a)