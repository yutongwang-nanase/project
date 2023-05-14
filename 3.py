import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Iframe(
    src='assets/index.html',
    style={'width': '1800px', 'height': '2200px', 'border': 'none'}
)

if __name__ == '__main__':
    app.run_server(debug=False, host='127.0.0.1', port=8089)
