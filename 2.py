import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output

data = {
    'Kvrh': {'CGCNN': 0.068, 'DimeNet': 0.064, 'MEGNet': 0.068},
    'jdft2d': {'CGCNN': 54.873, 'DimeNet': 57.779, 'MEGNet': 53.224},
    'dielectric': {'CGCNN': 0.632, 'DimeNet': 0.366, 'MEGNet': 0.349},
    'Gvrh': {'CGCNN': 0.057, 'DimeNet': 0.085, 'MEGNet': 0.094},
    'mp_e_form': {'CGCNN': 0.034, 'DimeNet': 0.023, 'MEGNet': 0.024},
    'mp_gap': {'CGCNN': 0.211, 'DimeNet': 0.252, 'MEGNet': 0.201},
    'perovskites': {'CGCNN': 0.039, 'DimeNet': 0.042, 'MEGNet': 0.059},
    'phonons': {'CGCNN': 36.299, 'DimeNet': 44.531, 'MEGNet': 36.293},

}

matbench_data = {
    'Task name': [
        'matbench_steels', 'matbench_jdft2d', 'matbench_phonons',
        'matbench_expt_gap', 'matbench_dielectric', 'matbench_expt_is_metal', 'matbench_glass',
        'matbench_log_gvrh', 'matbench_log_kvrh', 'matbench_perovskites',
        'matbench_mp_gap', 'matbench_mp_is_metal', 'matbench_mp_e_form'
    ],
    'Samples': [
        312, 636, 1265, 4604, 4764, 4921, 5680, 10987,
        10987, 18928, 106113, 106113, 132752
    ],
    'Algorithm': [
        'MODNet (v0.1.12)', 'MODNet (v0.1.12)', 'MegNet (kgcnn v2.1.0)', 'MODNet (v0.1.12)',
        'MODNet (v0.1.12)', 'AMMExpress v2020', 'MODNet (v0.1.12)', 'coGN',
        'coGN', 'coGN', 'coGN', 'CGCNN v2019', 'coGN'
    ],
    'Verified MAE (unit) or ROCAUC': [
        '87.7627 (MPa)', '33.1918 (meV/atom)', '28.7606 (cm^-1)',
        '0.3327 (eV)', '0.2711 (unitless)', '0.9209', '0.9603',
        '0.0689 (log10(GPa))', '0.0535 (log10(GPa))',
        '0.0269 (eV/unit cell)', '0.1559 (eV)', '0.9520',
        '0.0170 (eV/atom)'
    ]
}
official_data = {
    'Kvrh': {'CGCNN': 0.0712, 'DimeNet': 0.0572, 'MEGNet': 0.0668},
    'jdft2d': {'CGCNN': 49.2440, 'DimeNet': 49.0243, 'MEGNet': 54.1719},
    'dielectric': {'CGCNN': 0.5988, 'DimeNet': 0.3400, 'MEGNet': 0.3391},
    'Gvrh': {'CGCNN': 0.0895, 'DimeNet': 0.0792, 'MEGNet': 0.0871},
    'mp_e_form': {'CGCNN': 0.0337, 'DimeNet': 0.0235, 'MEGNet': 0.0252},
    'mp_gap': {'CGCNN': 0.2972, 'DimeNet': 0.1993, 'MEGNet': 0.1934},
    'mp_is_metal': {'CGCNN': 0.9520, 'DimeNet': 0.9021, 'MEGNet': 0.9032},
    'perovskites': {'CGCNN': 0.0452, 'DimeNet': 0.0376, 'MEGNet': 0.0352},
    'phonons': {'CGCNN': 57.7635, 'DimeNet': 37.4619, 'MEGNet': 28.7606},
}
matbench_dielectric_data = {
    'algorithm': [
        'MODNet (v0.1.12)', 'MODNet (v0.1.10)', 'coGN', 'AMMExpress v2020', 'Finder_v1.2 structure-based version',
        'Finder_v1.2 composition-only version', 'CrabNet', 'SchNet (kgcnn v2.1.0)', 'MegNet (kgcnn v2.1.0)',
        'DimeNet++ (kgcnn v2.1.0)', 'ALIGNN', 'RF-SCM/Magpie', 'CGCNN v2019', 'Dummy'
    ],
    'mean mae': [
        0.2711, 0.2970, 0.3088, 0.3150, 0.3197, 0.3204, 0.3234, 0.3277, 0.3391, 0.3400, 0.3449, 0.4196, 0.5988, 0.8088
    ],
    'std mae': [
        0.0714, 0.0720, 0.0859, 0.0672, 0.0717, 0.0811, 0.0714, 0.0829, 0.0745, 0.0570, 0.0871, 0.0750, 0.0833, 0.0718
    ],
    'mean rmse': [
        1.6832, 1.7185, 2.0546, 1.7202, 1.7213, 1.7189, 1.7288, 1.8990, 1.9871, 1.9936, 1.9651, 1.8538, 1.8976, 1.9728
    ],
    'max max_error': [
        59.1179, 58.9519, 58.7728, 59.0112, 59.0606, 59.0528, 59.1583, 58.6071, 59.3095, 58.5416, 58.7285, 59.1201,
        58.9996, 59.6653
    ]
}
matbench_expt_gap_data = {
    'algorithm': [
        'Ax/SAASBO CrabNet v1.2.7',
        'MODNet (v0.1.12)',
        'CrabNet',
        'MODNet (v0.1.10)',
        'Ax+CrabNet v1.2.1',
        'Ax(10/90)+CrabNet v1.2.7',
        'CrabNet v1.2.1',
        'AMMExpress v2020',
        'RF-SCM/Magpie',
        'gptchem',
        'Dummy'
    ],
    'mean mae': [
        0.3310, 0.3327, 0.3463, 0.3470, 0.3566, 0.3632, 0.3757, 0.4161, 0.4461, 0.4544, 1.1435
    ],
    'std mae': [
        0.0071, 0.0239, 0.0088, 0.0222, 0.0248, 0.0196, 0.0207, 0.0194, 0.0177, 0.0123, 0.0310
    ],
    'mean rmse': [
        0.8123, 0.7685, 0.8504, 0.7437, 0.8673, 0.8679, 0.8805, 0.9918, 0.8243, 1.0737, 1.4438
    ],
    'max max_error': [
        11.1001, 9.8955, 9.8002, 9.8567, 11.0998, 11.1003, 10.2572, 12.7533, 9.5428, 11.7000, 10.7354
    ]
}
matbench_expt_is_metal_data = {
    'algorithm': [
        'AMMExpress v2020', 'RF-SCM/Magpie', 'MODNet (v0.1.10)', 'MODNet (v0.1.12)',
        'gptchem', 'Dummy'
    ],
    'mean rocauc': [
        0.9209, 0.9167, 0.9161, 0.9161, 0.8965, 0.4924
    ],
    'std rocauc': [
        0.0028, 0.0064, 0.0072, 0.0072, 0.0060, 0.0128
    ],
    'mean f1': [
        0.9200, 0.9159, 0.9153, 0.9153, 0.8953, 0.4913
    ],
    'mean balanced_accuracy': [
        0.9209, 0.9167, 0.9161, 0.9161, 0.8965, 0.4924
    ]
}
matbench_glass_data = {
    'algorithm': [
        'MODNet (v0.1.12)',
        'AMMExpress v2020',
        'RF-SCM/Magpie',
        'MODNet (v0.1.10)',
        'gptchem',
        'Dummy'
    ],
    'mean rocauc': [
        0.9603, 0.8607, 0.8587, 0.8107, 0.7762, 0.5005
    ],
    'std rocauc': [
        0.0075, 0.0199, 0.0158, 0.0212, 0.0122, 0.0178
    ],
    'mean f1': [
        0.9784, 0.9043, 0.9278, 0.9104, 0.8782, 0.7127
    ],
    'mean balanced_accuracy': [
        0.9603, 0.8607, 0.8587, 0.8107, 0.7762, 0.5005
    ]
}
matbench_jdft2d_data = {
    'algorithm': [
        'MODNet (v0.1.12)',
        'MODNet (v0.1.10)',
        'coGN',
        'AMMExpress v2020',
        'SchNet (kgcnn v2.1.0)',
        'ALIGNN',
        'CrabNet',
        'Finder_v1.2 structure-based version',
        'Finder_v1.2 composition-only version',
        'DimeNet++ (kgcnn v2.1.0)',
        'CGCNN v2019',
        'RF-SCM/Magpie',
        'MegNet (kgcnn v2.1.0)',
        'Dummy'
    ],
    'mean mae': [
        33.1918, 34.5368, 37.1652, 39.8497, 42.6637, 43.4244, 45.6104, 46.1339, 47.9614, 49.0243,
        49.2440, 50.0440, 54.1719, 67.2851
    ],
    'std mae': [
        7.3428, 9.4959, 13.6825, 9.8835, 13.7201, 8.9491, 12.2491, 11.4644, 11.6680, 11.9027,
        11.5865, 8.6271, 11.4299, 10.1832
    ],
    'mean rmse': [
        96.7332, 92.2288, 101.1580, 106.5460, 111.0187, 117.4213, 120.0088, 120.0917, 120.8819,
        114.9349, 112.7689, 112.2660, 129.3267, 126.8446
    ],
    'max max_error': [
        1564.8245, 1534.9797, 1515.5614, 1552.9102, 1524.9143, 1519.7424, 1532.0118, 1581.4571,
        1582.3598, 1515.0046, 1516.9120, 1538.6073, 1561.5756, 1491.7993
    ]
}
matbench_gvrh_data = {
    'algorithm': [
        'coGN', 'ALIGNN', 'MODNet (v0.1.10)', 'MODNet (v0.1.12)', 'DimeNet++ (kgcnn v2.1.0)',
        'SchNet (kgcnn v2.1.0)', 'MegNet (kgcnn v2.1.0)', 'AMMExpress v2020',
        'CGCNN v2019', 'Finder_v1.2 structure-based version',
        'Finder_v1.2 composition-only version', 'CrabNet', 'RF-SCM/Magpie', 'Dummy'
    ],
    'mean mae': [
        0.0689, 0.0715, 0.0731, 0.0731, 0.0792, 0.0796, 0.0871, 0.0874, 0.0895, 0.0910,
        0.0996, 0.1014, 0.1040, 0.2931
    ],
    'std mae': [
        0.0009, 0.0006, 0.0007, 0.0007, 0.0011, 0.0022, 0.0013, 0.0020, 0.0016, 0.0018,
        0.0018, 0.0017, 0.0016, 0.0031
    ],
    'mean rmse': [
        0.1102, 0.1123, 0.1103, 0.1103, 0.1255, 0.1260, 0.1358, 0.1277, 0.1337, 0.1412,
        0.1572, 0.1604, 0.1540, 0.3716
    ],
    'max max_error': [
        1.0842, 1.1324, 1.1745, 1.1745, 1.5558, 1.1584, 1.5558, 1.1580, 1.4520, 1.4842,
        2.3854, 2.4220, 1.6942, 1.5552
    ]
}
matbench_kvrh_data = {
    'algorithm': [
        'coGN',
        'MODNet (v0.1.10)',
        'MODNet (v0.1.12)',
        'ALIGNN',
        'DimeNet++ (kgcnn v2.1.0)',
        'SchNet (kgcnn v2.1.0)',
        'AMMExpress v2020',
        'MegNet (kgcnn v2.1.0)',
        'Finder_v1.2 structure-based version',
        'CGCNN v2019',
        'CrabNet',
        'Finder_v1.2 composition-only version',
        'RF-SCM/Magpie',
        'Dummy'
    ],
    'mean mae': [
        0.0535, 0.0548, 0.0548, 0.0568, 0.0572, 0.0590, 0.0647, 0.0668, 0.0693, 0.0712,
        0.0758, 0.0764, 0.0820, 0.2897
    ],
    'std mae': [
        0.0028, 0.0025, 0.0025, 0.0028, 0.0032, 0.0022, 0.0015, 0.0034, 0.0035, 0.0028,
        0.0034, 0.0025, 0.0027, 0.0043
    ],
    'mean rmse': [
        0.1082, 0.1043, 0.1043, 0.1106, 0.1149, 0.1143, 0.1183, 0.1287, 0.1318, 0.1301,
        0.1471, 0.1491, 0.1454, 0.3693
    ],
    'max max_error': [
        1.6521, 1.5366, 1.5366, 1.6438, 1.7063, 1.7542, 1.4823, 1.8705, 1.6242, 1.7725,
        1.8430, 2.3863, 1.7642, 1.8822
    ]
}
matbench_e_form_data = {
    'algorithm': [
        'coGN', 'ALIGNN', 'SchNet (kgcnn v2.1.0)',
        'DimeNet++ (kgcnn v2.1.0)', 'GN-OA v1', 'MegNet (kgcnn v2.1.0)', 'CGCNN v2019',
        'Finder_v1.2 structure-based version', 'MODNet (v0.1.10)',
        'MODNet (v0.1.12)', 'Finder_v1.2 composition-only version',
        'CrabNet', 'RF-SCM/Magpie', 'AMMExpress v2020',
        'Lattice-XGBoost', 'Dummy'
    ],
    'mean mae': [
        0.0170, 0.0215, 0.0218, 0.0235, 0.0248, 0.0252, 0.0337, 0.0343, 0.0448, 0.0448,
        0.0839, 0.0862, 0.1165, 0.1726, 0.7515, 1.0059
    ],
    'std mae': [
        0.0003, 0.0005, 0.0004, 0.0004, 0.0002, 0.0003, 0.0006, 0.0012, 0.0039, 0.0039,
        0.0011, 0.0010, 0.0008, 0.0270, 0.0042, 0.0030
    ],
    'mean rmse': [
        0.0483, 0.0544, 0.0529, 0.0695, 0.0636, 0.0701, 0.0682, 0.1331, 0.0888, 0.0888,
        0.2537, 0.2544, 0.2419, 0.2602, 0.9415, 1.1631
    ],
    'max max_error': [
        3.8249, 3.5487, 2.9990, 3.6006, 2.4150, 3.6006, 7.7205, 45.1834, 4.8803, 4.8803,
        6.3948, 6.3774, 5.4382, 5.8108, 4.2425, 3.9096
    ]
}
matbench_mp_gap_data = {
    'algorithm': [
        'coGN', 'ALIGNN', 'MegNet (kgcnn v2.1.0)', 'DimeNet++ (kgcnn v2.1.0)', 'Finder_v1.2 structure-based version',
        'MODNet (v0.1.10)', 'MODNet (v0.1.12)', 'Finder_v1.2 composition-only version',
        'SchNet (kgcnn v2.1.0)', 'CrabNet', 'AMMExpress v2020', 'CGCNN v2019',
        'RF-SCM/Magpie', 'Dummy'
    ],
    'mean mae': [
        0.1559, 0.1861, 0.1934, 0.1993, 0.2193, 0.2199, 0.2199, 0.2308, 0.2352, 0.2655,
        0.2824, 0.2972, 0.3452, 1.3272
    ],
    'std mae': [
        0.0017, 0.0030, 0.0087, 0.0058, 0.0012, 0.0059, 0.0059, 0.0029, 0.0034, 0.0029,
        0.0061, 0.0035, 0.0033, 0.0060
    ],
    'mean rmse': [
        0.3956, 0.4635, 0.4715, 0.4720, 0.4989, 0.4525, 0.4525, 0.4837, 0.5172, 0.5898,
        0.5611, 0.6771, 0.6125, 1.5989
    ],
    'max max_error': [
        7.3352, 7.4756, 7.8821, 14.0169, 7.6676, 7.5685, 7.5685, 7.8152, 9.1171, 7.9829,
        6.9105, 13.6569, 7.0601, 8.5092
    ]
}
matbench_mp_is_metal_data = {
    'algorithm': [
        'CGCNN v2019', 'ALIGNN', 'coGN', 'AMMExpress v2020',
        'MODNet (v0.1.12)', 'DimeNet++ (kgcnn v2.1.0)', 'MegNet (kgcnn v2.1.0)',
        'RF-SCM/Magpie', 'SchNet (kgcnn v2.1.0)', 'Matformer',
        'MODNet (v0.1.10)', 'Dummy'
    ],
    'mean rocauc': [
        0.9520, 0.9128, 0.9124, 0.9093, 0.9038, 0.9032, 0.9021, 0.8992, 0.8907, 0.8117,
        0.7805, 0.5012
    ],
    'std rocauc': [
        0.0074, 0.0015, 0.0023, 0.0008, 0.0106, 0.0036, 0.0018, 0.0019, 0.0018, 0.0455,
        0.1406, 0.0043
    ],
    'mean f1': [
        0.9462, 0.9015, 0.9012, 0.8981, 0.8916, 0.8907, 0.8895, 0.8866, 0.8765, 0.7660,
        0.6621, 0.4353
    ],
    'mean balanced_accuracy': [
        0.9520, 0.9128, 0.9124, 0.9093, 0.9038, 0.9032, 0.9021, 0.8992, 0.8907, 0.8117,
        0.7805, 0.5012
    ]
}
matbench_perovskites_data = {
    'algorithm': [
        'coGN', 'ALIGNN', 'Finder_v1.2 structure-based version',
        'SchNet (kgcnn v2.1.0)', 'MegNet (kgcnn v2.1.0)', 'DimeNet++ (kgcnn v2.1.0)',
        'CGCNN v2019', 'MODNet (v0.1.10)', 'MODNet (v0.1.12)', 'AMMExpress v2020',
        'RF-SCM/Magpie', 'CrabNet', 'Dummy', 'Finder_v1.2'
    ],
    'mean mae': [
        0.0269, 0.0288, 0.0320, 0.0342, 0.0352, 0.0376, 0.0452, 0.0908, 0.0908, 0.2005,
        0.2355, 0.4065, 0.5660, 0.6450
    ],
    'std mae': [
        0.0008, 0.0009, 0.0012, 0.0005, 0.0016, 0.0011, 0.0007, 0.0028, 0.0028, 0.0085,
        0.0034, 0.0069, 0.0048, 0.0167
    ],
    'mean rmse': [
        0.0554, 0.0559, 0.0594, 0.0599, 0.0635, 0.0642, 0.0722, 0.1277, 0.1277, 0.2954,
        0.3346, 0.5412, 0.7424, 0.8831
    ],
    'max max_error': [
        0.9449, 0.9028, 0.8875, 0.8929, 1.0236, 0.9676, 0.9923, 1.1780, 1.1780, 3.3116,
        2.8870, 2.3726, 3.6873, 3.5402
    ]
}
matbench_phonons_data = {
    'algorithm': [
        'MegNet (kgcnn v2.1.0)', 'ALIGNN', 'coGN', 'MODNet (v0.1.12)',
        'DimeNet++ (kgcnn v2.1.0)', 'MODNet (v0.1.10)', 'SchNet (kgcnn v2.1.0)',
        'Finder_v1.2 composition-only version', 'Finder_v1.2 structure-based version',
        'CrabNet', 'AMMExpress v2020', 'CGCNN v2019', 'RF-SCM/Magpie',
        'Dummy'
    ],
    'mean mae': [
        28.7606, 29.5385, 29.7117, 34.2751, 37.4619, 38.7524, 38.9636, 46.5751, 50.7406,
        55.1114, 56.1706, 57.7635, 67.6126, 323.9822
    ],
    'std mae': [
        2.5767, 2.1148, 1.9968, 2.0781, 2.1934, 1.7732, 1.9760, 3.7415, 5.4036, 5.7317,
        6.7981, 12.3109, 8.9900, 17.7269
    ],
    'mean rmse': [
        57.4679, 53.5010, 57.7099, 70.0669, 80.3047, 78.2220, 76.9279, 94.8514, 124.0783,
        138.3775, 109.7048, 141.7018, 146.2764, 492.1533
    ],
    'max max_error': [
        774.1321, 615.3466, 622.4674, 1079.1280, 1012.6802, 1031.8168, 1034.3312, 1051.2485,
        1706.8711, 1452.7562, 1151.5570, 2504.8743, 2024.7301, 3062.3450
    ]
}
matbench_steels_data = {
    'algorithm': [
        'AutoML-Mat', 'MODNet (v0.1.12)', 'RF-Regex Steels', 'MODNet (v0.1.10)', 'AMMExpress v2020',
        'RF-SCM/Magpie', 'CrabNet', 'gptchem', 'Dummy'
    ],
    'mean mae': [
        82.3043, 87.7627, 90.5896, 96.2139, 97.4929, 103.5125, 107.3160, 143.0028, 229.7445
    ],
    'std mae': [
        8.8565, 12.2188, 6.7138, 9.8352, 13.7919, 11.0368, 18.9057, 16.9642, 9.6958
    ],
    'mean rmse': [
        114.0577, 144.7722, 128.0865, 149.9535, 154.0161, 149.3839, 153.0041, 218.0282, 301.2211
    ],
    'max max_error': [
        463.0130, 1121.0504, 505.2967, 931.3261, 1142.9223, 1121.1276, 576.3912, 1368.2000, 1088.0568
    ]
}

