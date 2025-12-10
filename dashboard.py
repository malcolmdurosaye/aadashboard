import os
import dash
from dash import html

API_BASE_URL = os.getenv("API_BASE_URL", "https://accelerate-africa-data-api.onrender.com")
LOGO_URL = os.getenv("LOGO_URL", "")

dash_app = dash.Dash(__name__)

dash_app.layout = html.Div([
    html.H2("Accelerate Africa Dashboard"),
    html.P("Replace this file with your full Dash application code.")
])

server = dash_app.server  # WSGI server for Vercel
