# BlackJack Strategy Dashboard
###please use FULL SCREEN web browser
This is our final project for DS3500 that features the game of blackjack on a Plotly Dashboard, and utilizes the B.O.S.S. (Blackjack Optimal Solution Suggestor) to suggest the next best move the player should play based on the House's hands and the player's hands. 

## Installation
To run the simulation, you will need Python 3 and the following libraries:
```
from dash import Dash, dcc, html, Input, Output
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import pandas as pd
```
## Usage
To start the dashboard, simply run the Blackjack_Dashboard.py file. Note that the dashboard works best on a **full screen** browser. 

The player should select the card value and suit for the house's hands as well as their own hands. The helper will automatically run its genetic algorithm to output the next best move to make a win. We hope you enjoy!
