"""
Conor Doyle
ds3500
HW 2
02/10/2023
"""

# import statements
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import pandas as pd

"""app = dash.Dash(name)

app.layout = html.Div(style={
‘background-image’: ‘url(“diginex.png”)’,
‘background-repeat’: ‘no-repeat’,
‘background-position’: ‘right top’,
‘background-size’: ‘150px 100px’
},children = [
html.H1(‘Hello World’),
html.P(‘This image has an image in the background’)
])

app.run_server(port = 8059)"""

# Read in the csv data
sunspots = pd.read_csv('SN_m_tot_V2.0.csv', delimiter=';', header=None)

# set the rest of the universal variables
time = sunspots[2]
years = sunspots[0]
spots = sunspots[3]
marks = {i: '{}'.format(i) for i in range(years.min(), years.max(), 10)}

deck = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# create the app
app = Dash(__name__)

# define the layout
app.layout = html.Div([
    html.H1(children = "Hello", style = {'textAlign': 'center', 'background-color': 'green'}),
    html.Div(style={
        'background-image': 'url(https://pl.sterlingcdn.com/wp-content/uploads/sites/3/2018/07/blackjack-classic-background.jpg)',
        'background-repeat': 'no-repeat',
        'background-position': 'center t',
        'background-size': '1500px 900px'
        },
             children=[html.Img(src='https://soho.nascom.nasa.gov/data/realtime/hmi_igr/1024/latest.jpg', width='30%', height='30%',
             style={'display': 'inline-block', 'margin-center': '175px', 'margin-bottom': '200px'})]
             ),
    # Create the image and sunspot count figures, and put them side by side


])
"""
html.Img(src='https://soho.nascom.nasa.gov/data/realtime/hmi_igr/1024/latest.jpg', width='30%', height='30%',
             style={'display': 'inline-block', 'margin-center': '75px', 'margin-bottom': '100px'}),
    dcc.Dropdown(id='dropdown',
                 options=[{'label': 'Sunspot activity (monthly)', 'value': 'sunspot_graph'},
                          {'label': 'Sunspot cycle', 'value': 'cycle_graph'}],
                 value='sunspot_graph'),

    dcc.Graph(id='sunspots_line',
              style={'width': '90vh', 'height': '90vh', 'display': 'inline-block', 'margin-left': '200px'}),
    html.H5(children='Time Range'),
    dcc.RangeSlider(years.min(), years.max(), step=None, marks=marks, value=[years.min(), years.max()],
                    id='sunspot_window_slider'),
    html.H5(children='Smoothing Amount'),
    dcc.Slider(1, 12, 1, value=5, id='rolling_window_slider'),
    # create the cycle graph with the necessary sliders
    dcc.Graph(id='cycle_variability',
              style={'width': '125vh', 'height': '90vh', 'display': 'block', 'margin-left': 'auto',
                     'margin-right': 'auto'}),
    html.H5(children='Cycle Year'),
    dcc.Slider(5, 15, 1, value=5, id='cycle_slider'),
    html.H5(children='Cycle Month'),
    dcc.Slider(0, 12, 1, value=0, id='cycle_slider_month'),
    # add references at the bottom
    html.H6(children='Image Source: https://soho.nascom.nasa.gov/data/realtime/realtime-update.html'),
    html.H6(children='Graph Data Source: https://www.sidc.be'),"""

"""
# define how the sunspot number graph reacts to the slider inputs
@app.callback(
    Output('sunspots_line', 'figure'),
    Input('sunspot_window_slider', 'value'),
    Input('rolling_window_slider', 'value')
)
def update_sunspots(slider_vals, rolling_window):
    
    Updates the sunspot graph with the user inputs
    :param slider_vals: the user-defined time range for the graph
    :param rolling_window: the user-defined smoothness level for the rolling average
    :return: the updated figure
    
    # compute the rolling average using the input
    rolling = spots.rolling(window=rolling_window).mean()

    # construct the figure using the original sunspot counts and the rolling average
    fig = go.Figure(
        data=[go.Scatter(x=time, y=spots,
                         mode='lines', name='Monthly'),
              go.Scatter(x=time, y=rolling, name='Smoothed')])

    # resize the window to the user's input, and update title and labels
    fig.update_layout(xaxis_range=slider_vals, title='Monthly Mean Total Sunspots Over Time',
                      xaxis_title='Time (years)',
                      yaxis_title='Sunspot Count')

    return fig


# define how the cycle graph responds to user input
# EXTRA CREDIT: I added the functionality for the user to choose the month on top of the year for the cycles
@app.callback(
    Output('cycle_variability', 'figure'),
    Input('cycle_slider', 'value'),
    Input('cycle_slider_month', 'value')
)
def update_cycles(slider_val_year, slider_val_month, sunspots=sunspots):
    
    Updates the cycle graph to the user inputs
    :param slider_val_year: the user-defined year to measure as the cycle
    :param slider_val_month: the user-defined month to measure as the cycle
    :param sunspots: passed original dataframe
    :return: the updated figure
    
    # compute the modulo of the time period based on the user input
    cycle_year = (slider_val_year + (slider_val_month / 12))
    sunspots = sunspots.assign(overlayed_cycle=time % cycle_year)

    # create the figure
    fig = go.Figure(
        data=[go.Scatter(x=sunspots['overlayed_cycle'], y=spots, mode='markers')]
    )

    # update title, labels
    fig.update_layout(title=f'Sunspot Cycle: {cycle_year}', xaxis_title='Years',
                      yaxis_title='Sunspot Count')

    return fig

"""
def main():
    # run the dashboard
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