df_matbench_dielectric = pd.DataFrame(matbench_dielectric_data)
df_matbench_expt_gap = pd.DataFrame(matbench_expt_gap_data)
df_matbench_expt_is_metal = pd.DataFrame(matbench_expt_is_metal_data)
df_matbench_glass = pd.DataFrame(matbench_glass_data)
df_matbench_jdft2d = pd.DataFrame(matbench_jdft2d_data)
df_matbench_gvrh = pd.DataFrame(matbench_gvrh_data)
df_matbench_kvrh = pd.DataFrame(matbench_kvrh_data)
df_matbench_e_form = pd.DataFrame(matbench_e_form_data)
df_matbench_mp_gap = pd.DataFrame(matbench_mp_gap_data)
df_matbench_mp_is_metal = pd.DataFrame(matbench_mp_is_metal_data)
df_matbench_perovskites = pd.DataFrame(matbench_perovskites_data)
df_matbench_phonons = pd.DataFrame(matbench_phonons_data)
df_matbench_steels = pd.DataFrame(matbench_steels_data)
df_A = pd.read_csv('cgcnn_log_kvrh.csv')
df_B = pd.read_csv('test_results.csv')
df_die = pd.read_csv('picture2/cgcnn_dielectric.csv')
df_eform = pd.read_csv('picture2/cgcnn_e_form.csv')
df_gap = pd.read_csv('picture2/cgcnn_gap.csv')
df_gvrh = pd.read_csv('picture2/cgcnn_gvrh.csv')
df_per = pd.read_csv('picture2/cgcnn_perovskites.csv')
df_phon = pd.read_csv('picture2/cgcnn_phonons.csv')
df_matbench = pd.DataFrame(matbench_data)

