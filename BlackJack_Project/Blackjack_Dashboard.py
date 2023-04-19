"""
Heidi Eren, Conor Doyle, Kelsey Nihezagirwe, Olivia Mintz
DS3500
Final project dashboard
4/19/23

"""

# card image source: https://code.google.com/archive/p/vector-playing-cards/

from dash import Dash, dcc, html, Input, Output, ctx
from dash import html
from dash import dcc
from dash.dependencies import Output, Input

from strategy import Hand

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


background = 'https://media.istockphoto.com/photos/green-abstract-glass-texture-background-or-pattern-creative-design-picture-id680008334?k=20&m=680008334&s=612x612&w=0&h=P5O3WExGj_3FZyh84I_wfpmNnECNQvy_r_8sBvEjt4M='

# create the app
app = Dash(__name__)

# define the layout
app.layout = html.Div(
    style={
        # set background image
        'background-image': f'url({background})',
        'background-repeat': 'no-repeat',
        'background-position': 'center t',
        'background-size': '1500px 900px'},
    children=[
    html.H1(children = "Blackjack Strategy Dashboard", style = {'textAlign': 'center', 'background-color': 'white'}),
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
                           style = {'display':'inline-block', 'float':'left', 'margin': '0px', 'margin-left': '-260px'}),

            dcc.Markdown('''
            ## Welcome!
            #### (please use FULL SCREEN browser for optimal playing)
            ## How to play:
            * Click to use dropdown feature to select card values
            * Select suit to input card suits
            * The top row is the **house's** hands
            * The bottom row is **your** hands
            #### Click on the buttons below for more help.
            ''', style = {'float':'left', 'margin': '-280px', 'margin-left': '-690px', 'background-color': 'white'}),
            dcc.Markdown(id='rules-text',
                         style = {'float':'left', 'margin': '100px', 'margin-left': '-690px', 'background-color': 'white', 'width': '200px'}),
            html.Button('Rules', id='rules-button', n_clicks=0,
                        style = {'float':'left', 'margin': '100px', 'margin-left': '-690px'})
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
                            'margin': '100px', 'margin-left': '-120px'}),

            # user card on the left
            dcc.Dropdown(id='user-dropdown-1', options= new_deck, value='4',
                         style={'width': '20%', 'display': 'inline-block', 'float': 'left', 'margin': '60px',
                                'margin-left': '-170px'}),
            dcc.RadioItems(id='user-suit-1', options=suit, value='clubs', inline=True,
                           style={'display': 'inline-block', 'float': 'left', 'margin': '-90px',
                                  'margin-left': '460px'}),

            # user card on the right
            dcc.Dropdown(id='user-dropdown-2', options= new_deck, value='8',
                         style={'width': '20%', 'display': 'inline-block', 'float': 'left', 'margin': '-150px',
                                'margin-left': '500px'}, maxHeight=100),
            dcc.RadioItems(id='user-suit-2', options=suit, value='hearts', inline=True,
                           style={'display': 'inline-block', 'float': 'left', 'margin': '-90px',
                                  'margin-left': '800px'}),
            dcc.Markdown(id='helper-text',
                         style = {'float':'left', 'margin': '-680px', 'margin-left': '1100px', 'background-color': 'white'}),
            dcc.Markdown(id='helper-guide-text', style={'float': 'left', 'margin': '-180px', 'margin-left': '16px',
                                    'background-color': 'white'}),
            html.Button('Helper', id='helper-button', n_clicks=0,
                        style = {'float':'left', 'margin': '-180px', 'margin-left': '16px'})

        ]),
    )
])

@app.callback(
    Output('house', 'src'),
    Output('user-1', 'src'),
    Output('user-2', 'src'),
    Output('helper-text', 'children'),
    Output('rules-text', 'children'),
    Output('helper-guide-text', 'children'),

    Input('house-dropdown', 'value'),
    Input('house-suit', 'value'),

    Input('user-dropdown-1', 'value'),
    Input('user-suit-1', 'value'),

    Input('user-dropdown-2', 'value'),
    Input('user-suit-2', 'value'),

    Input('rules-button', 'n_clicks'),
    Input('helper-button', 'n_clicks')


)

def update_card(house_val, house_suit, user_1_val, user_1_suit, user_2_val, user_2_suit, n_click_1, n_click_2):
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

    # fix output of ace cards
    if house_val == 'ace':
        house_val = 'A'

    if user_1_val == 'ace':
        user_1_val = 'A'

    if user_2_val == 'ace':
        user_2_val = 'A'

    # determine user's hands
    hand = Hand(user_1_val, user_2_val)

    # run optimal solution
    helper = hand.get_action(house_val)

    if n_click_1 % 2 > 0:
        msg_1 = '#### Sum as close to 21 as possible, without going over. ' \
              'Ace is worth 1 or 11. ' \
              'Face cards are 10.'
        return house_card_path, user_card_1_path, user_card_2_path, ' Your next play should be **{}** '.format(helper), msg_1, ''
    elif n_click_2 % 2 > 0:

        msg_3 = ''' #### BOSS Guide
                    * Stand = not ask for card
                    * Hit = ask for card
                    * Split = separate two hands
                    * Double-down = double your bet
                    * Pair = bet for first two cards dealt being a pair
                '''

        return house_card_path, user_card_1_path, user_card_2_path, ' Your next play should be **{}** '.format(helper), '', msg_3
    else:
        return house_card_path, user_card_1_path, user_card_2_path, ' Your next play should be **{}** '.format(helper), '', ''




def main():
    # run the dashboard
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
