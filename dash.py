import dash
import dash_core_components as dcc
from dash import html
import pandas as pd

df_sgo = pd.read_csv('C:/Users/Tomasz/zad/export_danych.csv')

df_sgo_frame = pd.DataFrame(df_sgo)

# Import
import_df_sgo_frame = df_sgo_frame[df_sgo_frame['NAZWA'] == 'Import']

import_df_sgo_frame_all = import_df_sgo_frame[['PROCES', 'NAZWA', 'CZAS_PODPROCESU', 'DATA_LADOWANIA']]

# Parametry wejściowe
param_df_sgo_frame = df_sgo_frame[df_sgo_frame['NAZWA'] == ' Parametry wejściowe']

param_df_sgo_frame_all = param_df_sgo_frame[['PROCES', 'NAZWA', 'CZAS_PODPROCESU', 'DATA_LADOWANIA']]


# Aplikacja 
app = dash.Dash(__name__)

app.layout = html.Div ([
    html.H1 ('Usuwanie danych z bazy'),
    dcc.Graph(
    id='dataframe-graph',
    figure={
        'data': [{
            'type': 'table',
            'header': {
                'values': import_df_sgo_frame_all.columns
            },
            'cells': {
                'values': import_df_sgo_frame_all.values.T,
            }
        }]
    }
), 
 html.Div([
        dcc.Graph(
            id='dataframe-graph-2',
            figure={
                'data': [{
                    'type': 'table',
                    'header': {
                        'values': param_df_sgo_frame_all.columns
                    },
                    'cells': {
                        'values': param_df_sgo_frame_all.values.T
                    }
                }],
            }
        )
    ], style={'marginTop': '-230px'}) 
])



if __name__ == '__main__':
    app.run_server(debug=True)