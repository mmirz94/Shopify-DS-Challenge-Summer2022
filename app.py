from defaults import *

app = dash.Dash(__name__, title = "Shopify DS Challenge", update_title= None, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_folder= "assets")
server = app.server

body = html.Div(
    [
        html.Div(
            [],
        style={'height':'1px'}
        ),
        html.Div(
            [
                html.A(
                    html.Img(src=app.get_asset_url('shopify_logo.png'), height="80px",style={'margin-left':'1rem', 'display':'inline-block'}),
                    href='https://www.shopify.ca/careers'
                ),
                html.P("Shopify Data Scientist Challenge for Summer 2022 Data Science Internship",
                       style= {'fontWeight': 'bold', 'font-size': '17px', 'color': colors['text'],
                               'margin-left': '3px', 'font-family': 'cursive', 'display':'inline-block'})
            ]
        ),
        html.Div(
            [
                html.P("Initial statistical analysis of the data:",
                       style={'fontWeight': 'bold', 'font-size': '17px', 'color': colors['text'], 'margin-top': '1rem',
                              'margin-left': '1rem', 'backgroundColor': colors['bg_color'], 'font-family': 'cursive'})
            ]
        ),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P("Statistical metrics",
                                       style = {'font-family': 'cursive', 'font-size': '17px',
                                        'color':colors['text'], 'margin-left':'1rem'}),
                                html.Div(
                                    default_data_stats_table('initial_stats'),
                                    id='initial_stats_table_container',
                                    style={'margin-left':'1rem'}
                                )
                            ],
                            width=3
                        ),
                        dbc.Col(
                            [
                                dcc.Graph(id='initial_histogram',
                                          config={'displayModeBar': False},
                                          style = {'width':'97%', 'backgroundColor': colors['bg_color']}
                                         )
                            ],
                            width=9
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.P("Share of each shop from total sales",
                                               style = {'font-family': 'cursive', 'font-size': '17px',
                                                         'color':colors['text'], 'margin-left':'1rem'}),
                                        dash_charts.pie(
                                            id="pie_chart", width='480px', height='350px',
                                            data=[["shop_sales","Count"]], title = None,
                                            is3D= True, pieHole=0, backgroundColor=colors['bg_color'], legendTextColor=colors['text'],
                                            slices_color = {0:{'color':pie_chart_colors[0]},1:{'color':pie_chart_colors[1]},2:{'color':pie_chart_colors[2]}}
                                        )
                                    ]
                                )
                            ],
                            width=3
                        ),
                        dbc.Col(
                            [
                                dcc.Graph(id='bar_chart',
                                          config={'displayModeBar': False},
                                          style={'width': '97%', 'backgroundColor': colors['bg_color']}
                                          )
                            ],
                            width=9
                        )
                    ]
                )
            ]
        ),
        html.Div(
            [
                dbc.Card(
                    [
                        html.P("Insights:", style={'fontWeight': 'bold', 'font-size': '15px', 'color': colors['text'],
                                       'margin-left': '1rem', 'font-family': 'cursive', 'margin-top':'5px'}),
                        html.Ul(
                            [
                                html.Li('Looking at the Min and Max values of "Total Items" it can be seen that there are shops that sell sneakers in large quantities'),
                                html.Li('Looking at the Min, Max, and std of "Order Amount" it can easily be concluded that mean is not a good metric for reporting the average order value(AOV) as the shops with high sales volume affect the average value of an order considerably'),
                                html.Li('''std (standard deviation) of "Order Amount" suggests that the distribution of the orders' value covers a wide range of values and sales values are distant from each other.'''),
                                html.Li("Log scale histogram of the sales also confirms the above conclusion and shows a few orders with very large values"),
                                html.Li("Pie chart ilustrated the share of each shop from the total sales. Shop number 42 and shop number 78 are the ones whose orders are increasing the AOV"),
                                html.Li("Bar chart depicts the sales of each shop in detail and provides more in depth understanding of the data"),
                                html.Li("Considering all of the points above, Median of 284 is a much better estimate of AOV.")
                            ],
                            style={'color':colors['text'], 'margin-right':'3%', 'font-family': 'cursive'}
                        ),
                    ],
                    style={'width':'97%', 'margin-left':'1rem','backgroundColor': colors['bg_color'], 'border-color': colors['text']}
                ),
                dbc.Card(
                    [
                        html.P("Actions:", style={'fontWeight': 'bold', 'font-size': '15px', 'color': colors['text'],
                                       'margin-left': '1rem', 'font-family': 'cursive', 'margin-top':'5px'}),
                        html.Ul(
                            [
                                html.Li('Remove orders that are above $1000'),
                                html.Li('Explore how the distance between Mead and Median changes as a result of data cleaning'),
                                html.Li('Find the most probable regions based on Probability Density Function (PDF) and report what AOV a new shop would probably achieve')
                            ],
                            style={'color':colors['text'], 'margin-right':'3%', 'font-family': 'cursive'}
                        ),
                    ],
                    style={'width':'97%', 'margin-left':'1rem', 'backgroundColor': colors['bg_color'],
                           'border-color': colors['text'], 'margin-top':'1rem'}
                )

            ],
            style={'margin-top':'1rem'}
        ),
        html.Hr(style={'color':colors['text'], 'opacity':1}),
        html.P("Data Cleaning:",
               style={'fontWeight': 'bold', 'font-size': '17px', 'color': colors['text'], 'margin-top': '1rem',
                      'margin-left': '1rem', 'backgroundColor': colors['bg_color'], 'font-family': 'cursive'}),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(id='Box_plot',
                                    config={'displayModeBar': False},
                                    style={'width': '97%', 'backgroundColor': colors['bg_color'],'margin-left':'1rem'}
                                )
                            ],
                            width=3
                        ),
                        dbc.Col(
                            [
                                dcc.Graph(id='PDF_and_hist',
                                    config={'displayModeBar': False},
                                    style={'width': '97%', 'backgroundColor': colors['bg_color']}
                                )
                            ],
                            width=9
                        )
                    ]
                )
            ]
        ),
        html.Div(
            [
                dbc.Card(
                    [
                        html.P("Insights:", style={'fontWeight': 'bold', 'font-size': '15px', 'color': colors['text'],
                                                   'margin-left': '1rem', 'font-family': 'cursive',
                                                   'margin-top': '5px'}),
                        html.Ul(
                            [
                                html.Li('Looking at the box plot, it can be seen that there are still outlier in the data set and further cleaning can be useful'),
                                html.Li(
                                    'Looking at the estimated PDF, it can be concluded that [130,170] and [270-360] regions are the most probable regions for the value of orders respectively'),
                            ],
                            style={'color': colors['text'], 'margin-right': '3%', 'font-family': 'cursive'}
                        ),
                    ],
                    style={'width': '97%', 'margin-left': '1rem', 'backgroundColor': colors['bg_color'],
                           'border-color': colors['text']}
                ),
                dbc.Card(
                    [
                        html.P("Actions:", style={'fontWeight': 'bold', 'font-size': '15px', 'color': colors['text'],
                                                  'margin-left': '1rem', 'font-family': 'cursive',
                                                  'margin-top': '5px'}),
                        html.Ul(
                            [
                                html.Li('Keep the orders in the Median +/- (1.5*IQ) where IQ is interquartile range'),
                            ],
                            style={'color': colors['text'], 'margin-right': '3%', 'font-family': 'cursive'}
                        ),
                    ],
                    style={'width': '97%', 'margin-left': '1rem', 'backgroundColor': colors['bg_color'],
                           'border-color': colors['text'], 'margin-top': '1rem'}
                )

            ],
            style={'margin-top': '1rem'}
        ),

        html.Hr(style={'color':colors['text'], 'opacity':1}),
        html.P("Final analysis and conclusion:",
               style={'fontWeight': 'bold', 'font-size': '17px', 'color': colors['text'], 'margin-top': '1rem',
                      'margin-left': '1rem', 'backgroundColor': colors['bg_color'], 'font-family': 'cursive'}),

        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P("Final data statistical metrics",
                                       style = {'font-family': 'cursive', 'font-size': '17px',
                                        'color':colors['text'], 'margin-left':'1rem'}),
                                html.Div(
                                    default_data_stats_table('final_stats'),
                                    style={'margin-left':'1rem'}
                                )
                            ],
                            width=3
                        ),
                        dbc.Col(
                            [
                                dbc.Card(
                                    [
                                        html.P("Conclusion:", style={'fontWeight': 'bold', 'font-size': '15px',
                                                                  'color': colors['text'],
                                                                  'margin-left': '1rem', 'font-family': 'cursive',
                                                                  'margin-top': '5px'}),
                                        html.Ul(
                                            [
                                                html.Li('At this point both Median and Mean are reasonable values and can be reported as evaluation metric (272 and 283 respectively)'),
                                                html.Li('most of the orders filled by the current shops are in the $[130-170] or $[270-360] ranges'),
                                                html.Li('2 out of 100 shops have 90.6% of total sales recorded and are most likely distributors')
                                            ],
                                            style={'color': colors['text'], 'margin-right': '3%',
                                                   'font-family': 'cursive'}
                                        ),
                                    ],
                                    style={'width': '97%', 'backgroundColor': colors['bg_color'],
                                           'border-color': colors['text'], 'margin-top':'41px'}
                                )
                            ],
                            width=9
                        )
                    ]
                )
            ]
        ),

        html.Div(id='initializer', style={'margin-bottom':'1rem'})
    ],
    style={'backgroundColor': colors['bg_color'], 'height':'100vh', 'overflow-x':'hidden'}
)

