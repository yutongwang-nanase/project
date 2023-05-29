import pymongo

# 连接到MongoDB数据库
client = pymongo.MongoClient("mongodb://root:9lWxJysyKUUBvC!@120.46.186.160:27017/")
db = client['mydatabase']  # 替换为实际的数据库名称
collection = db['matbench_glass_data']  # 替换为实际的集合名称

# 从数据库中获取数据
data_from_mongodb = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段


# 打印数据
print(data_from_mongodb)
# 打印转换后的数据

