import pickle

#Python 中pickle出现 ascii’ codec can’t decode byte 0xe4 in position 0: ordinal not in range(128) 解决方法
#bin文件中包含图片的数据
pickle.load(open(bin_path, "r"), encoding='bytes')
#bin文件中包含字符串数据
pickle.load(open(bin_path, "r"), encoding='latin1')