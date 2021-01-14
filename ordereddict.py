from collections import OrderedDict


a = OrderedDict()
a[0] = "a"
a[1] = "b"
a[2] = "c"
print(a)

a = {0: "c", 1: "b", 2: "a"}
b = OrderedDict(a)
print(b)
c = OrderedDict(sorted(a.items(), key=lambda x: x[1]))
print(c)
