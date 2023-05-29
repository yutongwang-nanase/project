import pymongo

# 创建MongoDB客户端
client = pymongo.MongoClient("mongodb://root:9lWxJysyKUUBvC!@120.46.186.160:27017/")

# 连接到数据库
db = client['mydatabase']

# 连接到集合（表）
collection = db['matbench_expt_gap_data']

# 要导入的数据
matbench_expt_gap_data = {

    "algorithm": [
        "Ax/SAASBO CrabNet v1.2.7",
        "MODNet (v0.1.12)",
        "CrabNet",
        "MODNet (v0.1.10)",
        "Ax+CrabNet v1.2.1",
        "Ax(10/90)+CrabNet v1.2.7",
        "CrabNet v1.2.1",
        "AMMExpress v2020",
        "RF-SCM/Magpie",
        "gptchem",
        "Dummy"
    ],
    "mean mae": [
        0.331,
        0.3327,
        0.3463,
        0.347,
        0.3566,
        0.3632,
        0.3757,
        0.4161,
        0.4461,
        0.4544,
        1.1435
    ],
    "std mae": [
        0.0071,
        0.0239,
        0.0088,
        0.0222,
        0.0248,
        0.0196,
        0.0207,
        0.0194,
        0.0177,
        0.0123,
        0.031
    ],
    "mean rmse": [
        0.8123,
        0.7685,
        0.8504,
        0.7437,
        0.8673,
        0.8679,
        0.8805,
        0.9918,
        0.8243,
        1.0737,
        1.4438
    ],
    "max max_error": [
        11.1001,
        9.8955,
        9.8002,
        9.8567,
        11.0998,
        11.1003,
        10.2572,
        12.7533,
        9.5428,
        11.7,
        10.7354
    ]
}

# 插入数据
collection.insert_one(matbench_expt_gap_data)

# 关闭连接
client.close()
