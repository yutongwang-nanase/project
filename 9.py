import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table

# 定义表格数据
data = [
    {'algorithm': 'MODNet (v0.1.12)', 'mean mae': 0.2711, 'std mae': 1.6832, 'mean rmse': 59.1179,
     'max max_error': None},
    {'algorithm': 'MODNet (v0.1.10)', 'mean mae': 0.2970, 'std mae': 1.7185, 'mean rmse': 58.9519,
     'max max_error': None},
    {'algorithm': 'coGN', 'mean mae': 0.3088, 'std mae': 2.0546, 'mean rmse': 58.7728, 'max max_error': None},
    {'algorithm': 'AMMExpress v2020', 'mean mae': 0.3150, 'std mae': 1.7202, 'mean rmse': 59.0112,
     'max max_error': None},
    {'algorithm': 'Finder_v1.2 structure-based version', 'mean mae': 0.3197, 'std mae': 1.7213, 'mean rmse': 59.0606,
     'max max_error': None},
    {'algorithm': 'Finder_v1.2 composition-only version', 'mean mae': 0.3204, 'std mae': 1.7189, 'mean rmse': 59.0528,
     'max max_error': None},
    {'algorithm': 'CrabNet', 'mean mae': 0.3234, 'std mae': 1.7288, 'mean rmse': 59.1583, 'max max_error': None},
    {'algorithm': 'SchNet (kgcnn v2.1.0)', 'mean mae': 0.3277, 'std mae': 1.8990, 'mean rmse': 58.6071,
     'max max_error': None},
    {'algorithm': 'MegNet (kgcnn v2.1.0)', 'mean mae': 0.3391, 'std mae': 1.9871, 'mean rmse': 59.3095,
     'max max_error': None},
    {'algorithm': 'DimeNet++ (kgcnn v2.1.0)', 'mean mae': 0.3400, 'std mae': 1.9936, 'mean rmse': 58.5416,
     'max max_error': None},
    {'algorithm': 'ALIGNN', 'mean mae': 0.3449, 'std mae': 1.9651, 'mean rmse': 58.7285, 'max max_error': None},
    {'algorithm': 'RF-SCM/Magpie', 'mean mae': 0.4196, 'std mae': 1.8538, 'mean rmse': 59.1201, 'max max_error': None},
    {'algorithm': 'Dummy', 'mean mae': 0.8088, 'std mae': 1.9728, 'mean rmse': 59.6653, 'max max_error': None}
]

# 创建Dash应用程序
app = dash.Dash(__name__, assets_external_path='style')

app.layout = html.Div(
    children=[
        html.H1('表格示例'),
        dash_table.DataTable(
            id='table',
            columns=[{'name': col, 'id': col} for col in data[0].keys()],
            data=data,
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto'
            },
            style_cell={
                'textAlign': 'center',
                'minWidth': '100px',
                'width': '100px',
                'maxWidth': '100px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis'
            },
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold'
            }
        )
    ]
)
if __name__ == '__main__':
    app.run_server(debug=True)
