import plotly.express as px
import plotly.graph_objects as go

from data_cleaning import sale_data, rent_data, municipality_price_m2, municipality_price_m2_rent

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
        y=1.3,
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
        y=1.3,
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
        y=1.3,
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

sale_data["length_url"] = sale_data["Url"].apply(len)
sale_data = sale_data.groupby("length_url",as_index=False)[["Price"]].mean().sort_values("length_url",ascending=False)
rent_data["length_url"] = rent_data["Url"].apply(len)
rent_data = rent_data.groupby("length_url",as_index=False)[["Price"]].mean().sort_values("length_url",ascending=False)

fig_url = go.Figure()
fig_url.add_trace(go.Bar(
    x=sale_data["length_url"],y=sale_data["Price"],
    offsetgroup=1,
    name='Sale',
    marker=dict(
            color=colors[0]
        )))
fig_url.add_trace(go.Bar(
    x=rent_data["length_url"],y=rent_data["Price"],
    offsetgroup=2,
    yaxis='y2',
    name='Rent',
    marker=dict(
            color=colors[1]
        )))
fig_url.update_layout(
    title='Average price by length of the URL',
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
        title='Monthly rent in €')
)
fig_sale_municipalities = px.scatter(data_frame=municipality_price_m2,x="Nom commune",y= "€/m2",color='Province',title='Sale price per m² by municipalities')
fig_rent_municipalities = px.scatter(data_frame=municipality_price_m2_rent,x="Nom commune",y= "€/m2",color='Province',title='Rent price per m² by municipalities')