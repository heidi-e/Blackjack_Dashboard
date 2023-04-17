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

new_deck = [{'label': 'A', 'value': 'A'},
        {'label': '2', 'value': '2'},
        {'label': '3', 'value': '3'},
        {'label': '4', 'value': '4'},
        {'label': '5', 'value': '5'},
        {'label': '6', 'value': '6'},
        {'label': '7', 'value': '7'},
        {'label': '8', 'value': '8'},
        {'label': '9', 'value': '9'},
        {'label': '10', 'value': '10'},
        {'label': 'J', 'value': 'J'},
        {'label': 'Q', 'value': 'Q'},
        {'label': 'K', 'value': 'K'}]
# margin = position on the dashboard (up or down)
# margin-left = position left or right
# create the app
app = Dash(__name__)

# define the layout
app.layout = html.Div(
    style={
        'background-image': 'url(https://pl.sterlingcdn.com/wp-content/uploads/sites/3/2018/07/blackjack-classic-background.jpg)',
        'background-repeat': 'no-repeat',
        'background-position': 'center t',
        'background-size': '1500px 900px'},
    children=[
    html.H1(children = "Blackjack Strategy Dashboard", style = {'textAlign': 'center', 'background-color': 'green'}),
    html.Div(id='house',
        children=
        html.Div([
            html.Img(src='https://www.pngall.com/wp-content/uploads/4/Playing-Card-PNG-Clipart.png',
                     style={'width': '10%', 'display':'inline-block', 'float':'left', 'borderRadius': '5px', 'margin': '20px', 'margin-left': '500px'}),
            html.Img(src='https://opengameart.org/sites/default/files/card%20back%20red.png',
                     style={'width': '10%', 'display':'inline-block', 'float':'right', 'borderRadius': '5px', 'margin': '20px', 'margin-right': '500px'}),
            dcc.Dropdown(id = 'house-dropdown', options = new_deck, value = 'A',
                         style = {'width': '20%','display':'inline-block', 'float':'left', 'margin': '0px', 'margin-left': '-60px'}),
            dcc.RadioItems(id='house-suite', options=suite, value='hearts', inline=True,
                           style = {'display':'inline-block', 'float':'left', 'margin': '45px', 'margin-left': '-420px'})
        ]),
    ),
    html.Div(id='user',
        children=
        html.Div([
            html.Img(src='https://www.pngall.com/wp-content/uploads/4/Playing-Card-PNG-Clipart.png',
                     style={'width': '10%', 'display': 'inline-block', 'float': 'bottom-left', 'borderRadius': '5px',
                            'margin': '140px', 'margin-left': '-380px'}),
            html.Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/08_of_spades.svg/800px-08_of_spades.svg.png',
                     style={'width': '10%', 'display': 'inline-block', 'float': 'bottom-right', 'borderRadius': '5px',
                            'margin': '140px', 'margin-left': '30px'}),

            # user hand card on the left
            dcc.Dropdown(id='user-dropdown-1', options= new_deck, value='A',
                         style={'width': '20%', 'display': 'inline-block', 'float': 'left', 'margin': '-70px',
                                'margin-left': '270px'}, optionHeight=30),
            dcc.RadioItems(id='user-suite-1', options=suite, value='hearts', inline=True,
                           style={'display': 'inline-block', 'float': 'left', 'margin': '-90px',
                                  'margin-left': '460px'}),

            # user hand card on the right
            dcc.Dropdown(id='user-dropdown-2', options= new_deck, value='A',
                         style={'width': '20%', 'display': 'inline-block', 'float': 'left', 'margin': '-70px',
                                'margin-left': '435px'}, optionHeight=30),
            dcc.RadioItems(id='user-suite-2', options=suite, value='hearts', inline=True,
                           style={'display': 'inline-block', 'float': 'left', 'margin': '-90px',
                                  'margin-left': '790px'})
        ]),
    )
])

@app.callback(
    Output('house', 'children'),
    Input('house-dropdown', 'value'),
    Input('user-dropdown-1', 'value'),
    Input('user-dropdown-2', 'value'),
    Input('house-suite', 'value')
)


def main():
    # run the dashboard
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
