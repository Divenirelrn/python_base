import pickle

# a = ["a", "b", "c", "d", "e"]
# with open("./test.pkl", "w") as fp:
#     pickle.dump(a, fp)

# with open("./test.pkl", "rb") as fo:
#     data = pickle.load(fo)
#
# print(data)

import json
# a = {1: "li", 2: "ruo", 3: "nan"}
# with open("./test.json", "w") as fp:
#     json.dump(a, fp)

# with open("./test.json", "r") as fp:
#     data = fp.read()
#
# print(data)

import csv
a = [1, "中国", 1, 0, 1]
# with open("./test.csv", "w", encoding="utf-8") as fp:
#     csv_writer = csv.writer(fp)
#     csv_writer.writerow(a)

with open("./test.csv", "r", encoding="utf-8") as fp:
    data = csv.reader(fp)
    print(list(data))

import yaml

fp = open("./config.yaml", "r")
data = yaml.load(fp, Loader=yaml.FullLoader)
fp.close()
print(data)

fo = open("./config2.yaml", "w")
yaml.dump(data, fo)
fo.close()



