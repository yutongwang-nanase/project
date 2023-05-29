import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output
import pymongo

# 连接到MongoDB数据库
client = pymongo.MongoClient("mongodb://root:9lWxJysyKUUBvC!@120.46.186.160:27017/")
db = client['mydatabase']  # 替换为实际的数据库名称
collection = db['mycollection']  # 替换为实际的集合名称
# 从数据库中获取数据
data_from_mongodb = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段
# 将数据转换为所需的格式
data = {}
for key, values in data_from_mongodb.items():
    for sub_key, value in values.items():
        if key not in data:
            data[key] = {}
        data[key][sub_key] = value

official_data = {}
collection = db['official_data']  # 替换为实际的集合名称
data_from_mongodb = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段
for key, values in data_from_mongodb.items():
    for sub_key, value in values.items():
        if key not in official_data:
            official_data[key] = {}
        official_data[key][sub_key] = value

collection = db['matbench_data']  # 替换为实际的集合名称
# 从数据库中获取数据
matbench_data = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段

collection = db['matbench_dielectric_data']  # 替换为实际的集合名称
# 从数据库中获取数据
matbench_dielectric_data = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段

matbench_expt_gap_data = {}
collection = db['matbench_expt_gap_data']  # 替换为实际的集合名称
# 从数据库中获取数据
matbench_expt_gap_data = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段

collection = db['matbench_expt_is_metal_data']  # 替换为实际的集合名称
# 从数据库中获取数据
matbench_expt_is_metal_data = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段

collection = db['matbench_glass_data']  # 替换为实际的集合名称
# 从数据库中获取数据
matbench_glass_data = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段

collection = db['matbench_jdft2d_data']  # 替换为实际的集合名称
# 从数据库中获取数据
matbench_jdft2d_data = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段

collection = db['matbench_gvrh_data']  # 替换为实际的集合名称
# 从数据库中获取数据
matbench_gvrh_data = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段

collection = db['matbench_kvrh_data']  # 替换为实际的集合名称
# 从数据库中获取数据
matbench_kvrh_data = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段

collection = db['matbench_e_form_data']  # 替换为实际的集合名称
# 从数据库中获取数据
matbench_e_form_data = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段

collection = db['matbench_mp_gap_data']  # 替换为实际的集合名称
# 从数据库中获取数据
matbench_mp_gap_data = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段

collection = db['matbench_mp_is_metal_data']  # 替换为实际的集合名称
# 从数据库中获取数据
matbench_mp_is_metal_data = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段

collection = db['matbench_perovskites_data']  # 替换为实际的集合名称
# 从数据库中获取数据
matbench_perovskites_data = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段

collection = db['matbench_phonons_data']  # 替换为实际的集合名称
# 从数据库中获取数据
matbench_phonons_data = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段

collection = db['matbench_steels_data']  # 替换为实际的集合名称
# 从数据库中获取数据
matbench_steels_data = collection.find_one({}, {'_id': 0})  # 在这里指定要排除的'_id'字段

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

        ], style={'position': 'fixed', 'width': 'auto', 'left': '4%', 'padding-top': '20px',
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
               'background-color': 'black', 'padding-left': '18%'})

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
        html.H1('matbench_expt_is_metal的模型预测能力的排行榜', style={'color': '#FFCC99', 'paper_bgcolor': '#404040'}),
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

    ], style={'height': '2000px', 'backgroundColor': '#404040'}),

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
], style={'backgroundColor': '#404040'})


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
    app.run_server(debug=False, host='123.249.2.21', port=8081)

