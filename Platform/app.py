# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:35:50 2019

@author: khoim
"""

import os
import flask
import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd

from random import randint
from pandas import read_csv, DataFrame
from dash.dependencies import Input, Output, State

plotly.tools.set_credentials_file(username='weirdleau', api_key='6OwzPOESWVTBrBSj14BF')

SEVERITY_LOOKUP = {'Fatal' : 'red',
                    'Serious' : 'orange',
                    'Slight' : 'yellow'}

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
Python = [40, 35, 32, 31, 25, 26, 22, 35, 37, 36, 35, 34]
MachineLearning = [27, 23, 10, 16, 17, 14, 21, 25, 26, 19, 18, 11]
Keras = [24, 22, 17, 26, 20, 11, 12, 23, 29, 10, 18, 16]
Tensorflow = [17, 27, 10, 25, 26, 12, 24, 15, 11, 18, 24, 22]
SQL = [26, 17, 27, 20, 10, 16, 18, 13, 28, 14, 22, 12]
Hadoop = [17, 14, 29, 13, 20, 15, 22, 25, 19, 10, 24, 12]

csvLoc = 'data.csv'
dat = read_csv(csvLoc, index_col = 0)
server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', 'secret')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.supress_callback_exceptions = True

app.layout = html.Div(children=[
    html.H1(children='System recommended Jobs'),

    html.Div(children='''This is prototype of Jobs Advising team, not final version'''),

    dbc.Nav(
        [
            dbc.NavItem(dbc.NavLink("Home", active=True, href="#")),
            dbc.DropdownMenu(
                [dbc.DropdownMenuItem("Item 1"), dbc.DropdownMenuItem("Item 2")],
                label="Skills popularity",
                nav=True,
            ),
            dbc.DropdownMenu(
                [dbc.DropdownMenuItem("Item 1"), dbc.DropdownMenuItem("Item 2")],
                label="Job locations",
                nav=True,
            ),
            dbc.DropdownMenu(
                [dbc.DropdownMenuItem("Item 1"), dbc.DropdownMenuItem("Item 2")],
                label="Salary stats",
                nav=True,
            ),
            dbc.NavItem(dbc.NavLink("User account", href="#")),
        ], horizontal = "end",
    ),

    dbc.CardDeck(
    [
        dbc.Card(
            [
                dbc.CardHeader("Python"),
                dbc.CardBody(
                    [
                        dbc.CardTitle("Python là một ngôn ngữ lập trình bậc cao"),
                        dbc.CardText("Python được sử dụng cho các mục đích lập trình đa năng, Python được tạo ra với ưu điểm là dễ đọc, dễ học và dễ nhớ, Python là ngôn ngữ có hình thực rất sáng sửa, cấu trúc rõ ràng, thuận tiện cho người mới học lập trình, cấu trúc của nó còn cho phép người sử dụng viết mã lệnh với số lần gõ phím tối thiểu."),
                    ]
                ),
            ]
        ),
        dbc.Card(
            [
                dbc.CardHeader("SQL"),
                dbc.CardBody(
                    [
                        dbc.CardTitle("SQL là một ngôn ngữ truy vấn, tính cấu trúc dùng để quản lý dữ liệu"),
                        dbc.CardText("Ngôn ngữ cơ sở dữ liệu, được sử dụng để tạo, xóa trong cơ sở dữ liệu, lấy các hàng và sửa đổi các hàng, … SQL dùng để: tạo cơ sở dữ liệu, bảng và view mới, chèn các bản ghi vào trong một cơ sở dữ liệu, xóa các bản ghi từ một cơ sở dữ liệu, lấy dữ liệu từ một cơ sở dữ liệu."),
                    ]
                ),
            ]
        ),
        dbc.Card(
            [
                dbc.CardHeader("Machine Learning"),
                dbc.CardBody(
                    [
                        dbc.CardTitle("Maching learning là một ngành học thuộc khoa học máy tính, giúp máy tính có khả năng tự học mà không phải lập trình một cách rõ ràng"),
                        dbc.CardText("Machine Learning được chia thành 3 loại: Supervised learning (học có giám sát), Unsupervised learning (học không giám sát), Reinforcement learning (học tăng cường/học củng cố)"),
                    ]
                ),
            ]
        ),
        dbc.Card(
            [
                dbc.CardHeader("Hadoop"),
                dbc.CardBody(
                    [
                        dbc.CardTitle("Là một framwork giúp lưu trữ và xử lý Big Data"),
                        dbc.CardText("Nó áp dụng phân tán dữ liệu vì nó tách hết tập hợp các dữ liệu ban đầu thành các dữ liệu nhỏ và sắp xếp lại chúng để dễ dàng tìm kiếm và truy xuất hơn, đặc biệt là việc truy xuất các dữ liệu tương đồng, do Apache phát triển"),
                    ]
                ),
            ]
        ),
    ],style={"max-width": "100%"},
),

    dcc.Graph(
        id='graph city',
        figure={
            'data': [
                {'x': month, 'y': Python, 'type': 'lines', 'name': u'Python'},
                {'x': month, 'y': MachineLearning, 'type': 'lines', 'name': u'Deep learning'},
                {'x': month, 'y': Keras, 'type': 'lines', 'name': u'Java'},
                {'x': month, 'y': Tensorflow, 'type': 'lines', 'name': u'R'},
                {'x': month, 'y': SQL, 'type': 'lines', 'name': u'SQL'},
                {'x': month, 'y': Hadoop, 'type': 'lines', 'name': u'C++'},
            ],
            'layout': {
                'title': 'Độ phổ biến skills qua từng giai đoạn'
            }
        }
    ),

    html.H1(
        'Nhập vào các skill hiện có của bạn',
        style={
            'paddingLeft' : 50,
            }
        ),
    
    html.Div([
        html.Div([  
            dcc.Checklist( 
                options=[
                    {'label': s,
                     'value': s} for s in dat['S'].unique()
                ],
                values=['C++'],
                labelStyle={
                    'display': 'inline-block',
                    'paddingRight' : 10,
                    'paddingLeft' : 10,
                    'paddingBottom' : 5,
                    },
                id="dataChecklist", 
            ),
        ],
        style={
            "width" : '60%',
            'text-size':'54px',
            'display' : 'inline-block', 
            'paddingLeft' : 50, 
            'paddingRight' : 10,
            'boxSizing' : 'border-box',
            }
        ),
    ],
    style={'paddingBottom' : 20}),

    html.Div([ 
        html.Div([  # Holds the barchart
            dcc.Graph(id="Pie",)
        ],
        style={
            "width" : '40%', 
            "height":'150%',
            'float' : 'right', 
            'paddingRight' : 50, 
            'paddingLeft' : 5,
            })

    ]),
])

@app.callback( 
    Output(component_id='Pie', component_property='figure'),
    [Input(component_id='dataChecklist', component_property='values')]
)

def updatePieChart(data):
    df = DataFrame(dat[['S','Points']]
                    [(dat['S'].isin(data))].groupby(['S','Points']).sum()).reset_index()
    p = df['Points']
    s = 0
    for i in p:
        s += i
    
        
    label = ['Xin việc thành công','Xin việc không thành công']
    
    x=int(min(s,99))
    y=int (100-x)

    piedata = go.Pie(values=[x,y], labels=label)
    
    return {
            'data': [piedata],
            'layout': {
                    'height': 550,
                    'margin': {
                            'l': 20,
                            'b': 30, 
                            'r': 10, 
                            't': 10
                            }
                    }
            }

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)