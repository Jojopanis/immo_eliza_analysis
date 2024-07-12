import plotly.express as px
import plotly.graph_objects as go

from data_cleaning import sale_data, rent_data

colors = px.colors.qualitative.Vivid

price_sale_region = sale_data.groupby("Region", as_index=False)[["Price"]].mean().round()
price_rent_region = rent_data.groupby("Region", as_index=False)[["Price"]].mean().round()

fig_region_price = go.Figure()
fig_region_price.add_trace(
    go.Bar(
        x=price_sale_region['Region'],
        y=price_sale_region['Price'],
        name='Sale',
        offsetgroup=1,
        marker=dict(
            color=colors[0]
        )
    )
)
fig_region_price.add_trace(
    go.Bar(
        x=price_rent_region['Region'],
        y=price_rent_region['Price'],
        name='Rent',
        yaxis='y2',
        offsetgroup=2,
        marker=dict(
            color=colors[1]
        )
    )
)
fig_region_price.update_traces(
    hovertemplate='<b>%{y:,.0f} €</b>'
)
fig_region_price.update_layout(
    title='Average price per region',
    # width = 800,
    legend=dict(
        x=0.5,
        y=1.1,
        orientation='h',
        xanchor='center'
    ),
    yaxis=dict(
        gridcolor=colors[0],
        color=colors[0],
        title='Sale price in €'
    ),
    yaxis2=dict(
        overlaying='y',
        side='right',
        gridcolor=colors[1],
        color=colors[1],
        title='Monthly rent in €'
    ),
        xaxis=dict(
        categoryorder='array',
    ),
    bargap=0.1,
    bargroupgap=0.05,
    hovermode='x unified',
)

price_sale_province = sale_data.groupby("Province", as_index=False)[["Price"]].mean().round().sort_values("Price",ascending=False)
price_rent_province = rent_data.groupby("Province", as_index=False)[["Price"]].mean().round().sort_values("Price",ascending=False)

fig_province_price = go.Figure()
fig_province_price.add_trace(
    go.Bar(
        x=price_sale_province['Province'],
        y=price_sale_province['Price'],
        name='Sale',
        offsetgroup=1,
        marker=dict(
            color=colors[0]
        )
    )
)
fig_province_price.add_trace(
    go.Bar(
        x=price_rent_province['Province'],
        y=price_rent_province['Price'],
        name='Rent',
        yaxis='y2',
        offsetgroup=2,
        marker=dict(
            color=colors[1]
        )
    )
)
fig_province_price.update_traces(
    hovertemplate='<b>%{y:,.0f} €</b>',   
)
fig_province_price.update_layout(
    title='Average price per province',
    # width = 800,
    legend=dict(
        x=0.5,
        y=1.1,
        orientation='h',
        xanchor='center'
    ),
    yaxis=dict(
        gridcolor=colors[0],
        color=colors[0],
        title='Sale price in €'
    ),
    yaxis2=dict(
        overlaying='y',
        side='right',
        gridcolor=colors[1],
        color=colors[1],
        title='Monthly rent in €'
    ),
    xaxis=dict(
        categoryorder='array',
    ),
    bargap=0.1,
    bargroupgap=0.05,
    hovermode='x unified',
)

price_sale_district = sale_data.groupby("District", as_index=False)[["Price"]].mean().round().sort_values("Price",ascending=False)
price_rent_district = rent_data.groupby("District", as_index=False)[["Price"]].mean().round().sort_values("Price",ascending=False)

fig_district_price = go.Figure()
fig_district_price.add_trace(
    go.Bar(
        x=price_sale_district['District'],
        y=price_sale_district['Price'],
        name='Sale',
        offsetgroup=1,
        marker=dict(
            color=colors[0]
        )
    )
)
fig_district_price.add_trace(
    go.Bar(
        x=price_rent_district['District'],
        y=price_rent_district['Price'],
        name='Rent',
        yaxis='y2',
        offsetgroup=2,
        marker=dict(
            color=colors[1]
        )
    )
)
fig_district_price.update_traces(
    hovertemplate='<b>%{y:,.0f} €</b>',   
)
fig_district_price.update_layout(
    title='Average price per district',
    # width = 800,
    legend=dict(
        x=0.5,
        y=1.15,
        orientation='h',
        xanchor='center'
    ),
    yaxis=dict(
        gridcolor=colors[0],
        color=colors[0],
        title='Sale price in €'
    ),
    yaxis2=dict(
        overlaying='y',
        side='right',
        gridcolor=colors[1],
        color=colors[1],
        title='Monthly rent in €'
    ),
    xaxis=dict(
        categoryorder='array',
    ),
    bargap=0.1,
    bargroupgap=0.05,
    hovermode='x unified',
)