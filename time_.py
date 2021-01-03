import time

print(time.localtime())
print(time.asctime())
print(time.ctime())

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))