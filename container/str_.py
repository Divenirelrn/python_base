a = "sdgGFdsfh"
#大小写转换
a = a.capitalize()
print(a)
a = a.casefold() #包含其他语言时同样有效
print(a)
a = a.lower() #只作用于中英文
print(a)
a = a.upper()
print(a)

#判断
print(a.startswith("S"))
print(a.endswith("H"))

#索引
print(a.count("S"))
print(a.index("S"))
print(a.find("S"))

#编码
print(a.encode("utf-8"))

#替换
print(a.replace("S", "K"))

#分割
print(a.split()) #字符串转化为列表
print(a.splitlines())

#转义
print("\\")
print("\ta")

#format
print("%10.2f" % 3.672)
print("%-10.2f" % 3.672)
print("{0},{1},{2}".format(1,2,3))
print("{a},{b},{c}".format(a=1,b=2,c=3))
print("{0:.2f}".format(5.674))