df = pd.DataFrame({
    'Task name': ['matbench_steels', 'matbench_jdft2d', 'matbench_phonons', 'matbench_expt_gap', 'matbench_dielectric',
                  'matbench_expt_is_metal', 'matbench_glass', 'matbench_log_gvrh', 'matbench_log_kvrh',
                  'matbench_perovskites', 'matbench_mp_gap', 'matbench_mp_is_metal', 'mat_mp_e_form'],
    'Task type/input': ['regression/composition', 'regression/structure', 'regression/structure',
                        'regression/composition', 'regression/structure', 'classification/composition',
                        'classification/composition', 'regression/structure', 'regression/structure',
                        'regression/structure', 'regression/structure', 'classification/structure',
                        'regression/structure'],
    'Target column (unit)': ['yield strength (MPa)', 'exfoliation_en (meV/atom)', 'last phdos peak (cm^-1)',
                             'gap expt (eV)', 'n (unitless)', 'is_metal', 'gfa', 'log10(G_VRH (log10(GPa))',
                             'log10(K_VRH) (log10(GPa))', 'e_form (eV/unit cell)', 'gap pbe (eV)', 'is_metal',
                             'e_form (eV/atom)'],
    'Samples': [312, 636, 1265, 4604, 4764, 4921, 5680, 10987, 10987, 18928, 106113, 106113, 132752],
    'MAD (regression) or Fraction True (classification)': [229.3743, 67.202, 323.7870, 1.1432, 0.8085, 0.4981, 0.7104,
                                                           0.2931, 0.2897, 0.5660, 1.3271, 0.4349, 1.0059],
    '': ['download, interactive', 'download, interactive', 'download, interactive', 'download, interactive',
         'download, interactive', 'download, interactive', 'download, interactive', 'download, interactive',
         'download, interactive', 'download, interactive', 'download, interactive', 'download, interactive',
         'download, interactive'],
    'Submissions': [9, 14, 14, 11, 14, 6, 6, 14, 14, 14, 14, 11, 16],
    'Task description': ['Predict the yield strength of steel alloys based on their composition',
                         'Predict the exfoliation energy of 2D materials based on their structure',
                         'Predict the frequency of the last peak in the phonon density of states of materials based '
                         'on their structure',
                         'Predict the experimental band gap of inorganic compounds based on their composition',
                         'Predict the refractive index of materials based on their structure',
                         'Classify inorganic compounds as metals or non-metals based on their composition',
                         'Classify inorganic compounds as glass formers or glass modifiers based on their composition',
                         'Predict the shear modulus of materials based on their structure',
                         'Predict the bulk modulus of materials based on their structure',
                         'Predict the formation energy of perovskite materials based on their structure',
                         'Predict the band gap of inorganic compounds based on their structure',
                         'Classify inorganic compounds as metals or non-metals based on their structure',
                         'Predict the formation energy per atom of inorganic compounds based on their structure'],
    'Task category': ['Materials science', 'Materials science', 'Materials science', 'Materials science',
                      'Materials science', 'Materials science', 'Materials science', 'Materials science',
                      'Materials science', 'Materials science', 'Materials science', 'Materials science',
                      'Materials science'],
    'Task difficulty': ['Intermediate', 'Advanced', 'Advanced', 'Intermediate', 'Intermediate', 'Beginner', 'Beginner',
                        'Advanced', 'Advanced', 'Advanced', 'Advanced', 'Beginner', 'Advanced']
})
df_C = pd.read_csv('megnet_kvrh.csv')
df_D = pd.read_csv('megnet_dielectric.csv')
df_E = pd.read_csv('megnet_gvrh.csv')
df_F = pd.read_csv('megnet_phonons.csv')
df_G = pd.read_csv('megnet_perovskites.csv')
df_H = pd.read_csv('megnet_jdft2d.csv')
df_I = pd.read_csv('megnet_mp_e_form.csv')
df_J = pd.read_csv('megnet_mp_gap.csv')
num_labels = ['<1k', '1k-10k', '10k-100k', '>=100k']
num_values = [2, 5, 3, 3]
num_colors = ['#7B68EE', '#6A5ACD', '#483D8B', '#2c2656']

