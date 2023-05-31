import dash
import dash_html_components as html
import dash_core_components as dcc


DIMENET = {
    'python': ['scikit-learn==1.0.1', 'numpy==1.21.2', 'matbench==0.6.0', 'tensorflow==2.9.0',
               'kgcnn==2.1.1', 'pandas==1.5.2', 'pymatgen==2022.11.7', 'networkx==2.8.8',
               'torch==1.8.1+cu111', 'tensorflow-addons==0.17.1'],
    '配置信息': ['GPU==RTX 3080(10GB) * 1', 'CPU==12 vCPU Intel(R) Xeon(R) Platinum 8255C CPU @ 2.50GHz', '内存==40GB',
                 'Python==3.8(ubuntu18.04)', 'Cuda==11.1']
}

CGCNN = {
    'python': ['kgcnn==2.1.1', 'matbench==0.6', 'matminer==0.7.4', 'matplotlib==3.4.3',
               'networkx==2.8.8', 'numpy==1.21.2', 'plotly==5.13.1', 'pymatgen==2022.11.7',
               'scikit-learn==1.0.1', 'tensorflow==2.11.0', 'tensorflow-addons==0.17.1', 'torch==1.8.1+cu111',
               ],
    '配置信息': ['GPU==RTX 3080(10GB) * 1', 'CPU==12 vCPU Intel(R) Xeon(R) Platinum 8255C CPU @ 2.50GHz',
                 '内存==40GB', 'Python==3.8(ubuntu18.04)', 'Cuda==11.1']

}

MEGNET = {
    'python': ['kgcnn==2.1.1', 'matbench==0.6', 'matminer==0.7.4', 'matplotlib==3.5.3',
               'networkx==2.8.8', 'numpy==1.22.4', 'plotly==5.14.1', 'pymatgen==2022.11.7',
               'scikit-learn==1.0.1', 'tensorflow==2.9.0', 'tensorflow-addons==0.17.1', 'pandas==2.0.0'
               ],
    '配置信息': ['GPU==RTX 3090(10GB) * 1', 'CPU==15 vCPU AMD EPYC 7642 48-Core Processor',
                 '内存==80GB', 'Python==3.8(ubuntu20.04)', 'Cuda==11.2'
                 ]

}
app = dash.Dash(__name__)

app.layout = html.Div(
    style={'color': '#FFFFFF'},  # 设置文本颜色为白色
    children=[
        html.H1('项目环境配置配置'),

        html.H2('MEGNET'),
        html.Div(
            style={'display': 'flex'},
            children=[
                html.Div(
                    style={'flex': '50%'},
                    children=[
                        html.H2('Python库'),
                        html.Ul([html.Li(lib) for lib in MEGNET['python']])
                    ]
                ),
                html.Div(
                    style={'flex': '50%'},
                    children=[
                        html.H2('配置信息'),
                        html.Ul([html.Li(info) for info in MEGNET['配置信息']])
                    ]
                )
            ]
        ),

        html.H2('CGCNN'),
        html.Div(
            style={'display': 'flex'},
            children=[
                html.Div(
                    style={'flex': '50%'},
                    children=[
                        html.H2('Python库'),
                        html.Ul([html.Li(lib) for lib in CGCNN['python']])
                    ]
                ),
                html.Div(
                    style={'flex': '50%'},
                    children=[
                        html.H2('配置信息'),
                        html.Ul([html.Li(info) for info in CGCNN['配置信息']])
                    ]
                )
            ]
        ),

        html.H2('DIMENET'),
        html.Div(
            style={'display': 'flex'},
            children=[
                html.Div(
                    style={'flex': '50%'},
                    children=[
                        html.H2('Python库'),
                        html.Ul([html.Li(lib) for lib in DIMENET['python']])
                    ]
                ),
                html.Div(
                    style={'flex': '50%'},
                    children=[
                        html.H2('配置信息'),
                        html.Ul([html.Li(info) for info in DIMENET['配置信息']])
                    ]
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
