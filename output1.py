import pandas as pd
from sklearn.preprocessing import LabelEncoder, Normalizer
from joblib import dump, load
import base64
import io
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from plotly import graph_objs as go
from app import app

colors = {"background": "#F3F6FA", "background_div": "white"}


new_df = pd.read_csv('new_df.csv')
cal_num_columns = ['Host Response Time','Property Type', 'Room Type', 'Bed Type',
                   'Accommodates', 'Bathrooms','Bedrooms', 'Beds', 'Cleaning Fee',
                   'Guests Included', 'Extra People']

X = pd.read_csv('X.csv')
y = pd.read_csv('y.csv')


def categorical_numerical_encoder(df, num_col=None, cal_col=None):
    cal_enc = LabelEncoder()
    categorical_X = df[cal_col].apply(cal_enc.fit_transform)

    num_enc = Normalizer('max')
    num_enc = num_enc.fit(df[num_col])
    numerical_X = num_enc.transform(df[num_col])
    numerical_X = pd.DataFrame(numerical_X, columns=num_col)

    numerical_X[cal_col] = categorical_X
    X = numerical_X

    return X


layout1 = html.Div([

    # Instruction
    html.Div([
        html.H4('In this page, you could input the data and find the positioning of you listing.')
    ]),
    # Row 1
    html.Div([
        # Accommodates
        html.Div([
            html.H6('Number of accommodates', className="gs-header gs-text-header padded"),
            dcc.Input(id='acc_input', type='number', value=2),
            html.Button(id='acc_button', children='Submit'),
            dcc.Graph(id='acc_graph_with_input',
                      figure={"data": [{
                              "type": 'violin',
                              "x": new_df['Accommodates'],
                              'name': 'Quantity',
                              "box": {
                                  "visible": True
                              },
                              "meanline": {
                                  "visible": True
                              },
                              "opacity": 0.6,
                              "y0": 'Accommodates'
                          }]})
        ], className="four columns"),

        #Bathrooms
        html.Div([
            html.H6('Number of bathrooms', className="gs-header gs-text-header padded"),
            dcc.Input(id='bath_input', type='number', value=1),
            html.Button(id='bath_button', children='Submit'),
            dcc.Graph(id='bath_graph_with_input',
                      figure={"data": [{
                              "type": 'violin',
                              "x": new_df['Bathrooms'],
                              'name': 'Quantity',
                              "box": {
                                  "visible": True
                              },
                              "meanline": {
                                  "visible": True
                              },
                              "opacity": 0.6,
                              "y0": 'Bathrooms'
                          }]})
        ], className="four columns"),

        #Bedrooms
        html.Div([
            html.H6('Number of bedrooms', className="gs-header gs-text-header padded"),
            dcc.Input(id='br_input', type='number', value=1),
            html.Button(id='br_button', children='Submit'),
            dcc.Graph(id='br_graph_with_input',
                      figure={"data": [{
                              "type": 'violin',
                              "x": new_df['Bedrooms'],
                              'name': 'Quantity',
                              "box": {
                                  "visible": True
                              },
                              "meanline": {
                                  "visible": True
                              },
                              "opacity": 0.6,
                              "y0": 'Bedrooms'
                          }]})
        ], className="four columns"),
], className="row"),

    #Row 2
    html.Div([
    #Beds
    html.Div([
        html.H6('Number of beds', className="gs-header gs-text-header padded"),
        dcc.Input(id='b_input', type='number', value=1),
        html.Button(id='b_button', children='Submit'),
        dcc.Graph(id='b_graph_with_input',
                  figure={"data": [{
                          "type": 'violin',
                          "x": new_df['Beds'],
                          'name': 'Quantity',
                          "box": {
                              "visible": True
                          },
                          "meanline": {
                              "visible": True
                          },
                          "opacity": 0.6,
                          "y0": 'Beds'
                      }]})
    ], className="four columns"),

    #Cleaning Fee
    html.Div([
        html.H6('Number of Cleaning Fee', className="gs-header gs-text-header padded"),
        dcc.Input(id='cf_input', type='number', value=10),
        html.Button(id='cf_button', children='Submit'),
        dcc.Graph(id='cf_graph_with_input',
                  figure={"data": [{
                          "type": 'violin',
                          "x": new_df['Cleaning Fee'],
                          'name': 'Quantity',
                          "box": {
                              "visible": True
                          },
                          "meanline": {
                              "visible": True
                          },
                          "opacity": 0.6,
                          "y0": 'Cleaning Fee'
                      }]})
    ], className="four columns"),

    #Guests Included
    html.Div([
        html.H6('Number of Guests Included', className="gs-header gs-text-header padded"),
        dcc.Input(id='gi_input', type='number', value=2),
        html.Button(id='gi_button', children='Submit'),
        dcc.Graph(id='gi_graph_with_input',
                  figure={"data": [{
                          "type": 'violin',
                          "x": new_df['Guests Included'],
                          'name': 'Quantity',
                          "box": {
                              "visible": True
                          },
                          "meanline": {
                              "visible": True
                          },
                          "opacity": 0.6,
                          "y0": 'Guests Included'
                      }]})
    ], className="four columns"),
]),
    #Row 3
    html.Div([
        #Extra People
        html.Div([
            html.H6('Number of Extra People', className="gs-header gs-text-header padded"),
            dcc.Input(id='ep_input', type='number', value=0),
            html.Button(id='ep_button', children='Submit'),
            dcc.Graph(id='ep_graph_with_input',
                      figure={"data": [{
                              "type": 'violin',
                              "x": new_df['Extra People'],
                              'name': 'Quantity',
                              "box": {
                                  "visible": True
                              },
                              "meanline": {
                                  "visible": True
                              },
                              "opacity": 0.6,
                              "y0": 'Extra People'
                          }]})
        ], className="four columns"),
], className="row"),

    #Row 5
    html.Div([
    #Host Response Time
        html.Div([
            html.H6('Host Response Time', className="gs-header gs-text-header padded"),
            dcc.RadioItems(id='rt_input', options=[{'label':i, 'value': i} for i in ['within an hour',
                                                                                     'within a day',
                                                                                     'within a few hours',
                                                                                     'Unknown',
                                                                                     'a few days or more']],
                           value="within an hour",
                           labelStyle={'display': 'inline-block'}
                           ),
            html.Button(id='rt_button', children='Submit'),
            dcc.Graph(id='rt_graph_with_input')
        ], className="six columns"),

        #Property Type
        html.Div([
            html.H6('Property Type', className="gs-header gs-text-header padded"),
            dcc.RadioItems(id='pt_input', options=[{'label': i, 'value': i} for i in ['House','Cabin','Apartment',
                                                                                      'Bungalow','Guesthouse','Loft',
                                                                                      'Bed & Breakfast','Condominium',
                                                                                      'Other','Townhouse','Villa',
                                                                                      'Hostel','Camper/RV','Dorm',
                                                                                      'Serviced apartment','Tent',
                                                                                      'Guest suite','Boutique hotel',
                                                                                      'Lighthouse','Treehouse','Boat',
                                                                                      'Island','Tipi','Timeshare',
                                                                                      'Train','Chalet','Yurt','Earth House',
                                                                                      'Castle','Hut','Vacation home', 'Cave',
                                                                                      'Plane','In-law']],
                           value="House",
                           labelStyle={'display': 'inline-block'}
                           ),
            html.Button(id='pt_button', children='Submit'),
            dcc.Graph(id='pt_graph_with_input')
        ], className="six columns"),
    ], className="row"),

    #Row 6
    html.Div([
        # Property Type
        html.Div([
            html.H6('Room Type', className="gs-header gs-text-header padded"),
            dcc.RadioItems(id='rtt_input', options=[{'label': i, 'value': i} for i in ['Private room', 'Entire home/apt', 'Shared room']],
                           value="Private room",
                           labelStyle={'display': 'inline-block'}
                           ),
            html.Button(id='rtt_button', children='Submit'),
            dcc.Graph(id='rtt_graph_with_input')
        ], className="six columns", style={'display': 'inline-block'}),

        # 'Bed Type'
        html.Div([
            html.H6('Bed Type' , className="gs-header gs-text-header padded"),
            dcc.RadioItems(id='bt_input',
                           options=[{'label': i, 'value': i} for i in ['Real Bed', 'Airbed', 'Futon', 'Pull-out Sofa', 'Couch']],
                           value="Real Bed",
                           labelStyle={'display': 'inline-block'}
                           ),
            html.Button(id='bt_button', children='Submit'),
            dcc.Graph(id='bt_graph_with_input')
        ], className="six columns"),
    ], className="row"),

    #Row 7
    html.Div([
    #Overview of training set
        html.Div([
            html.H6('The training Data sample Overview', className="gs-header gs-text-header padded"),
            dash_table.DataTable(
                id='training_table',
                columns=[{"name": i, "id": i} for i in new_df.columns],
                data=new_df.head().to_dict("rows"),
                style_header={"fontSize":14, "fontWeight":"bold", 'textAlign': 'left'},
                style_cell={'fontSize':14, 'textAlign': 'left'},
            )
        ], className="twelve columns"),
], className="row"),

    #Row 8
    html.Div([
        #live input test set
        html.Div([
            html.H6('Are you willing to insert the data you entered to test set?', className="gs-header gs-text-header padded"),
            html.Button('Confirmed', id='input_new_row', n_clicks=0),
            html.H6('Your test set (editable)'),
            dash_table.DataTable(
                id='adding-rows-table',
                columns=[{"name": i, "id": i} for i in cal_num_columns],
                data=new_df[cal_num_columns].head(1).to_dict("rows"),
                editable=True,
                row_deletable=True,
                style_header={"fontSize":14, "fontWeight":"bold", 'textAlign': 'left'},
                style_cell={'fontSize':14, 'textAlign': 'left'},
            ),
            html.Button('Add Row', id='editing-rows-button', n_clicks=0),
            html.Button('Save the test set', id='trigger_of_saving', n_clicks=0),
        ], className="twelve columns"),
], className="row"),

    #Row 9
    html.Div([
        #Upload data
        html.Div([
            html.H6('Or you could upload your own data in specific format.', className="gs-header gs-text-header padded"),
            dcc.Upload(
                id='datatable-upload',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%', 'height': '60px', 'lineHeight': '60px',
                    'borderWidth': '1px', 'borderStyle': 'dashed',
                    'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'
                },
            ),
            dash_table.DataTable(id='datatable-upload-container'),
        ], className="twelve columns"),
], className="row"),
    html.Div(id='hidden_area', style={'display': 'none'})
])