app_colors = ['#FFA07A', '#FF7F50', '#FF6347', '#FF4500', '#FF8C00']
app_labels = ['stability', 'electronic', 'mechanical', 'optical', 'thermal']
app_values = [4, 4, 3, 1, 1]

type_colors = ['#FFDAB9', '#F4A460']
type_labels = ['regression', 'classification']
type_values = [3, 10]

data_colors = ['#90EE90', '#32CD32']
data_labels = ['DTF', 'experiment']
data_values = [9, 4]

# Create pie charts
num_chart = go.Pie(labels=num_labels, values=num_values, marker=dict(colors=num_colors))
app_chart = go.Pie(labels=app_labels, values=app_values, marker=dict(colors=app_colors))
type_chart = go.Pie(labels=type_labels, values=type_values, marker=dict(colors=type_colors))
data_chart = go.Pie(labels=data_labels, values=data_values, marker=dict(colors=data_colors))

# Define layout for each pie chart
num_layout = go.Layout(title='Number of Samples', width=460,
                       height=470)
app_layout = go.Layout(title='Matbench Property Distribution', width=460,
                       height=470)
type_layout = go.Layout(title='Task Type Distribution', width=460,
                        height=470)
data_layout = go.Layout(title='Data Type Distribution', width=460,
                        height=470)

paragraph1 = html.Div([
    html.H1('欢迎来到我的网页！'),
    html.P('我的网页灵感来源于matbench，旨在帮助您更好地理解材料科学和计算材料学。'),
    html.P('通过这个页面，您可以了解到各种材料属性的数据集和模型，以及它们如何被用于材料设计和发现。'),
])

# 第二个段落
paragraph2 = html.Div([
    html.P(
        '页面的设计和功能灵感来自于matbench项目，它是一个由材料科学家和计算机科学家合作创建的开放数据集和基准测试平台。'),
    html.P(
        '与matbench不同的是，我的页面重点放在对材料科学初学者友好的解释和展示上，同时也提供了一些进阶的内容和资源，以满足更高级的用户需求。'),
])

# 第三个段落
paragraph3 = html.Div([
    html.P('我希望您能在这个页面中找到有用的信息和灵感，也欢迎您提出任何反馈和建议，帮助我不断改进这个页面。'),
    html.P('祝您学习愉快！'),
])

markdown_text = '''
## MAPE和RMSE

MAPE指的是平均绝对百分比误差（Mean Absolute Percentage Error），它是预测值与实际值之间的百分比误差的平均值。对于样本数据集D，MAPE可以表示为：

MAPE(D) = (1/n) * Σ | (预测值(i) - 实际值(i)) / 实际值(i) | * 100%

其中n是样本数据集D的大小。

MAPE可以反映模型预测误差相对于实际值的大小，具有良好的可解释性。但是，MAPE存在一些问题，例如在实际值接近于0时，MAPE可能会出现异常值。

相对地，RMSE指的是均方根误差（Root Mean Squared Error），它是预测值与实际值之间的平方误差的平均值的平方根。对于样本数据集D，RMSE可以表示为：

RMSE(D) = sqrt( (1/n) * Σ (预测值(i) - 实际值(i))^2 )

其中n是样本数据集D的大小。

RMSE可以反映模型预测误差的大小，并且能够更好地处理异常值。通常来说，RMSE越小，说明模型的预测越准确。
'''
cgcnn_intro = '''
# CGCNN简介

CGCNN（Crystal Graph Convolutional Neural Network）是一种基于深度学习的晶体结构预测方法，可用于预测晶体材料的一些属性，如能带、晶格常数等。为了更好地评估 CGCNN 预测性能，通常需要绘制预测值和真实值之间的曲线。

选择 CGCNN 来展示预测值和真实值的曲线是因为它是一种高效、准确的晶体结构预测方法。与传统的基于物理理论或经验公式的方法相比，CGCNN 不需要繁琐的手工特征工程，而是通过学习晶体结构的局部特征和全局特征，可以自动提取关键特征，从而获得更好的预测性能。
'''


def create_figure(selected_model, selected_task):
    trace1 = go.Bar(
        x=list(data[selected_task].keys()),
        y=list(data[selected_task].values()),
        name='Results'
    )
    trace2 = go.Bar(
        x=list(official_data[selected_task].keys()),
        y=list(official_data[selected_task].values()),
        name='Official Results'
    )
    if selected_model == 'All Models':
        data_plot = [trace1, trace2]
    else:
        data_plot = [trace1 if selected_model == 'Results' else trace2]

    return {
        'data': data_plot,
        'layout': go.Layout(
            barmode='group',
            title=f'{selected_model} on {selected_task}',
            xaxis={'title': 'Model'},
            yaxis={'title': 'Performance'},
        )
    }


