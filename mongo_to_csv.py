from pymongo import MongoClient

# 创建MongoDB连接
client = MongoClient('mongodb://localhost:27017/')

# 选择数据库和集合
db = client['mydatabase']
collection = db['megnet_dielectric']

# 检索集合中的所有文档
documents = collection.find()

# 遍历文档并打印数据
for document in documents:
    mae = float(document['MAE'])
    mape = float(document['MAPE'])
    rmse = float(document['RMSE'])
    print(f"MAE: {mae}, MAPE: {mape}, RMSE: {rmse}")

# 关闭MongoDB连接
client.close()