layout2 = html.Div([
    # Instruction
    html.Div([
        html.H4('In this page, you could train, predict and view the visualization of model training.')
    ]),
    # Row 1
    html.Div([
        # Test set
        html.Div([
            html.H6("You can overview the test data you have submitted.", className="gs-header gs-text-header padded"),
            html.Button('Pass your test data', id='pass_from_output1', n_clicks=0),
            dash_table.DataTable(
                id='raw_test_table',
                columns=[{"name": i, "id": i} for i in cal_num_columns],
                editable=True,
                row_deletable=True,
                style_header={"fontSize":14, "fontWeight":"bold", 'textAlign': 'left'},
                style_cell={'fontSize':14, 'textAlign': 'left'},
            ),

        ], className="twelve columns"),
    ],className="row"),

    #Row 2
    html.Div([
        # Data prepare
        html.Div([
            html.H6("The test data will be encoded and fit the requirement of the training of machine learning.", className="gs-header gs-text-header padded"),
            html.Button('Normalize and label the test data', id='data_prepare'),
            dash_table.DataTable(
                id='normalized_data',
                columns=[{"name": i, "id": i} for i in X.columns],
                editable=False,
                row_deletable=False,
                style_header={"fontSize":14, "fontWeight":"bold", 'textAlign': 'left'},
                style_cell={'fontSize':14, 'textAlign': 'left'},
            )
        ], className='twelve columns'),
    ], className="row"),

    #Row 3
    html.Div([
        html.Div([
            html.H6("Machine Learning Model: Random Forest Regression", className="gs-header gs-text-header padded"),
            html.Button("Plot prediction result of Random Forest Regression", id="trigger_t"),
            dcc.Graph(id="training_point"),
        ])
    ],className="row"),

    #Row 4
    html.Div([

        # Prediction model and result
        html.Div([
            html.H6("Collect the final insight with simple clicks.", className="gs-header gs-text-header padded"),
            html.Button('Predict the result', id='predict_result'),
            dash_table.DataTable(
                id='predicted_result',
                columns=[{"name": "index", "id": "index"},
                         {"name": "Revenue from marketing per day", "id": "Revenue from marketing per day"}],
                editable=False,
                row_deletable=False,
                style_header={"fontSize":14, "fontWeight":"bold", 'textAlign': 'left'},
                style_cell={'fontSize':14, 'textAlign': 'left'},
            )
        ], className='six columns'),


        # The final target
        html.Div([
            html.H6('Please enter the total day of the reservation coming from promotion:', className="gs-header gs-text-header padded"),
            dcc.Input(id='number_of_day', type='number', value=10),
            html.Button('Recommend the appropriate promotional fee to charge', id="trigger_final"),
            dash_table.DataTable(
                id="final_output",
                columns=[{"name":"index", "id":"index"},
                         {"name":"The appropriate promotional fee to charge", "id":"The appropriate promotional fee to charge"}],
                editable=False,
                row_deletable=False,
                style_header={"fontSize":14, "fontWeight":"bold", 'textAlign': 'left'},
                style_cell={'fontSize':14, 'textAlign': 'left'},
            )
        ], className="six columns"),
    ], className="row")
])


