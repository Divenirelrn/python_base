a = {1: "liruonan", 2: "lixiaokou", 3: "xiaojun"}

#查找
print(a.get(1))
print(a.get(5, "not found"))

print(1 in a)

#删除
a.pop(1)
print(a)

#拷贝
b = a.copy() #浅拷贝（只拷贝第一层）
print(b)

#清除
a.clear()
print(a)

#排序
key_value = {}
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

key_value = sorted(key_value.items(), key=lambda x: x[1], reverse=True)
print(key_value)