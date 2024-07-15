from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

import plots as pt

app = Dash(external_stylesheets=[dbc.themes.SLATE])

# app.layout = [
#     html.H1(children='People are dumb', style={'text-align':'center'}),
#     dcc.Dropdown(options=['Sort by sale price', 'Sort by rent price'], value='Sort by sale price', id='controls-and-radio-item'),
#     dcc.Dropdown([4,5,6]),
#     dcc.Graph(id='region_price', figure=pt.fig_region_price,style={'width':'90vw'}),
#     dcc.Graph(id='province_price', figure=pt.fig_province_price,style={'width':'90vw'}),
#     dcc.Graph(id='district_price', figure=pt.fig_district_price,style={'width':'90vw'})
# ]
app.layout = dbc.Container(
    [
        dbc.Row([html.H1(children='Analysis of the belgian house market', style={'text-align':'center'})]),
        dbc.Row([html.H2(children='People cannot encode on Immoweb', style={'text-align':'center'})]),
        dbc.Row(
            [
                dbc.Col(
                    html.Div("Sort by :")
                ),
                dbc.Col(
                    dcc.Dropdown(options=['Sale price', 'Rent price'], value='Sale price', id='controls-and-radio-item')
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id='region_price', figure=pt.fig_region_price,style={'height':'60vh'}),
                    width = 4
                ),
                dbc.Col(
                    dcc.Graph(id='province_price', figure=pt.fig_province_price,style={'height':'60vh'}),
                    width = 4
                ),
                dbc.Col(
                    dcc.Graph(id='district_price', figure=pt.fig_district_price,style={'height':'60vh'}),
                    width = 4
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(figure=pt.fig_sale_municipalities, style={'height' :'100vh'}))]),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(figure=pt.fig_rent_municipalities, style={'height' :'100vh'})
                )
            ]
        ),
        dbc.Row(
            dcc.Graph(id='url_price',figure=pt.fig_url,style={'height' :'100vh'})
        )
    ],
    fluid=True
)

@callback(
    Output(component_id='region_price', component_property='figure'),
    Output(component_id='province_price', component_property='figure'),
    Output(component_id='district_price', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    if 'Sale' in col_chosen:
        arrayR = pt.price_sale_region['Region']
        arrayP = pt.price_sale_province['Province']
        arrayD = pt.price_sale_district['District']
    else:
        arrayR = pt.price_rent_region['Region']
        arrayP = pt.price_rent_province['Province']
        arrayD = pt.price_rent_district['District']
    pt.fig_region_price.update_layout(
        xaxis=dict(
                categoryarray=arrayR
            )
    )
    pt.fig_province_price.update_layout(
        xaxis=dict(
                categoryarray=arrayP
            )
    )
    pt.fig_district_price.update_layout(
        xaxis=dict(
                categoryarray=arrayD
            )
    )
    return pt.fig_region_price, pt.fig_province_price, pt.fig_district_price

if __name__ == '__main__':
    app.run(debug=True)