# # # # # # # # #
# detail the way that external_css and external_js work and link to alternative method locally hosted
# # # # # # # # #


external_css = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/bcd/pen/KQrXdb.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})



@app.callback(
    Output('acc_graph_with_input', 'figure'),
    [Input('acc_button', 'n_clicks')],
    [State('acc_input', 'value')])
def update_figure(n_clicks, g_input):
    return {"data": [{
                          "type": 'violin',
                          "x": new_df['Accommodates'],
                          'name': 'Number of Accommodates',
                          "box": {
                              "visible": True
                          },
                          "meanline": {
                              "visible": True
                          },
                          "opacity": 0.6,
                          "y0": 'Accommodates'
                      },
                       go.Scatter(
                mode='markers',
                x=[g_input],
                y=['Accommodates'],
                name="Input Value",
                marker=dict(
                    color='red',
                    size=10,
                    line=dict(
                        color='red',
                        width=1)
                )
                       )
    ]}

@app.callback(
    Output('bath_graph_with_input', 'figure'),
    [Input('bath_button', 'n_clicks')],
    [State('bath_input', 'value')])
def update_figure(n_clicks, g_input):
    return {"data": [{
                          "type": 'violin',
                          "x": new_df['Bathrooms'],
                          'name': 'Number of Bathrooms',
                          "box": {
                              "visible": True
                          },
                          "meanline": {
                              "visible": True
                          },
                          "opacity": 0.6,
                          "y0": 'Bathrooms'
                      },
                       go.Scatter(
                mode='markers',
                x=[g_input],
                y=['Bathrooms'],
                name="Input Value",
                marker=dict(
                    color='red',
                    size=10,
                    line=dict(
                        color='red',
                        width=1)
                )
                       )
    ]}

