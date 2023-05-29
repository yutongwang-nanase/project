import pymongo
from pymongo import MongoClient
import csv
# 创建MongoDB连接
client = pymongo.MongoClient("mongodb://root:9lWxJysyKUUBvC!@120.46.186.160:27017/")
# 选择数据库
db = client['mydatabase']

# 选择或创建集合
collection = db['megnet_phonons']


# 打开CSV文件
with open('megnet_phonons.csv', 'r') as file:
    reader = csv.DictReader(file)

    # 遍历CSV文件的每一行
    for row in reader:
        # 在集合中插入一行数据
        collection.insert_one(row)
# 关闭MongoDB连接
client.close()
