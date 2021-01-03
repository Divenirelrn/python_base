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