@app.callback(
    Output('br_graph_with_input', 'figure'),
    [Input('br_button', 'n_clicks')],
    [State('br_input', 'value')])
def update_figure(n_clicks, g_input):
    return {"data": [{
                          "type": 'violin',
                          "x": new_df['Bedrooms'],
                          'name': 'Number of Bedrooms',
                          "box": {
                              "visible": True
                          },
                          "meanline": {
                              "visible": True
                          },
                          "opacity": 0.6,
                          "y0": 'Bedrooms'
                      },
                       go.Scatter(
                mode='markers',
                x=[g_input],
                y=['Bedrooms'],
                name="Input Value",
                marker=dict(
                    color='red',
                    size=10,
                    line=dict(
                        color='red',
                        width=1)
                )
                       )
    ]}

@app.callback(
    Output('b_graph_with_input', 'figure'),
    [Input('b_button', 'n_clicks')],
    [State('b_input', 'value')])
def update_figure(n_clicks, g_input):
    return {"data": [{
                          "type": 'violin',
                          "x": new_df['Beds'],
                          'name': 'Number of Beds',
                          "box": {
                              "visible": True
                          },
                          "meanline": {
                              "visible": True
                          },
                          "opacity": 0.6,
                          "y0": 'Beds'
                      },
                       go.Scatter(
                mode='markers',
                x=[g_input],
                y=['Beds'],
                name="Input Value",
                marker=dict(
                    color='red',
                    size=10,
                    line=dict(
                        color='red',
                        width=1)
                )
                       )
    ]}