# 创建第一个Dash应用程序的布局
app1 = dash.Dash(__name__)
app1.layout = html.Div(children=[
    # left
    # left
    # left
    html.Div(children=[
        html.Div([

            html.H1('导航', style={'color': 'white'}),
            html.A('回到页顶', href='#top', style={'color': '#FFCC99'}),
            html.Br(),
            html.Br(),
            html.A('Matbench Dataset Visualization', href='#dataset', style={'color': '#FFCC99'}),
            html.Br(),
            html.A('比赛成绩', href='#score', style={'color': '#FFCC99'}),
            html.Br(),
            html.A('预测值和真实值对比', href='#line1', style={'color': '#FFCC99'}),
            html.Br(),
            html.A('Megnet 数据箱型图', href='#box', style={'color': '#FFCC99'}),
            html.Br(),
            html.A('模型性能对比', href='#Comparison', style={'color': '#FFCC99'}),
            html.Br(),

        ], style={'position': 'fixed', 'width': 'auto', 'left': '8%', 'padding-top': '20px',
                  'background-color': '#404040'}),
        html.Div([
            html.H1('Download', style={
                'color': 'white',
            }),
            html.Br(),
            html.A('下载matbench steels数据集', href="https://ml.materialsproject.org/projects/matbench_steels.json.gz",
                   style={'color': '#FFDAB9', 'text-decoration': 'none', 'font-weight': 'bold'}),
            html.Br(),
            html.A('下载matbench jdft2d数据集', href="https://ml.materialsproject.org/projects/matbench_jdft2d.json.gz",
                   style={'color': '#FFDAB9', 'text-decoration': 'none', 'font-weight': 'bold'}),
            html.Br(),
            html.A('下载matbench phonons数据集',
                   href="https://ml.materialsproject.org/projects/matbench_phonons.json.gz",
                   style={'color': '#FFDAB9', 'text-decoration': 'none', 'font-weight': 'bold'}),
            html.Br(),
            html.A('下载matbench expt gap数据集',
                   href="https://ml.materialsproject.org/projects/matbench_expt_gap.json.gz",
                   style={'color': '#FFDAB9', 'text-decoration': 'none', 'font-weight': 'bold'}),
            html.Br(),
            html.A('下载matbench dielectric数据集',
                   href="https://ml.materialsproject.org/projects/matbench_dielectric.json.gz",
                   style={'color': '#FFDAB9', 'text-decoration': 'none', 'font-weight': 'bold'}),
            html.Br(),
            html.A('下载matbench expt is metal数据集',
                   href="https://ml.materialsproject.org/projects/matbench_expt_is_metal.json.gz",
                   style={'color': '#FFDAB9', 'text-decoration': 'none', 'font-weight': 'bold'}),
            html.Br(),
            html.A('下载matbench glass数据集', href="https://ml.materialsproject.org/projects/matbench_glass.json.gz",
                   style={'color': '#FFDAB9', 'text-decoration': 'none', 'font-weight': 'bold'}),
            html.Br(),
            html.A('下载matbench log gvrh数据集',
                   href="https://ml.materialsproject.org/projects/matbench_log_gvrh.json.gz",
                   style={'color': '#FFDAB9', 'text-decoration': 'none', 'font-weight': 'bold'}),
            html.Br(),
            html.A('下载matbench log kvrh数据集',
                   href="https://ml.materialsproject.org/projects/matbench_log_kvrh.json.gz",
                   style={'color': '#FFDAB9', 'text-decoration': 'none', 'font-weight': 'bold'}),
            html.Br(),
            html.A('下载matbench perovskites数据集',
                   href="https://ml.materialsproject.org/projects/matbench_perovskites.json.gz",
                   style={'color': '#FFDAB9', 'text-decoration': 'none', 'font-weight': 'bold'}),
            html.Br(),
            html.A('下载matbench mp gap数据集', href="https://ml.materialsproject.org/projects/matbench_mp_gap.json.gz",
                   style={'color': '#FFDAB9', 'text-decoration': 'none', 'font-weight': 'bold'}),
            html.Br(),
            html.A('下载matbench mp is metal数据集',
                   href="https://ml.materialsproject.org/projects/matbench_mp_is_metal.json.gz",
                   style={'color': '#FFDAB9', 'text-decoration': 'none', 'font-weight': 'bold'}),
            html.Br(),
            html.A('下载mat mp e form数据集', href="https://ml.materialsproject.org/projects/mat_mp_e_form.json.gz",
                   style={'color': '#FFDAB9', 'text-decoration': 'none', 'font-weight': 'bold'})

        ], style={'position': 'fixed', 'width': 'auto', 'right': '3%', 'padding-top': '20px',
                  'background-color': '#404040'}),

        html.Div([
            html.H1('介绍', style={'color': '#FFCC99'}),
            html.Div([
                paragraph1,
                paragraph2,
                paragraph3
            ], style={'color': '#FFCC99'}),

            html.Div([
                html.Div([
                    dash_table.DataTable(
                        id='table1',
                        columns=[
                            {'name': 'Task name', 'id': 'Task name'},
                            {'name': 'Task type/input', 'id': 'Task type/input'},
                            {'name': 'Target column (unit)', 'id': 'Target column (unit)'},
                            {'name': 'Submissions', 'id': 'Submissions'},
                            {'name': 'Samples', 'id': 'Samples'}
                        ],
                        data=df.to_dict('records'),
                        style_header={
                            'backgroundColor': '#2c3e50',
                            'color': 'white',
                            'fontWeight': 'bold',
                            'textAlign': 'center',
                            'border': '1px solid white'
                        },
                        style_cell={
                            'backgroundColor': '#34495e',
                            'color': 'white',
                            'textAlign': 'center',
                            'border': '1px solid white'
                        },
                        style_data_conditional=[
                            {
                                'if': {'row_index': 'odd'},
                                'backgroundColor': '#2c3e50'
                            },
                            {
                                'if': {'column_id': 'Task difficulty'},
                                'backgroundColor': '#16a085',
                                'color': 'white'
                            },
                            {
                                'if': {'column_id': 'Task category'},
                                'backgroundColor': '#8e44ad',
                                'color': 'white'
                            },
                            {
                                'if': {'state': 'active'},
                                'backgroundColor': 'inherit !important',
                                'border': 'inherit !important'
                            }
                        ]
                    )
                ]),
                html.Br(),
                html.Div([
                    dash_table.DataTable(
                        id='table2',
                        columns=[
                            {'name': 'MAD or Fraction True ',
                             'id': 'MAD (regression) or Fraction True (classification)'},

                            # {'name': 'Task description', 'id': 'Task description'},
                            {'name': 'Task difficulty', 'id': 'Task difficulty'}
                        ],
                        data=df.to_dict('records'),
                        style_header={
                            'backgroundColor': '#2c3e50',
                            'color': 'white',
                            'fontWeight': 'bold',
                            'textAlign': 'center',
                            'border': '1px solid white'
                        },
                        style_cell={
                            'backgroundColor': '#34495e',
                            'color': 'white',
                            'textAlign': 'center',
                            'border': '1px solid white'
                        },
                        style_data_conditional=[
                            {
                                'if': {'row_index': 'odd'},
                                'backgroundColor': '#2c3e50'
                            },
                            # {
                            #     'if': {'column_id': 'Task difficulty'},
                            #     'backgroundColor': '#16a085',
                            #     'color': 'white'
                            # },
                            {
                                'if': {'column_id': 'Task category'},
                                'backgroundColor': '#8e44ad',
                                'color': 'white'
                            },
                            {
                                'if': {'state': 'active'},
                                'backgroundColor': 'inherit !important',
                                'border': 'inherit !important'
                            },
                            {
                                'if': {'column_id': 'Task difficulty',
                                       'filter_query': '{Task difficulty} = "Beginner"'},
                                'backgroundColor': '#32CD32',
                                'color': 'white'
                            },
                            {
                                'if': {'column_id': 'Task difficulty',
                                       'filter_query': '{Task difficulty} = "Intermediate"'},
                                'backgroundColor': '#F0E68C',
                                'color': 'black'
                            },
                            {
                                'if': {'column_id': 'Task difficulty',
                                       'filter_query': '{Task difficulty} = "Advanced"'},
                                'backgroundColor': '#A52A2A',
                                'color': 'white'
                            }
                        ]
                    )
                ])
            ]),

            html.Div([

                dcc.Markdown(
                    id='gvrh-description',
                    children='''**GVRH**（Grain Boundary Voltage Relaxation Hysteresis）指的是晶界电压松弛滞后的能力。它是材料科学中的一个重要属性，
特别涉及到晶界的性质和行为，如晶界电导、电子迁移和电荷储存等方面。GVRH 可能影响材料的电化学性能和电子器件的可靠性。'''
                ),
                html.Br(),
                dcc.Markdown(
                    id='phonons-description',
                    children='''**Phonons**（声子）是晶体中的一种量子态，是晶体中原子振动的一种集体激发。声子在固体中传播，可以携带能量和动量，影响
材料的热传导和声学性质。声子的能谱与材料的晶格结构密切相关，因此研究声子可以帮助我们理解材料的热力学性质和输运行为。'''
                ),
                html.Br(),
                dcc.Markdown(
                    id='perovskites-description',
                    children='''**Perovskites**（钙钛矿）是一类具有钙钛矿晶体结构的材料，具有广泛的应用潜力。钙钛矿材料的晶体结构由一个大的阳离子（通常是
钙离子）被八个小的阴离子（通常是氧离子）包围形成。这种结构的材料表现出多种有趣的光电性质，使其在太阳能电池、光电器件和光催化等领域
受到广泛关注。'''
                ),
                html.Br(),
                dcc.Markdown(
                    id='kvrh-description',
                    children='''**KVRH**（Kirkendall Voiding in Grain Boundaries）是指晶界中的柯肯达尔空洞形成现象。在金属材料的晶界处，
存在不同的扩散速率，当扩散速率不平衡时，会导致空洞在晶界中形成和扩展。KVRH 现象对于金属材料的界面稳定性和失效机制具有重要意义。'''
                ),
                html.Br(),
                dcc.Markdown(
                    id='steels-description',
                    children='''**Steels**（钢材）是一类由铁和碳组成的合金材料。钢材具有优异的力学性能、可塑性和耐腐蚀性，广泛应用于建筑、桥梁、汽车、
航空航天等领域。钢材的性能可以通过合金化、热处理和表面处理等工艺进行调控，以满足不同应用的要求。'''
                ),
                html.Br(),
                dcc.Markdown(
                    id='dielectric-description',
                    children='''**Dielectric**（介电材料）是指材料具有储存电能的能力。在电容器等应用中，储存电荷的能力对于电气性能非常重要。介电材料常常
具有较高的电阻和较低的导电性，使其能够有效地储存电荷并阻止电流的流动。介电材料广泛应用于电子器件、电力系统和通信技术等领域。'''
                ),
                html.Br(),
                dcc.Markdown(
                    id='jdft2d-description',
                    children='''**JDFT2D**（Two-Dimensional Janus Dumbbell Framework）是指二维的雅努斯哑铃结构框架。这种结构由两种不同的
原子组成，形成了一种具有非常特殊性质的材料。JDFT2D 可以展示出多种有趣的物理和化学特性，如光电效应、磁性和拓扑特性等。'''
                ),
                html.Br(),
                dcc.Markdown(
                    id='expt_gap-description',
                    children='''**Experimental Band Gap**（实验带隙）是指通过实验测量得到的材料的能带间隙。能带间隙是固体材料中价带和导带之间的
能量差，它对材料的导电性质和光学性质起着重要作用。实验带隙的准确测量可以帮助我们理解材料的能带结构和电子行为。'''
                ),
                html.Br(),
                dcc.Markdown(
                    id='expt_is_metal-description',
                    children='''**Experimental Is Metal**（实验判断金属）是根据实验数据对材料进行金属性质的判断。金属是一类具有良好导电性和热传导性
的材料，其导电性来源于自由电子在晶体中的运动。通过实验测量材料的电导率、电阻率等性质，可以确定材料是否表现出金属特性。'''
                ),
                html.Br(),
                dcc.Markdown(
                    id='glass-description',
                    children='''**Glass**（玻璃）是一种非晶态的固体材料，由非晶质的结构组成。与晶体材料不同，玻璃没有长程有序的周期性结构。玻璃具有
无定形、透明、硬度高等特点，广泛应用于建筑、容器、光学器件等领域。玻璃的性质可以通过材料成分和制备工艺进行调控，以满足各种特定的
应用需求。'''
                ),
                html.Br(),
                dcc.Markdown(
                    id='mp-gap-description',
                    children='''**Band Gap**（能隙）是指固体材料中导带和价带之间的能量间隔。能隙决定了材料的导电性和光电性质。对于半导体材料而言，
具有较大的能隙，导带和价带之间没有电子态可用于导电，因此具有较高的电阻性质。而对于导体材料来说，能隙非常小或者没有能隙，导带和价
带之间存在大量电子态可用于导电，因此具有良好的电导性质。'''
                ),
                html.Br(),
                dcc.Markdown(
                    id='mp-is-metal-description',
                    children='''**Metallicity**（金属性质）是指材料是否表现出金属的特性，即具有良好的电导性和热导性。金属是一类没有能隙的材料，
其导带中存在大量自由电子，可以自由地移动和传导电荷。相比之下，非金属材料具有能隙，导带中的电子受限，电导性较差。金属性质对于电子器
件、导线和结构材料等具有重要意义。'''
                ),
                html.Br(),
                dcc.Markdown(
                    id='mp-e-form-description',
                    children='''**Formation Energy**（能量形成）是指材料形成过程中所涉及的能量变化。在材料科学中，通过计算和比较不同晶体结构的能量形成，
可以预测和评估材料的稳定性和反应性。能量形成与材料的结构、成分以及化学反应等因素相关，对于材料合成、相变和催化等研究具有重要指导意义。'''
                ),

            ], style={'color': '#FFD700'}),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                html.H1('Matbench 数据可视化分析', id='dataset', style={'color': '#FFE5CC'}),
                # 描述
                html.Div(children='''Matbench Dataset Visualization''',
                         style={'color': '#FFE5CC'}),
                html.Table([
                    html.Tr([
                        html.Td(dcc.Graph(id='num-chart', figure={'data': [num_chart], 'layout': num_layout})),
                        html.Td(dcc.Graph(id='app-chart', figure={'data': [app_chart], 'layout': app_layout})),
                    ]),
                    html.Tr([
                        html.Td(dcc.Graph(id='type-chart', figure={'data': [type_chart], 'layout': type_layout})),
                        html.Td(dcc.Graph(id='data-chart', figure={'data': [data_chart], 'layout': data_layout})),
                    ])
                ])
            ]),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H1('比赛成绩', id='score', style={'color': '#FFE5CC'}),
            # 描述
            html.Div(children='''Comparison of grades in the dataset''',
                     style={'color': '#FFE5CC'}),
            dcc.Graph(
                id='score-graph',
                figure=go.Figure(
                    data=[
                        go.Bar(
                            x=list(data.keys()),
                            y=[data[k]['CGCNN'] for k in data.keys()],
                            text=['CGCNN', 'DimeNet', 'MEGNet'],
                            name='CGCNN',
                            marker=dict(color='#00008B')
                        ),
                        go.Bar(
                            x=list(data.keys()),
                            y=[data[k]['DimeNet'] for k in data.keys()],
                            text=['CGCNN', 'DimeNet', 'MEGNet'],
                            name='DimeNet',
                            marker=dict(color='#6495ED')
                        ),
                        go.Bar(
                            x=list(data.keys()),
                            y=[data[k]['MEGNet'] for k in data.keys()],
                            text=['CGCNN', 'DimeNet', 'MEGNet'],
                            name='MEGNet',
                            marker=dict(color='#87CEFA')
                        )
                    ],
                    layout=go.Layout(
                        barmode='group',
                        title='成绩对比',
                        xaxis=dict(title='比赛项目'),
                        yaxis=dict(title='MAE'),
                        height=600,  # 设置高度
                        width=300  # 设置宽度
                    )
                )
            ),
            html.Div([
                dcc.RadioItems(
                    id='select-game',
                    options=[
                        {'label': 'Kvrh', 'value': 'Kvrh'},
                        {'label': 'jdft2d', 'value': 'jdft2d'},
                        {'label': 'dielectric', 'value': 'dielectric'},
                        {'label': 'mp_gap', 'value': 'mp_gap'},
                        {'label': 'perovskites', 'value': 'perovskites'},
                        {'label': 'phonons', 'value': 'phonons'},
                    ],
                    value='Kvrh'
                ),
                dcc.Checklist(
                    id='select-player',
                    options=[
                        {'label': 'CGCNN', 'value': 'CGCNN'},
                        {'label': 'DimeNet', 'value': 'DimeNet'},
                        {'label': 'MEGNet', 'value': 'MEGNet'}
                    ],
                    value=['CGCNN', 'DimeNet', 'MEGNet'],
                    style={'display': 'none'}
                )
            ], style={'background-color': 'white'}),
            html.Div([
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Div([
                    html.H1(children='晶体结构预测方法介绍', id='line1', style={'color': '#FFE5CC'}),
                    html.Div([
                        dcc.Markdown(cgcnn_intro)
                    ], style={'width': '80%', 'margin': 'auto', 'color': '#FFCC99'})
                ], style={'textAlign': 'center'}),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H1("CGCNN 预测值和真实值的曲线", id='line', style={'color': '#FFE5CC'}),
                # 描述
                html.Div(children='''Curve of CGCNN predicted value and true value''',
                         style={'color': '#FFE5CC'}),
                # 选择项目的 Dropdown 组件
                dcc.Dropdown(
                    id='project-dropdown',
                    options=[
                        {'label': 'kvrh', 'value': 'A'},
                        {'label': 'jdft2d', 'value': 'B'},
                        {'label': 'gvrh', 'value': 'C'},
                        {'label': 'gap', 'value': 'D'},
                        {'label': 'dielectric', 'value': 'E'},
                        {'label': 'phonons', 'value': 'F'},
                        {'label': 'perovskites', 'value': 'G'},
                        {'label': 'e_form', 'value': 'H'},

                    ],
                    value='A'  # 默认选择项目A
                ),
                # 折线图
                dcc.Graph(id='line-chart'),
                dcc.Graph(id='scatter-plot')
            ]),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H1(children='Megnet 数据箱型图', id='box', style={'color': '#FFE5CC'}),
            # 描述
            html.Div(children='''MEGNet Box Plot''',
                     style={'color': '#FFE5CC'}),
            dcc.Dropdown(
                id='data-dropdown',
                options=[
                    {'label': 'Kvrh Data', 'value': 'C'},
                    {'label': 'Dielectric Data', 'value': 'D'},
                    {'label': 'Gvrh Data', 'value': 'E'},
                    {'label': 'Phonons Data', 'value': 'F'},
                    {'label': 'Perovskites Data', 'value': 'G'},
                    {'label': 'Jdft2d Data', 'value': 'H'},
                    {'label': 'Gap Data', 'value': 'J'},
                    {'label': 'E_form Data', 'value': 'I'},
                ],
                value='C'
            ),
            dcc.Graph(
                id='box-plot',
                figure={
                    'data': [
                        {'y': df_C[col], 'type': 'box', 'name': col} for col in ['MAE', 'MAPE', 'RMSE']
                    ],
                    'layout': {
                        'title': 'Box Plot of MAE, MAPE, and RMSE values',
                        'yaxis': {'title': 'Values'}
                    }
                }
            ),

            html.Div(
                id='data-description',
                children=[

                ]
            ),
            dcc.Markdown(children=markdown_text, style={'color': '#E5FFCC'}),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                html.H1(children='模型预测性能对比', id='Comparison', style={'color': '#FFCC99'}),

                # 描述
                html.Div(children='''Comparison of model performance on different tasks.''',
                         style={'color': '#FFE5CC'}),

                # 创建下拉列表
                html.Div([
                    dcc.Dropdown(
                        id='task-dropdown',
                        options=[{'label': i, 'value': i} for i in data.keys()],
                        value=list(data.keys())[0]
                    ),
                    dcc.Dropdown(
                        id='model-dropdown',
                        options=[{'label': 'All Models', 'value': 'All Models'},
                                 {'label': 'Results', 'value': 'Results'},
                                 {'label': 'Official Results', 'value': 'Official Results'}],
                        value='All Models'
                    ),
                ], style={'width': '50%', 'display': 'inline-block'}),

                # 绘制图表
                dcc.Graph(
                    id='performance-graph',
                    figure=create_figure('All Models', list(data.keys())[0])
                )
            ]),

        ], style={'width': '60%', 'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '20%',
                  'background-color': '#404040'}),
    ], style={'background-color': '#404040'}

    ),

])