app.layout = body

@app.callback(
    [
        Output("initial_stats","data"),
        Output("initial_histogram", "figure"),
        Output("pie_chart","data"),
        Output("bar_chart","figure")
    ],
    [
        Input("initializer", "style")
    ]
)
def update_initial_stats_components(initializer):
    sneaker_shops_data = pd.read_csv(os.path.join(PATH_DATA, "data.csv"))
    stats = sneaker_shops_data.loc[:, ['order_amount', 'total_items']].describe().reset_index()
    stats.columns = ['metric', 'order_amount', 'total_items']

    initial_hist = plot_histogram(sneaker_shops_data, "order_amount")

    shops_total_sales = sneaker_shops_data.loc[:, ["shop_id", "order_amount"]].groupby(by="shop_id").sum() \
        .sort_values(by='order_amount', ascending=False).reset_index()

    pie_chart_threshold = shops_total_sales['order_amount'].sum() * 0.01
    shops_total_sales.loc[shops_total_sales['order_amount'] < pie_chart_threshold, 'shop_id'] = 'other shops'
    shops_total_sales = shops_total_sales.groupby(by='shop_id').sum().reset_index()
    pie_data = [["shop_sales","Count"]] + [[str(shops_total_sales.loc[i, 'shop_id']), shops_total_sales.loc[i, 'order_amount']] for i in range(len(shops_total_sales))]



    AOV_shops_detailed = sneaker_shops_data.loc[:, ["shop_id", "order_amount"]].groupby(by="shop_id").mean() \
        .sort_values(by='order_amount', ascending=False).reset_index()
    bar_chart = plot_stores_sales_bar_chart(AOV_shops_detailed)


    return stats.to_dict('records'), initial_hist, pie_data, bar_chart


