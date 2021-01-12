import os
import sys


#os._exit()强制退出,之后的代码不会被执行，异常也不能捕获
# try:
#     os._exit(0)
# except:
#     print("error")
# finally:
#     print("os exit")

#sys.exit(0)，y异常能够捕获
try:
    sys.exit(0)
except:
    print("end")
finally:
    print("sys exit")


#exit()与quit()一般在交互式shell中使用
exit()
quit()