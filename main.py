# main.py
import os
import dash
from dash import html

API_BASE_URL = os.getenv("API_BASE_URL", "")
LOGO_URL = os.getenv("LOGO_URL", "")

dash_app = dash.Dash(__name__)
dash_app.layout = html.Div("Replace this with your full Dash app code")

server = dash_app.server
app = server

if __name__ == "__main__":
    dash_app.run_server(debug=True, port=8050)
