import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# 数据
data = {
    'Kvrh': {
        'CGCNN': 0.048,
        'DimeNet': 0.06458061,
        'MEGNet': 0.06817374082073885
    },
    'jdft2d': {
        'CGCNN': 30.101,
        'DimeNet': 57.779957,
        'MEGNet': 53.224194433218166
    },
    'dielectric': {
        'CGCNN': 0.261,
        'DimeNet': 0.3668,
        'MEGNet': 0.349344458
    },
    'gvrh': {
        'CGCNN': 0.057,
        'DimeNet': 0.0856,
        'MEGNet': 0.094580340932
    },
    # 'mp_e_form': {
    #     'CGCNN': 0.034,
    #     'DimeNet': 0.0000,
    #     'MEGNet': 0
    # },
    'mp_gap': {
        'CGCNN': 0.211,
        'DimeNet': 0.2520,
        'MEGNet': 0.2015
    },
    # 'mp_is_metal': {
    #     'CGCNN': 1,
    #     'DimeNet': 1,
    #     'MEGNet': 0
    # },
    'perovskites': {
        'CGCNN': 0.039,
        'DimeNet': 0.0427,
        'MEGNet': 0.059661779
    },
    'phonons': {
        'CGCNN': 36.299,
        'DimeNet': 44.5311,
        'MEGNet': 36.29363321159584
    },

}
official_data = {
    'Kvrh': {
        'CGCNN': 0.0712,
        'DimeNet': 0.0666,
        'MEGNet': 0.0668
    },
    'jdft2d': {
        'CGCNN': 49.2440,
        'DimeNet': 44.846,
        'MEGNet': 54.1719
    },
    'dielectric': {
        'CGCNN': 0.5988,
        'DimeNet': 0.344,
        'MEGNet': 0.349344458
    },
    'gvrh': {
        'CGCNN': 0.057,
        'DimeNet': 0.0900,
        'MEGNet': 0.0871
    },
    # 'mp_e_form': {
    #     'CGCNN': 0.0337,
    #     'DimeNet': 0.0000,
    #     'MEGNet': 0.0252
    # },
    'mp_gap': {
        'CGCNN': 0.2972,
        'DimeNet': 0.2520,
        'MEGNet': 0.1934
    },
    # 'mp_is_metal': {
    #     'CGCNN': 1,
    #     'DimeNet': 1,
    #     'MEGNet': 0
    # },
    'perovskites': {
        'CGCNN': 0.0452,
        'DimeNet': 0.0437,
        'MEGNet': 0.0352
    },
    'phonons': {
        'CGCNN': 57.7635,
        'DimeNet': 51.074,
        'MEGNet': 28.7606
    },
}
df_A = pd.read_csv('cgcnn_log_kvrh.csv')
df_B = pd.read_csv('test_results.csv')
df_die = pd.read_csv('picture2/cgcnn_dielectric.csv')
df_eform = pd.read_csv('picture2/cgcnn_e_form.csv')
df_gap = pd.read_csv('picture2/cgcnn_gap.csv')
df_gvrh = pd.read_csv('picture2/cgcnn_gvrh.csv')
df_per = pd.read_csv('picture2/cgcnn_perovskites.csv')
df_phon = pd.read_csv('picture2/cgcnn_phonons.csv')

df_C = pd.read_csv('megnet_kvrh.csv')
df_D = pd.read_csv('megnet_dielectric.csv')

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
                         'Predict the frequency of the last peak in the phonon density of states of materials based on their structure',
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

# 创建Dash应用程序
app = dash.Dash(__name__, assets_external_path='style')


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