@app.callback(
    Output('cf_graph_with_input', 'figure'),
    [Input('cf_button', 'n_clicks')],
    [State('cf_input', 'value')])
def update_figure(n_clicks, g_input):
    return {"data": [{
                          "type": 'violin',
                          "x": new_df['Cleaning Fee'],
                          'name': 'Number of Cleaning Fee',
                          "box": {
                              "visible": True
                          },
                          "meanline": {
                              "visible": True
                          },
                          "opacity": 0.6,
                          "y0": 'Cleaning Fee'
                      },
                       go.Scatter(
                mode='markers',
                x=[g_input],
                y=['Cleaning Fee'],
                name="Input Value",
                marker=dict(
                    color='red',
                    size=10,
                    line=dict(
                        color='red',
                        width=1)
                )
                       )
    ]}

@app.callback(
    Output('gi_graph_with_input', 'figure'),
    [Input('gi_button', 'n_clicks')],
    [State('gi_input', 'value')])
def update_figure(n_clicks, g_input):
    return {"data": [{
                          "type": 'violin',
                          "x": new_df['Guests Included'],
                          'name': 'Number of Guests Included',
                          "box": {
                              "visible": True
                          },
                          "meanline": {
                              "visible": True
                          },
                          "opacity": 0.6,
                          "y0": 'Guests Included'
                      },
                       go.Scatter(
                mode='markers',
                x=[g_input],
                y=['Guests Included'],
                name="Input Value",
                marker=dict(
                    color='red',
                    size=10,
                    line=dict(
                        color='red',
                        width=1)
                )
                       )
    ]}


@app.callback(
    Output('ep_graph_with_input', 'figure'),
    [Input('ep_button', 'n_clicks')],
    [State('ep_input', 'value')])
def update_figure(n_clicks, g_input):
    return {"data": [{
                          "type": 'violin',
                          "x": new_df['Extra People'],
                          'name': 'Number of Extra People',
                          "box": {
                              "visible": True
                          },
                          "meanline": {
                              "visible": True
                          },
                          "opacity": 0.6,
                          "y0": 'Extra People'
                      },
                       go.Scatter(
                mode='markers',
                x=[g_input],
                y=['Extra People'],
                name="Input value",
                marker=dict(
                    color='red',
                    size=10,
                    line=dict(
                        color='red',
                        width=1)
                )
                       )
    ]}


@app.callback(
    Output('rt_graph_with_input', 'figure'),
    [Input('rt_button', 'n_clicks')],
    [State('rt_input', 'value')])
def update_figure(n_clicks, g_input):
    label = list(new_df['Host Response Time'].value_counts().index)
    value = list(new_df['Host Response Time'].value_counts())
    return {"data": [go.Pie(labels=label, values=value)]}


