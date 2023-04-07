"""
Heidi Eren
DS3500
HW2
2/10/23
"""

from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd


def read_solar():
    """ Read in the sundash dataset to make
    interactive features more responsive """
    solar_data = pd.read_csv('SN_m_tot_V2.0.csv', sep=";", names=['Year', 'Month', 'Date', 'Sunspot',
                                                                  'Std', '# Observations', 'Marker'])

    return solar_data


# Read the Solar data
solar_data = read_solar()

# Create app
app = Dash(__name__)

# set layout of dashboard
app.layout = html.Div([html.H2('Solar Influences Data Analysis Center - Royal Observatory in Belgium'),
                       html.H3('Monitoring and Analyzing Solar Activity'),
                       html.H5('By Heidi Eren'),

                       dcc.Tabs(id='tabs', value='tab_1', children=[

                           # first tab features
                           dcc.Tab(label='Sunspot Activity', value='tab_1', children=[
                               html.Div([
                                   html.H3('Interactive Sunspot Dashboard'),
                                   html.P('Sunspot Index and Long-term Solar Observations'),
                                   html.Label(['Select a figure:'], style={'font-weight': 'bold'}),
                                   dcc.Dropdown(
                                       id='dropdown',
                                       options=[
                                           {'label': 'Sunspot activity (monthly)', 'value': 'sunspot_graph'},
                                           {'label': 'Sunspot cycle', 'value': 'cycle_graph'}],
                                       value='sunspot_graph'),
                                   # set graph and include sliders
                                   dcc.Graph(id="graph", style={'width': '70vw', 'height': '90vh'}),
                                   html.P("Select range of years:"),
                                   dcc.RangeSlider(id='time', min=solar_data['Year'].min(), max=solar_data['Year'].max(), step=1,
                                                   value=[1950, 2021],
                                                   tooltip={"placement": "bottom", "always_visible": True}, marks=None),
                                   html.P("Select number of months (observation period):"),
                                   dcc.Slider(id='num_months', min=1, max=12, step=1, value=3),
                                   html.P("Select the cycle period:"),
                                   dcc.Slider(id='cycle_period', min=1, max=20, step=1, value=11)
                               ])
                           ]),

                           # second tab features
                           dcc.Tab(label='Real-Time Images', value='tab_2', children=[
                               html.Div([
                                   html.P('NASA’s Solar and Heliospheric Observatory (SOHO)'),
                                   html.H1('Real-time Sun Image'),
                                   html.Img(src='https://soho.nascom.nasa.gov/data/realtime/hmi_igr/1024/latest.jpg',
                                            style={'width': '40%'})
                               ])
                           ])
                       ])
                    ])


def smooth_data(solar_data, num_months):
    """ Smooth data by taking the running average based on the inputted number of months,
    create new column for the smoothed sunspot numbers
    Args:
        solar_data (df): sundash dataframe
        num_months (int): number of months to take running average
    """

    solar_data['Smooth_Sunspot'] = solar_data['Sunspot'].rolling(num_months).mean()

    return solar_data


def filter_cycle(solar_data, cycle_period):
    """ Convert each date to a fractional year based on cycle period
    Args:
        solar_data (df): sundash dataframe
        cycle_period (int): cycle length period
    """

    solar_data['Period'] = solar_data['Date'] % cycle_period

    return solar_data

@app.callback(
    Output('graph', 'figure'),
    [Input('time', 'value')],
    Input('num_months', 'value'),
    Input('dropdown', 'value'),
    Input('cycle_period', 'value'),

)

def display_figure(time, num_months, value, cycle_period):
    """ Display figures based on dropdown selection
    Args:
        time (lst): the selected range of years, a list of 2 values
        num_months (int): number of months to take the running average
        value (obj): dropdown feature, selects the graph
        cycle_period (int): cycle length period
    """

    solar_data = read_solar()

    # subset the df to be within the selected range of years
    solar_data = solar_data[(solar_data['Year'] > time[0]) & (solar_data['Year'] <= time[1])]

    # smooth the df based on the selected number of months
    smoothed_solar_data = smooth_data(solar_data, num_months)

    # filter the df based on the cycle period
    filtered_data = filter_cycle(solar_data, cycle_period)

    # Generate figure
    fig = go.Figure()

    if value == 'sunspot_graph':
        # Add monthly line
        fig.add_trace(go.Scatter(x=list(solar_data.Date),
                                 y=list(solar_data.Sunspot),
                                 name='Monthly'))
        # Add smoothed monthly line
        fig.add_trace(go.Scatter(x=list(smoothed_solar_data.Date),
                                 y=list(smoothed_solar_data.Smooth_Sunspot),
                                 name='Smoothed'))
        # Add labels
        fig.update_layout(
            title_text='International Sunspot Number: '
                       'Monthly Mean and {}-Month Smoothed Number'.format(num_months),
            xaxis_title='Time (years)',
            yaxis_title='Sunspot Number',
            showlegend=True)

        return fig

    elif value == 'cycle_graph':
        # Add scatterplot
        fig.add_trace(go.Scatter(
            x=list(filtered_data.Period),
            y=list(filtered_data.Sunspot),
            mode="markers"))
        # Add labels
        fig.update_layout(
            title_text='Sunspot Cycle: {}'.format(cycle_period),
            xaxis_title='Years',
            yaxis_title='# of Sunspots')

        return fig

def main():
    # Run app
    app.run_server(debug=True)

main()
