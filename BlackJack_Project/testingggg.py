"""
Heidi Eren, Conor Doyle, Kelsey Nihezagirwe, Olivia Mintz
DS3500
Final project dashboard
4/19/23

"""

# import statements
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc


deck = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# margin = position on the dashboard (up or down)

# create the app
app = Dash(__name__)

# define the layout
app.layout = html.Div([
    html.H1(children = "Blackjack Strategy Dashboard", style = {'textAlign': 'center', 'background-color': 'green'}),
    html.Div(
        children=
        html.Div([
            html.Img(src='https://www.pngall.com/wp-content/uploads/4/Playing-Card-PNG-Clipart.png',
                     style={'width': '10%', 'display':'inline-block', 'float':'left', 'borderRadius': '5px', 'margin': '20px', 'margin-left': '500px'}),
            html.Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/08_of_spades.svg/800px-08_of_spades.svg.png',
                     style={'width': '10%', 'display':'inline-block', 'float':'right', 'borderRadius': '5px', 'margin': '20px', 'margin-right': '500px'}),

        ]),

        style={
        'background-image': 'url(https://pl.sterlingcdn.com/wp-content/uploads/sites/3/2018/07/blackjack-classic-background.jpg)',
        'background-repeat': 'no-repeat',
        'background-position': 'center t',
        'background-size': '1500px 900px',

        },
    ),
    html.Div(
        children=
        html.Div([
            html.Img(src='https://www.pngall.com/wp-content/uploads/4/Playing-Card-PNG-Clipart.png',
                     style={'width': '10%', 'display': 'inline-block', 'float': 'bottom-left', 'borderRadius': '5px',
                            'margin': '180px', 'margin-left': '-160px'}),
            html.Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/08_of_spades.svg/800px-08_of_spades.svg.png',
                     style={'width': '10%', 'display': 'inline-block', 'float': 'bottom-right', 'borderRadius': '5px',
                            'margin': '180px', 'margin-left': '0px'})
        ]),
    )
])



def main():
    # run the dashboard
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
