import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash import dash_table
from dash.dash_table.Format import Format, Group
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os
import pathlib
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_charts
import plotly.figure_factory as ff

#############################
PATH = pathlib.Path(__file__).parent
PATH_DATA=os.path.join(PATH,"assets")
colors={'bg_color':'#383e45', 'text':'#ffffff', 'shopify_green':'#96bf48'}
pie_chart_colors= ['#f0e6ce', '#008060', '#96bf48']
#############################

def default_data_stats_table(id):
    stocks_table_columns = [
        {'id': 'metric', 'name': 'Metric'},
        {'id': 'order_amount', 'name': 'Order Amount', 'type': 'numeric',
         'format': Format(precision=8, group=Group.yes, groups=3, group_delimiter=',', decimal_delimiter='.')},
        {'id': 'total_items', 'name': 'Total Items', 'type': 'numeric',
         'format': Format(precision=8, group=Group.yes, groups=3, group_delimiter=',', decimal_delimiter='.')}]
    initial_stats_table = dash_table.DataTable(
        id=id,
        columns=stocks_table_columns,
        sort_action="native",
        sort_mode="multi",
        row_deletable=False,
        style_table={'height': '280px', 'overflowY': 'auto'},
        style_header={'backgroundColor': colors['shopify_green'], 'fontWeight': 'bold', 'font_family': 'cursive',
                      'font_size': '17px', 'textAlign': 'center', 'color': colors['text']},
        style_data={'font_family': 'cursive', 'font_size': '14px', 'textAlign': 'center'},
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(220,224,230)'
            }
        ]
    )
    return initial_stats_table

def plot_histogram(data, x):
    fig = px.histogram(data, x=x, color_discrete_sequence=[colors['shopify_green']], log_y=True)
    fig.update_layout(
        title = "Histogram of the orders' value",
        margin=dict(t=25, r=0, l=0, b=0),
        paper_bgcolor=colors['bg_color'],
        plot_bgcolor=colors['bg_color'],
        font_family="cursive",
        font_color=colors['text'],
        yaxis=dict(
            title="Count(Log scale)",
            showticklabels=True,
            color=colors['text']
        ),
        xaxis=dict(
            title = 'Order Amount',
            showticklabels=True,
            color=colors['text'],
            showline=True,
            showdividers=True
        )
    )
    return fig


def plot_stores_sales_bar_chart(data):
    fig = px.bar(data, x='shop_id', y='order_amount', log_y=True, color_discrete_sequence=[colors['shopify_green']])
    fig.update_layout(
        title="Average order value (AOV) for each shop",
        margin=dict(t=25, r=0, l=0, b=0),
        paper_bgcolor=colors['bg_color'],
        plot_bgcolor=colors['bg_color'],
        font_family="cursive",
        font_color=colors['text'],
        yaxis=dict(
            title="AOV(Log scale)",
            showticklabels=True,
            color=colors['text']
        ),
        xaxis=dict(
            title="Shop ID",
            showticklabels=True,
            color=colors['text'],
            showline=True,
            showdividers=True
        )
    )
    return fig


def plot_box_plot(data):
    data_mean = data["order_amount"].mean()
    fig = px.box(data, y="order_amount", color_discrete_sequence=[colors['shopify_green']])
    fig.layout.xaxis2 = go.layout.XAxis(overlaying='x', range=[0, 2], showticklabels=False)
    fig.add_scatter(x=[0, 2], y=[data_mean, data_mean], mode='lines', xaxis='x2',
                    showlegend=False, line=dict(dash='dash', color="red", width=2))
    fig.add_annotation(x=1.9, y=data_mean + 35,
                       text="Mean", xref='x2',
                       font=dict(family="cursive", size=12, color="red"),
                       showarrow=False)
    fig.update_layout(
        title="Distribution of the order values after data cleaning",
        margin=dict(t=25, r=0, l=0, b=0),
        paper_bgcolor=colors['bg_color'],
        plot_bgcolor=colors['bg_color'],
        font_family="cursive",
        font_color=colors['text'],
        yaxis=dict(
            title="Order Amount",
            showticklabels=True,
            color=colors['text']
        ),
        xaxis=dict(
            showticklabels=True,
            color=colors['text'],
            showline=True,
            showdividers=True,
        )
    )
    fig.update_xaxes(showgrid=False)
    return fig

def PDF(data):
    hist_data = []
    order_amounts = data['order_amount'].values
    hist_data.append(list(order_amounts)) #hist__data must be a list of lists
    group_labels = ['Shopify Sneakers shops'] #name for the PDF we are estimating, you can use multiple data sets all in one plot
    fig = ff.create_distplot(hist_data, group_labels, bin_size=20, show_rug=False, show_curve=True, show_hist=True,
                             colors=[colors['shopify_green']])

    fig.update_layout(
        title="Probability Density Function (PDF) of the order values",
        margin=dict(t=25, r=0, l=0, b=0),
        paper_bgcolor=colors['bg_color'],
        plot_bgcolor=colors['bg_color'],
        font_family="cursive",
        font_color=colors['text'],
        yaxis=dict(
            title="Order Amount",
            showticklabels=True,
            color=colors['text']
        ),
        xaxis=dict(
            showticklabels=True,
            color=colors['text'],
            showline=True,
            showdividers=True,
        )
    )
    fig.update_xaxes(showgrid=False)
    return fig