# 创建第二个Dash应用程序的布局
app2 = dash.Dash(__name__)
app2.layout = html.Div(children=[
    # head
    # head
    # head

    html.Iframe(
        src='assets/index.html',
        style={'width': '1200px', 'height': '1200px', 'border': 'none'}
    )], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'padding-top': '50px',
               'background-color': 'black', 'padding-left': '22%'})

# 创建第三个Dash应用程序的布局
app3 = dash.Dash(__name__)
app3.layout = html.Div(children=[
    html.Div(children=[
        html.H1('matbench排行榜', style={'color': '#FFCC99'}),
        dcc.Graph(
            id='matbench',
            figure={
                'data': [
                    {'type': 'table',
                     'header': dict(values=df_matbench.columns,
                                    fill=dict(color='#808080'),
                                    font=dict(color='#FFCC99', size=24),
                                    line=dict(color='white', width=1),
                                    height=30),

                     'cells': dict(values=df_matbench.transpose().values.tolist(),
                                   fill=dict(color='#808080'),
                                   font=dict(color='#FFFFFF', size=20),
                                   line=dict(color='white', width=1),
                                   height=40
                                   )}
                ],
                'layout': {
                    'height': '800',  # 调整表格的高度
                    'paper_bgcolor': '#404040',  # 更改背景颜色
                },
                'style': {
                    'backgroundColor': '#404040',  # 设置背景颜色
                }
            }
        ),
        html.Br(),
        html.H1('matbench_deilectric的模型预测能力的排行榜', style={'color': '#FFCC99'}),
        dcc.Graph(
            id='matbench-die',
            figure={
                'data': [
                    {'type': 'table',
                     'header': dict(values=df_matbench_dielectric.columns,
                                    fill=dict(color='#808080'),
                                    font=dict(color='#FFCC99', size=20),
                                    line=dict(color='#FFFFFF', width=1)),  # 添加表头边框样式
                     'cells': dict(values=df_matbench_dielectric.transpose().values.tolist(),
                                   fill=dict(color='#808080'),
                                   font=dict(color='#FFFFFF', size=16),
                                   line=dict(color='#FFFFFF', width=1),
                                   height=30
                                   )}  # 添加单元格边框样式
                ],
                'layout': {
                    'height': '800',  # 调整表格的高度
                    'paper_bgcolor': '#404040',  # 更改背景颜色
                },
                'style': {
                    'backgroundColor': '#404040',  # 设置背景颜色
                }
            }
        ),
        html.Br(),
        html.H1('matbench_expt_gap的模型预测能力的排行榜', style={'color': '#FFCC99'}),
        dcc.Graph(
            id='matbench-expt-gap',
            figure={
                'data': [
                    {'type': 'table',
                     'header': dict(values=df_matbench_expt_gap.columns,
                                    fill=dict(color='#808080'),
                                    font=dict(color='#FFCC99', size=20),
                                    line=dict(color='#FFFFFF', width=1)),  # 添加表头边框样式
                     'cells': dict(values=df_matbench_expt_gap.transpose().values.tolist(),
                                   fill=dict(color='#808080'),
                                   font=dict(color='#FFFFFF', size=16),
                                   line=dict(color='#FFFFFF', width=1),
                                   height=30
                                   )}  # 添加单元格边框样式
                ],
                'layout': {
                    'height': '800',  # 调整表格的高度
                    'paper_bgcolor': '#404040',  # 更改背景颜色
                },
                'style': {
                    'backgroundColor': '#404040',  # 设置背景颜色
                }
            }
        ),
        html.Br(),
        html.Br(),
        html.H1('matbench_expt_is_metal的模型预测能力的排行榜', style={'color': '#FFCC99'}),
        dcc.Graph(
            id='matbench-expt-is-metal',
            figure={
                'data': [
                    {'type': 'table',
                     'header': dict(values=df_matbench_expt_is_metal.columns,
                                    fill=dict(color='#808080'),
                                    font=dict(color='#FFCC99', size=20),
                                    line=dict(color='#FFFFFF', width=1)),  # 添加表头边框样式
                     'cells': dict(values=df_matbench_expt_is_metal.transpose().values.tolist(),
                                   fill=dict(color='#808080'),
                                   font=dict(color='#FFFFFF', size=16),
                                   line=dict(color='#FFFFFF', width=1),
                                   height=30
                                   )}  # 添加单元格边框样式
                ],
                'layout': {
                    'height': '800',  # 调整表格的高度
                    'paper_bgcolor': '#404040',  # 更改背景颜色
                },
                'style': {
                    'backgroundColor': '#404040',  # 设置背景颜色
                }
            }
        ),
        html.Br(),
        html.Br(),
        html.H1('matbench_glass的模型预测能力的排行榜', style={'color': '#FFCC99'}),
        dcc.Graph(
            id='matbench-glass',
            figure={
                'data': [
                    {'type': 'table',
                     'header': dict(values=df_matbench_glass.columns,
                                    fill=dict(color='#808080'),
                                    font=dict(color='#FFCC99', size=20),
                                    line=dict(color='#FFFFFF', width=1)),  # 添加表头边框样式
                     'cells': dict(values=df_matbench_glass.transpose().values.tolist(),
                                   fill=dict(color='#808080'),
                                   font=dict(color='#FFFFFF', size=16),
                                   line=dict(color='#FFFFFF', width=1),
                                   height=30
                                   )}  # 添加单元格边框样式
                ],
                'layout': {
                    'height': '800',  # 调整表格的高度
                    'paper_bgcolor': '#404040',  # 更改背景颜色
                },
                'style': {
                    'backgroundColor': '#404040',  # 设置背景颜色
                }
            }
        ),
        html.H1('matbench_jdft2d的模型预测能力的排行榜', style={'color': '#FFCC99'}),
        dcc.Graph(
            id='matbench-gdft2d',
            figure={
                'data': [
                    {'type': 'table',
                     'header': dict(values=df_matbench_jdft2d.columns,
                                    fill=dict(color='#808080'),
                                    font=dict(color='#FFCC99', size=20),
                                    line=dict(color='#FFFFFF', width=1)),  # 添加表头边框样式
                     'cells': dict(values=df_matbench_jdft2d.transpose().values.tolist(),
                                   fill=dict(color='#808080'),
                                   font=dict(color='#FFFFFF', size=16),
                                   line=dict(color='#FFFFFF', width=1),
                                   height=30
                                   )}  # 添加单元格边框样式
                ],
                'layout': {
                    'height': '800',  # 调整表格的高度
                    'paper_bgcolor': '#404040',  # 更改背景颜色
                },
                'style': {
                    'backgroundColor': '#404040',  # 设置背景颜色
                }
            }
        ),

    ], style={'background-color': '#404040', 'height': '2000px'}),

    # App 3的其他组件
])
# 创建主应用程序的布局，并将两个子应用程序的布局组合在一起
app = dash.Dash(__name__, assets_external_path='style')
app.layout = html.Div(children=[

    html.Div([
        # 在页头左侧添加动态图标
        html.Iframe(
            src="https://giphy.com/embed/uljidatzCuEs7yo1KV",
            style={"height": "150px", "width": "150px", "border": "none", "pointer-events": "none",
                   "margin-left": "10%"},
            id='top'
        ),

        # 在页头中间添加标题
        html.H1(
            '我的页面',
            style={'color': 'white', 'background-color': '#0074D9', 'border-radius': '10px', 'padding': '20px'}
        ),
        # 在页头右侧添加静态图标，点击跳转到 GitHub 页面
        html.A(
            href="https://github.com/materialsproject/matbench",
            target="_blank",
            children=html.Div([
                html.Img(
                    src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
                    style={"height": "50px", "width": "50px", "margin-right": "10px"}
                ),
                html.Span("Visit Matbench", style={"color": "white", "margin-right": "70px"})
            ]),
            style={"display": "flex", "align-items": "center", "text-decoration": "none"}
        )

    ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'padding-top': '50px',
              'background-color': 'black'}),
    dcc.Tabs(id='tabs', value='app1', children=[
        dcc.Tab(label='主页面', value='app1', style={'background-color': '#808080'}),
        dcc.Tab(label='元素周期表', value='app2', style={'background-color': '#808080'}),
        dcc.Tab(label='官方数据', value='app3', style={'background-color': '#808080'}),
    ]),
    html.Div(id='page-content'),
    html.Div(children=[
        html.Br(),
        html.P(children='版权所有 ©2023 王羽桐. All rights reserved.', style={'color': 'white'}),
        html.Br(),
        html.P(children=[
            html.A('联系我们：', style={'color': 'white'}),
            html.A('bistuwyt@163.com', style={'color': 'white'}),
            html.A('|', style={'color': 'white'}),
            html.A('wyt34801142@gmail.com', style={'color': 'white'})
        ]),

    ], className='container', style={'height': '300px', 'background-color': '#404040'})
])