@app.callback(
    [
        Output("Box_plot","figure"),
        Output("PDF_and_hist","figure")
    ],
    [
        Input("initializer", "style")
    ]
)
def update_final_components(initializer):
    sneaker_shops_data = pd.read_csv(os.path.join(PATH_DATA, "data.csv"))
    cleaned_data = sneaker_shops_data[sneaker_shops_data["order_amount"] < 1000]
    box_plot = plot_box_plot(cleaned_data)

    PDF_plot = PDF(cleaned_data)

    return box_plot, PDF_plot


@app.callback(
    Output("final_stats", "data"),
    [
        Input("initializer", "style")
    ]
)
def final_analysis(initializer):
    sneaker_shops_data = pd.read_csv(os.path.join(PATH_DATA, "data.csv"))
    cleaned_data = sneaker_shops_data[sneaker_shops_data["order_amount"] < 1000]
    quantiles = cleaned_data['order_amount'].quantile([0.25,0.5,0.75])
    IQ= quantiles[0.75] - quantiles[0.25]
    final_data = cleaned_data[(cleaned_data['order_amount']<quantiles[0.5]+(1.5*IQ)) & (cleaned_data['order_amount']>quantiles[0.5]-(1.5*IQ))]

    stats = final_data.loc[:, ['order_amount', 'total_items']].describe().reset_index()
    stats.columns = ['metric', 'order_amount', 'total_items']

    return stats.to_dict('records')





if __name__ == "__main__":
    app.run_server(debug=False)