@app.callback(
    Output('pt_graph_with_input', 'figure'),
    [Input('pt_button', 'n_clicks')],
    [State('pt_input', 'value')])
def update_figure(n_clicks, g_input):
    label = list(new_df['Property Type'].value_counts().index)
    value = list(new_df['Property Type'].value_counts())
    return {"data": [go.Pie(labels=label, values=value)]}

@app.callback(
    Output('rtt_graph_with_input', 'figure'),
    [Input('rtt_button', 'n_clicks')],
    [State('rtt_input', 'value')])
def update_figure(n_clicks, g_input):
    label = list(new_df['Room Type'].value_counts().index)
    value = list(new_df['Room Type'].value_counts())
    return {"data": [go.Pie(labels=label, values=value)]}


@app.callback(
    Output('bt_graph_with_input', 'figure'),
    [Input('bt_button', 'n_clicks')],
    [State('bt_input', 'value')])
def update_figure(n_clicks, g_input):
    label = list(new_df['Bed Type'].value_counts().index)
    value = list(new_df['Bed Type'].value_counts())
    return {"data": [go.Pie(labels=label, values=value)]}


@app.callback(
    Output('adding-rows-table', 'data'),
    [Input('input_new_row', 'n_clicks'),
     Input('editing-rows-button', 'n_clicks'),
     ],
    [State('adding-rows-table', 'data'),
     State('adding-rows-table', 'columns'),
     State("acc_input", "value"),
     State('bath_input', 'value'),
     State('br_input', 'value'),
     State('b_input', 'value'),
     State('cf_input', 'value'),
     State('gi_input', 'value'),
     State('ep_input', 'value'),
     State('rt_input', 'value'),
     State('pt_input', 'value'),
     State('rtt_input', 'value'),
     State('bt_input', 'value'),]
)
def add_new_row(n_clicks1, n_clicks2, rows, columns,
                accommodates, bathrooms, bedrooms, beds, cleaning_fee, guest_included, extra_people,
                response_time, property_type, room_type, bed_type ):
    if n_clicks1 > 0:
        new_dict = {columns[0]['name']:response_time,
                    columns[1]['name']:property_type,
                    columns[2]['id']:room_type,
                    columns[3]['id']:bed_type,
                    columns[4]['id']:accommodates,
                    columns[5]['id']:bathrooms,
                    columns[6]['id']:bedrooms,
                    columns[7]['id']:beds,
                    columns[8]['id']:cleaning_fee,
                    columns[9]['id']:guest_included,
                    columns[10]['id']:extra_people}
        rows.append(new_dict)
        test_df_from_input = pd.DataFrame(data=rows, index=range(len(rows)))
        test_df_from_input.to_csv('test_df.csv', index=False)
        n_clicks1 = 0

    if n_clicks2 > 0:
        rows.append({c['name']: '' for c in columns})
        n_clicks2 = 0
        n_clicks1 = 0

    return rows


@app.callback(
    Output('hidden_area', 'children'),
    [Input('trigger_of_saving', 'n_clicks')],
    [State('adding-rows-table', 'data'),
     State('adding-rows-table', 'columns')])
def clean_data(n_clicks, rows, columns):
    if n_clicks > 0:
        test_df_from_input = pd.DataFrame(data=rows, index=range(len(rows)))
        test_df_from_input.to_csv('test_df.csv', index=False)
    return test_df_from_input


def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    if 'csv' in filename:
        # Assume that the user uploaded a CSV file
        return pd.read_csv(
            io.StringIO(decoded.decode('utf-8')))
    elif 'xls' in filename:
        # Assume that the user uploaded an excel file
        return pd.read_excel(io.BytesIO(decoded))


@app.callback(Output('datatable-upload-container', 'data'),
              [Input('datatable-upload', 'contents')],
              [State('datatable-upload', 'filename')])
def update_output(contents, filename):
    if contents is None:
        return [{}]
    df = parse_contents(contents, filename)
    return df.to_dict('rows')