# 回调函数，用于更新图表
@app.callback(
    Output('score-graph', 'figure'),
    Input('select-game', 'value'),
    Input('select-player', 'value'),
)
def update_graph(selected_game, selected_players):
    fig = go.Figure()
    for player in selected_players:
        fig.add_trace(go.Bar(
            x=[selected_game],
            y=[data[selected_game][player]],
            text=[player],
            name=player
        ))
    fig.update_layout(
        barmode='group',
        title=f"{selected_game}的MAE成绩对比",
        xaxis=dict(title='比赛项目'),
        yaxis=dict(title='得分')
    )
    return fig


@app.callback(
    Output('line-chart', 'figure'),
    Input('project-dropdown', 'value')
)
def update_chart(selected_project):
    if selected_project == 'A':

        fig = px.line(df_A, x=df_A.index, y=['TRUE', 'predict', 'AE'], title='kvrh')
        fig.update_layout(
            barmode='group',
            title=f"MAE = {df_A.MAE[0]}",
        )

    elif selected_project == 'B':
        fig = px.line(df_B, x=df_B.index, y=['TRUE', 'predict', 'AE'], title='jdft2d')
        fig.update_layout(
            barmode='group',
            title=f"MAE = {df_B.MAE[0]}",
        )
    elif selected_project == 'E':
        fig = px.line(df_die, x=df_die.index, y=['TRUE', 'predict', 'AE'], title='dielectric')
        fig.update_layout(
            barmode='group',
            title=f"MAE = {df_die.MAE[0]}",
        )
    elif selected_project == 'H':
        fig = px.line(df_eform, x=df_eform.index, y=['TRUE', 'predict', 'AE'], title='e_form')
        fig.update_layout(
            barmode='group',
            title=f"MAE = {df_eform.MAE[0]}",
        )
    elif selected_project == 'D':
        fig = px.line(df_gap, x=df_gap.index, y=['TRUE', 'predict', 'AE'], title='gap')
        fig.update_layout(
            barmode='group',
            title=f"MAE = {df_gap.MAE[0]}",
        )
    elif selected_project == 'C':
        fig = px.line(df_gvrh, x=df_gvrh.index, y=['TRUE', 'predict', 'AE'], title='gvrh')
        fig.update_layout(
            barmode='group',
            title=f"MAE = {df_gvrh.MAE[0]}",
        )
    elif selected_project == 'G':
        fig = px.line(df_per, x=df_per.index, y=['TRUE', 'predict', 'AE'], title='perovskites')
        fig.update_layout(
            barmode='group',
            title=f"MAE = {df_per.MAE[0]}",
        )
    elif selected_project == 'F':
        fig = px.line(df_phon, x=df_phon.index, y=['TRUE', 'predict', 'AE'], title='phonons')
        fig.update_layout(
            barmode='group',
            title=f"MAE = {df_phon.MAE[0]}",
        )

    return fig


