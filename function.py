#函数传参

#传入基本类型
def change_int(a):
    a = 20
    print(id(a))

a = 10
print(id(a))
change_int(a)
print(a)

#传入list
def change_list(l):
    l[0] = 100
    print(id(l))

l = [10,20,30,40,50]
print(id(l))
change_list(l)
print(l)

#传入dict
def change_dict(d):
    d[1] = 100
    print(id(d))

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print(id(d))
change_dict(d)
print(d)

#传入object
class Person:
    def __init__(self):
        self.age = 10

def chageObj(obj):
    obj.age = 20
    print(id(obj))

p = Person()
print(id(p))
chageObj(p)
print(p.age)


