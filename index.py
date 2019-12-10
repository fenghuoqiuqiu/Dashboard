#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__mtime__ = '2019/5/14'

"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from datetime import datetime
from flask import session
import mysql_db


from app import dash_app
from apps import app1,app2,app3,app4,app5,app6,app7,app8,app9,app10,app11,app12,app13,app14,app15,app16


dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])

colors={'background': '#111111','text': '#7FDBFF'}
number_map={'0':'一','1':'二','2':'三','3':'四','4':'五'}

# Update the index
@dash_app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    df = mysql_db.data_get(session['username'])
    children = []
    for i, j in enumerate(df['content'].unique()):
        i = number_map[str(i)]
        update_content = html.P('{0}.{1}'.format(i, j))
        children.append(update_content)
        for m, n in enumerate(df[df['content'] == j][['app_name', 'link']].values):
            m = str(m + 1)
            update_content = dcc.Link(html.P('{0}.{1}'.format(m, n[1]), style={'text-indent': '2em'}),
                                      href='/apps/{0}'.format(n[0]))
            children.append(update_content)
        children.append(html.Br())

    index_layout = html.Div([
        html.H2('目录', style={
            'textAlign': 'left'}),
        html.Br(),
        html.Div(children,
            style={'font-size': '20px', 'textAlign': 'left'})],
        style={'margin': '2%'})


    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/app3':
        return app3.layout
    elif pathname == '/apps/app4':
        return app4.layout
    elif pathname == '/apps/app5':
        return app5.layout
    elif pathname == '/apps/app6':
        return app6.layout
    elif pathname == '/apps/app7':
        return app7.layout
    elif pathname == '/apps/app8':
        return app8.layout
    elif pathname == '/apps/app9':
        return app9.layout
    elif pathname == '/apps/app10':
        return app10.layout
    elif pathname == '/apps/app11':
        return app11.layout
    elif pathname == '/apps/app12':
        return app12.layout
    elif pathname == '/apps/app13':
        return app13.layout
    elif pathname == '/apps/app14':
        return app14.layout
    elif pathname == '/apps/app15':
        return app15.layout
    elif pathname == '/apps/app16':
        return app16.layout
    else:
        return index_layout