@app.callback(Output('scatter-plot', 'figure'),
              Input('project-dropdown', 'value'))
def update_scatter_plot(selected_project):
    # 根据下拉列表选择更新数据
    if selected_project == 'H':
        df = pd.read_csv('picture2/cgcnn_e_form.csv')
    elif selected_project == 'D':
        df = pd.read_csv('picture2/cgcnn_gap.csv')
    elif selected_project == 'C':
        df = pd.read_csv('picture2/cgcnn_gvrh.csv')
    elif selected_project == 'A':
        df = pd.read_csv('cgcnn_log_kvrh.csv')
    elif selected_project == 'B':
        df = pd.read_csv('score.csv')
    elif selected_project == 'E':
        df = pd.read_csv('picture2/cgcnn_dielectric.csv')
    elif selected_project == 'F':
        df = pd.read_csv('picture2/cgcnn_phonons.csv')
    elif selected_project == 'G':
        df = pd.read_csv('picture2/cgcnn_perovskites.csv')

    # 创建散点图
    fig = px.scatter(df, x="TRUE", y="predict", color="AE", hover_data=["id"])

    # 添加布局信息
    fig.update_layout(title=f"{selected_project.upper()}真实值与预测值对比图",
                      xaxis_title="真实值",
                      yaxis_title="预测值",
                      coloraxis_colorbar=dict(title="AE"))

    return fig


@app.callback(
    dash.dependencies.Output('box-plot', 'figure'),
    [dash.dependencies.Input('data-dropdown', 'value')]
)
def update_figure(selected_data):
    if selected_data == 'C':
        data = df_C
    elif selected_data == 'D':
        data = df_D
    elif selected_data == 'E':
        data = df_E
    elif selected_data == 'F':
        data = df_F
    elif selected_data == 'H':
        data = df_H
    elif selected_data == 'I':
        data = df_I
    elif selected_data == 'J':
        data = df_J
    else:
        data = df_G
    return {
        'data': [
            {'y': data[col], 'type': 'box', 'name': col} for col in ['MAE', 'MAPE', 'RMSE']
        ],
        'layout': {
            'title': 'MAE, MAPE and RMSE ',
            # for ' + selected_data + ' Data'
            'yaxis': {'title': 'Values'}
        }
    }


# define the callback function for the data descriptions
@app.callback(
    dash.dependencies.Output('kvrh-description', 'style'),
    dash.dependencies.Output('dielectric-description', 'style'),
    dash.dependencies.Output('gvrh-description', 'style'),
    dash.dependencies.Output('phonons-description', 'style'),
    dash.dependencies.Output('perovskites-description', 'style'),
    [dash.dependencies.Input('data-dropdown', 'value')]
)
def update_data_description(selected_data):
    if selected_data == 'C':
        return {'display': 'block'}, {'display': 'none'}
    elif selected_data == 'D':
        return {'display': 'block'}, {'display': 'none'}
    elif selected_data == 'E':
        return {'display': 'block'}, {'display': 'none'}
    elif selected_data == 'F':
        return {'display': 'block'}, {'display': 'none'}
    elif selected_data == 'G':
        return {'display': 'block'}, {'display': 'none'}
    else:
        return {'display': 'none'}, {'display': 'block'}


# 回调函数
@app.callback(
    dash.dependencies.Output('performance-graph', 'figure'),
    [dash.dependencies.Input('model-dropdown', 'value'),
     dash.dependencies.Input('task-dropdown', 'value')])
def update_figure(selected_model, selected_task):
    figure = create_figure(selected_model, selected_task)

    # 获取柱状图的数据
    data = figure['data'][0]
    data1 = figure['data'][1]
    # 获取柱子的高度
    y_values = data['y']
    y_values2 = data1['y']

    # 在柱子的中间位置添加文本标签
    text_labels = [str(y) for y in y_values]
    text_labels2 = [str(y) for y in y_values2]
    data['text'] = text_labels
    data1['text'] = text_labels2
    data['textposition'] = 'auto'

    return figure


# 回调函数根据选择的选项卡显示相应的子应用程序界面
@app.callback(Output('page-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'app1':
        return app1.layout
    elif tab == 'app2':
        return app2.layout
    elif tab == 'app3':
        return app3.layout


if __name__ == '__main__':
    app.run_server(debug=False, host='127.0.0.1', port=8081)
