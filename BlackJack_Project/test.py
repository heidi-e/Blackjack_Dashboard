"""
Heidi Eren, Conor Doyle, Kelsey Nihezagirwe, Olivia Mintz
DS3500
Final project dashboard
4/19/23

"""

import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc


# button features
suit = ['hearts', 'clubs', 'spades', 'diamonds']

# dropdown features
new_deck = [{'label': 'A', 'value': 'ace'},
        {'label': '2', 'value': '2'},
        {'label': '3', 'value': '3'},
        {'label': '4', 'value': '4'},
        {'label': '5', 'value': '5'},
        {'label': '6', 'value': '6'},
        {'label': '7', 'value': '7'},
        {'label': '8', 'value': '8'},
        {'label': '9', 'value': '9'},
        {'label': '10', 'value': '10'},
        {'label': 'J', 'value': 'jack'},
        {'label': 'Q', 'value': 'queen'},
        {'label': 'K', 'value': 'king'}]

# margin = position on the dashboard (up or down)
# margin-left = position left or right

# create the app
app = Dash(__name__)

# define the layout
app.layout = html.Div(
    style={
        # set background image
        'background-image': 'url(https://pl.sterlingcdn.com/wp-content/uploads/sites/3/2018/07/blackjack-classic-background.jpg)',
        'background-repeat': 'no-repeat',
        'background-position': 'center t',
        'background-size': '1500px 900px'},
    children=[
    html.H1(children = "Blackjack Strategy Dashboard", style = {'textAlign': 'center', 'background-color': 'green'}),
    html.Div(children=
        html.Div([
            # house's hands
            html.Img(id='house', src='assets/3_of_spades.png',
                     style={'width': '10%', 'display':'inline-block', 'float':'left', 'borderRadius': '5px', 'margin': '60px', 'margin-left': '500px'}),
            html.Img(src='https://opengameart.org/sites/default/files/card%20back%20red.png',
                     style={'width': '10%', 'display':'inline-block', 'float':'right', 'borderRadius': '5px', 'margin': '60px', 'margin-right': '500px'}),
            dcc.Dropdown(id = 'house-dropdown', options = new_deck, value = '3',
                         style = {'width': '20%','display':'inline-block', 'float':'left', 'margin': '-25px', 'margin-left': '-80px'}),
            dcc.RadioItems(id='house-suit', options=suit, value='spades', inline=True,
                           style = {'display':'inline-block', 'float':'left', 'margin': '0px', 'margin-left': '-260px'})
        ]),
    ),
    html.Div(children=
        html.Div([
            # user's hands
            html.Img(id='user-1', src='assets/4_of_clubs.png',
                     style={'width': '10%', 'display': 'inline-block', 'float': 'left', 'borderRadius': '5px',
                            'margin': '100px', 'margin-left': '-200px'}),
            html.Img(id='user-2', src='assets/8_of_hearts.png',
                     style={'width': '10%', 'display': 'inline-block', 'float': 'bottom-right', 'borderRadius': '5px',
                            'margin': '100px', 'margin-left': '40px'}),

            # user card on the left
            dcc.Dropdown(id='user-dropdown-1', options= new_deck, value='4',
                         style={'width': '20%', 'display': 'inline-block', 'float': 'left', 'margin': '20px',
                                'margin-left': '200px'}, optionHeight=30),
            dcc.RadioItems(id='user-suit-1', options=suit, value='clubs', inline=True,
                           style={'display': 'inline-block', 'float': 'left', 'margin': '-90px',
                                  'margin-left': '460px'}),

            # user card on the right
            dcc.Dropdown(id='user-dropdown-2', options= new_deck, value='8',
                         style={'width': '20%', 'display': 'inline-block', 'float': 'left', 'margin': '-70px',
                                'margin-left': '420px'}, optionHeight=30),
            dcc.RadioItems(id='user-suit-2', options=suit, value='hearts', inline=True,
                           style={'display': 'inline-block', 'float': 'left', 'margin': '-90px',
                                  'margin-left': '790px'})
        ]),
    )
])

@app.callback(
    Output('house', 'src'),
    Output('user-1', 'src'),
    Output('user-2', 'src'),

    Input('house-dropdown', 'value'),
    Input('house-suit', 'value'),

    Input('user-dropdown-1', 'value'),
    Input('user-suit-1', 'value'),

    Input('user-dropdown-2', 'value'),
    Input('user-suit-2', 'value'),

)

def update_card(house_val, house_suit, user_1_val, user_1_suit, user_2_val, user_2_suit):
    """ update card images based on user input values
    :param house_val (int): the house card value
    :param house_suit (str): the house card suit
    :param user_1_val, user_2_val (int): the user card value
    :param user_1_suit, user_2_suit (str): the user card suit
    """

    # update card images based on input values
    house_card = f"{house_val}_of_{house_suit}.png"
    user_card_1 = f"{user_1_val}_of_{user_1_suit}.png"
    user_card_2 = f"{user_2_val}_of_{user_2_suit}.png"

    # set direct image path
    house_card_path = f"assets/{house_card}"
    user_card_1_path = f"assets/{user_card_1}"
    user_card_2_path = f"assets/{user_card_2}"
    return house_card_path, user_card_1_path, user_card_2_path


def main():
    # run the dashboard
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