# 定义布局
app.layout = html.Div(children=[

    # head
    # head
    # head
    html.Div([
        # 在页头左侧添加动态图标
        html.Iframe(
            src="https://giphy.com/embed/uljidatzCuEs7yo1KV",
            style={"height": "150px", "width": "150px", "border": "none", "pointer-events": "none",
                   "margin-left": "10%"}
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

    # left
    # left
    # left
    html.Div(children=[
        html.Div([
            html.H1('导航'),
            html.A('跳转到图表1', href='#score'),
            html.Br(),
            html.A('跳转到图表2', href='#line1'),
            html.Br(),
            html.A('跳转到图表3', href='#box'),
            html.Br(),
            html.A('跳转到图表4', href='#Comparison'),
            html.Br(),

        ], style={'position': 'fixed', 'width': 'auto', 'left': '12%', 'padding-top': '20px',
                  'background-color': '#476481'}),
        html.Div([
            html.H1('Download'),
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

        ], style={'position': 'fixed', 'width': 'auto', 'right': '0%', 'padding-top': '20px',
                  'background-color': '#476481'}),

        html.Div([
            html.H1('介绍'),
            html.Div([
                paragraph1,
                paragraph2,
                paragraph3
            ]),


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

                            {'name': 'Task description', 'id': 'Task description'},
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
                ])
            ]),

            html.Div([
                html.H1('Matbench Dataset Visualization'),
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

            html.H1('比赛成绩', id='score'),
            dcc.Graph(
                id='score-graph',
                figure=go.Figure(
                    data=[
                        go.Bar(
                            x=list(data.keys()),
                            y=[data[k]['CGCNN'] for k in data.keys()],
                            text=['CGCNN', 'DimeNet', 'MEGNet'],
                            name='CGCNN'
                        ),
                        go.Bar(
                            x=list(data.keys()),
                            y=[data[k]['DimeNet'] for k in data.keys()],
                            text=['CGCNN', 'DimeNet', 'MEGNet'],
                            name='DimeNet'
                        ),
                        go.Bar(
                            x=list(data.keys()),
                            y=[data[k]['MEGNet'] for k in data.keys()],
                            text=['CGCNN', 'DimeNet', 'MEGNet'],
                            name='MEGNet'
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
                        # {'label': 'jdft2d', 'value': 'jdft2d'},
                        # {'label': 'jdft2d', 'value': 'jdft2d'},
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
                    html.H1(children='晶体结构预测方法介绍', id='line1'),
                    html.Div([
                        dcc.Markdown(cgcnn_intro)
                    ], style={'width': '80%', 'margin': 'auto'})
                ], style={'textAlign': 'center'}),
                html.H1("CGCNN 预测值和真实值的曲线", id='line'),
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
                # dcc.Dropdown(
                #     id='project-dropdown',
                #     options=[
                #         {'label': 'kvrh', 'value': 'A'},
                #         {'label': 'jdft2d', 'value': 'B'},
                #         {'label': 'gvrh', 'value': 'C'},
                #         {'label': 'gap', 'value': 'D'},
                #         {'label': 'dielectric', 'value': 'E'},
                #         {'label': 'phonons', 'value': 'F'},
                #         {'label': 'perovskites', 'value': 'G'},
                #         {'label': 'e_form', 'value': 'H'},
                #     ],
                #     value='A',
                #     style = {'display': 'none'}
                # ),
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
            html.H1(children='Box Plot', id='box'),
            dcc.Dropdown(
                id='data-dropdown',
                options=[
                    {'label': 'KVRH Data', 'value': 'C'},
                    {'label': 'Dielectric Data', 'value': 'D'}
                ],
                value='C'
            ),
            dcc.Graph(
                id='box-plot',
                figure={
                    'data': [
                        {'y': df_C[col], 'type': 'box', 'name': col} for col in ['mae', 'mape', 'rmse']
                    ],
                    'layout': {
                        'title': 'Box Plot of mae, mape, and rmse values',
                        'yaxis': {'title': 'Values'}
                    }
                }
            ),

            html.Div(
                id='data-description',
                children=[
                    dcc.Markdown(
                        id='kvrh-description',
                        children='''**KVRH** is a measure of a material's resistance to indentation. It is an important 
                    material property for applications such as protective coatings, where the ability to withstand 
                    damage from impacts is important.'''
                    ),
                    dcc.Markdown(
                        id='dielectric-description',
                        children='''**Dielectric** refers to the ability of a material to store electrical energy. It is 
                    an important property for applications such as capacitors, where the ability to store electrical 
                    charge is important.'''
                    )
                ]
            ),
            dcc.Markdown(children=markdown_text),
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
                html.H1(children='Model Performance', id='Comparison'),

                # 描述
                html.Div(children='''Comparison of model performance on different tasks.'''),

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
                  'background-color': '#476481'}),

        html.P('这是底部区域', style={'height': '300px', 'background-color': '#f2f2f2'}, ),
        # html.Div(children=[
        #     html.P(children='版权所有 ©2023 XYZ 公司. All rights reserved.'),
        #     html.P(children=[
        #         '联系我们：',
        #         html.A('info@xyz.com', href='mailto:info@xyz.com'),
        #         ' | ',
        #         html.A('400-123-4567', href='tel:400-123-4567')
        #     ]),
        #     html.Ul(children=[
        #         html.Li(html.A('关于我们', href='#')),
        #         html.Li(html.A('服务条款', href='#')),
        #         html.Li(html.A('隐私政策', href='#')),
        #         html.Li(html.A('常见问题', href='#')),
        #         html.Li(html.A('帮助中心', href='#'))
        #     ]),
        #     html.Div(children=[
        #         html.A(html.I(className='fab fa-facebook-f'), href='#'),
        #         html.A(html.I(className='fab fa-twitter'), href='#'),
        #         html.A(html.I(className='fab fa-instagram'), href='#'),
        #         html.A(html.I(className='fab fa-linkedin'), href='#'),
        #         html.A(html.I(className='fab fa-youtube'), href='#')
        #     ], className='social-media')
        # ], className='container')
    ], style={'background-color': '#476481'}

    ),

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

    # {'label': 'kvrh', 'value': 'A'},
    # {'label': 'jdft2d', 'value': 'B'},
    # {'label': 'gvrh', 'value': 'C'},
    # {'label': 'gap', 'value': 'D'},
    # {'label': 'dielectric', 'value': 'E'},
    # {'label': 'phonons', 'value': 'F'},
    # {'label': 'perovskites', 'value': 'G'},
    # {'label': 'e_form', 'value': 'H'},

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
    else:
        data = df_D
    return {
        'data': [
            {'y': data[col], 'type': 'box', 'name': col} for col in ['mae', 'mape', 'rmse']
        ],
        'layout': {
            'title': 'Box Plot of mae, mape, and rmse values ',
            # for ' + selected_data + ' Data'
            'yaxis': {'title': 'Values'}
        }
    }


# define the callback function for the data descriptions
@app.callback(
    dash.dependencies.Output('kvrh-description', 'style'),
    dash.dependencies.Output('dielectric-description', 'style'),
    [dash.dependencies.Input('data-dropdown', 'value')]
)
def update_data_description(selected_data):
    if selected_data == 'C':
        return {'display': 'block'}, {'display': 'none'}
    else:
        return {'display': 'none'}, {'display': 'block'}


# 回调函数
@app.callback(
    dash.dependencies.Output('performance-graph', 'figure'),
    [dash.dependencies.Input('model-dropdown', 'value'),
     dash.dependencies.Input('task-dropdown', 'value')])
def update_figure(selected_model, selected_task):
    return create_figure(selected_model, selected_task)


if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port=8082)