@app.callback(Output('raw_test_table', 'data'),
              [Input('pass_from_output1', 'n_clicks')],
              [State('raw_test_table', 'data'),
               State('raw_test_table', 'columns')])
def update_test_df(n_clicks, rows, columns):
    if n_clicks > 0:
        test_df = pd.read_csv('test_df.csv')
        convert_dict = test_df.to_dict("rows")
    return convert_dict


@app.callback(Output('normalized_data', 'data'),
              [Input('data_prepare', 'n_clicks')])
def prepare_test_set(n_clicks):
    if n_clicks > 0:
        categorical_col = ['Host Response Time', 'Property Type', 'Room Type', 'Bed Type']
        numerical_col = ['Accommodates', 'Bathrooms', 'Bedrooms', 'Beds', 'Cleaning Fee', 'Guests Included',
                         'Extra People']
        test_df = pd.read_csv('test_df.csv')
        Encoded_X_test = categorical_numerical_encoder(test_df, num_col=numerical_col, cal_col=categorical_col)

    return Encoded_X_test.to_dict('rows')


@app.callback(Output("training_point", "figure"),
              [Input("trigger_t", "n_clicks")])
def display_random_forest_graph(n_clicks):
    if n_clicks >0:
        rf = load('rf_trained_model.joblib')
        y_test = pd.read_csv('y_test.csv')
        X_test = pd.read_csv("X_test.csv")
        rf_prediction = rf.predict(X_test)
    return {"data": [
            go.Scatter(
                x=list(range(len(rf_prediction))),
                y=list(rf_prediction),
                mode='lines+markers',
                name='Training'),
        go.Scatter(
            x=list(range(len(list(y_test.iloc[:, 0])))),
            y=list(y_test.iloc[:, 0]),
            mode='lines+markers',
            name='Validation',
        )
    ]}






@app.callback(Output('predicted_result', 'data'),
              [Input('predict_result', 'n_clicks')])
def update_predicted_result(n_clicks):
    if n_clicks > 0:
        categorical_col = ['Host Response Time', 'Property Type', 'Room Type', 'Bed Type']
        numerical_col = ['Accommodates', 'Bathrooms', 'Bedrooms', 'Beds', 'Cleaning Fee', 'Guests Included',
                         'Extra People']
        test_df = pd.read_csv('test_df.csv')
        Encoded_X_test = categorical_numerical_encoder(test_df, num_col=numerical_col, cal_col=categorical_col)
        rf = load('rf_trained_model.joblib')
        Encoded_prediction = rf.predict(Encoded_X_test)
        test_dict = {}
        idx_li = list(Encoded_X_test.index)
        pred_li = list(Encoded_prediction)
        test_dict["index"] = idx_li
        test_dict["Revenue from marketing per day"] = pred_li
        tst_df = pd.DataFrame(data=test_dict)
    return tst_df.to_dict('rows')


@app.callback(Output("final_output", "data"),
              [Input("trigger_final", "n_clicks")],
              [State('number_of_day', "value")])
def product_final_output(n_clicks, day):
    if n_clicks > 0:
        test_df = pd.read_csv('test_df.csv')
        categorical_col = ['Host Response Time', 'Property Type', 'Room Type', 'Bed Type']
        numerical_col = ['Accommodates', 'Bathrooms', 'Bedrooms', 'Beds', 'Cleaning Fee', 'Guests Included',
                         'Extra People']
        X_test = categorical_numerical_encoder(test_df, num_col=numerical_col, cal_col=categorical_col)
        rf = load('rf_trained_model.joblib')
        rf_prediction = rf.predict(X_test)
        dd_dict = {}
        idx_li = list(X_test.index)
        pred_li = list(rf_prediction)
        dd_dict["index"] = idx_li
        dd_dict["Revenue from marketing per day"] = pred_li
        test_df = pd.DataFrame(data=dd_dict)
        test_df["The appropriate promotional fee to charge"] = ((day * test_df["Revenue from marketing per day"]) * 0.5)
        output_df = test_df[["index", "The appropriate promotional fee to charge"]]
    return output_df.to_dict("rows")
