import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from SqlConnect import getData

df = getData()
column_names_list = list(df.columns.values)
column_names_count = len(column_names_list)
# (GameName) AS 'Game Name Count', GameName AS 'Game Name', Denom AS 'Denom', Bet AS 'Bet', AI AS 'AI' "

app = dash.Dash(__name__)

app.layout = html.Div([

    (html.Label('Skynet Data Result',
                style={'fontSize': 24, 'color': 'black', 'text-align': 'center', 'display': 'block'})),

    dash_table.DataTable(
        id='skynet-datatable',

        columns=[
            {"name": i, "id": i, "deletable": True} for i in df.columns],

        data=df.to_dict("rows"),
        editable=True,
        filtering=False,
        sorting=True,
        sorting_type="multi",
        row_selectable="multi",
        row_deletable=True,
        selected_rows=[],
        pagination_mode="fe",
        pagination_settings={
            "displayed_pages": 1,
            "current_page": 0,
            "page_size": 35,
        },
        navigation="page",

        n_fixed_rows=1,
        style_table={'overflowX': 'scroll'},
        style_cell_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)',
                'if': {'row_index': 'even'},
                'backgroundColor': 'rgb(148, 148, 148)'

            }],
        style_cell={
            'backgroundColor': 'rgb(50, 50, 50)',
            'color': 'white',
            'minWidth': '0px', 'maxWidth': '40px',
            'whiteSpace': 'normal',
            'textOverflow': 'ellipsis',
            'textAlign': 'left'
        },
        style_header={
            'backgroundColor': 'black',
            'fontWeight': 'bold'
        },
    ),

    html.Div(id='datatable-interactivity-container')
])

if __name__ == '__main__':
    app.run_server(debug=True)
