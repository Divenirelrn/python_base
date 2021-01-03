import os

# print(os.getcwd())
# os.chdir("D://")
# print(os.getcwd())
#
# #创建路径
# os.mkdir()
# os.makedirs()
# #删除路径
# os.remove()
# os.rmdir()
# os.removedirs()
#
# #重命名
# os.rename()
#
# #os.path
# import os.path as osp
# osp.realpath()
# osp.abspath()
# osp.dirname()
# osp.basename()
# osp.splitext()
# osp.exists()
#osp.isdir()
# osp.getsize()
# for root, dirs, files in os.walk("./container"):
    # print(root)
    # print(dirs)
    # print(files)

# import glob
# for i in glob.glob("*.py"):
#     print(i)

from pathlib import Path
import os

print("abspath", os.path.abspath("."))
print("realpath", os.path.realpath("."))
cur = Path.cwd()
path = Path(cur)
path = path / "os_.py"
print(path.parts)
print(path.parent)
print(path.name)
print(path.suffix)
print(path.stem)
print(path.exists())
print(list(path.parent.glob(".py")))
print(path.is_dir())
print(path.is_file())
for i in path.parent.iterdir():
    print(i)

(path.parent / "test").mkdir(parents=True)
(path.parent / "test").rename(path.parent / "test1")

path.rmdir()
