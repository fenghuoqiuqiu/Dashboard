#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jinxinlei'
__mtime__ = '2019/4/28'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              xx      xx
            xxxxxxxxx
            x      x      x
            x  xx  xx  x
            x      x      x
            xxx      xxx
                x      xxxxx
                x  xxxx    xx
                xxxxBUGx   xx
                xxxxxxxxx
                  xxx  xxx
                  xxx  xxx
"""


import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from app import dash_app

colors = {'background': '#111111', 'text': '#7FDBFF'}

df1 = pd.read_excel("excels/person_application/xxxx1.xlsx", index_col=0)
df2 = pd.read_excel("excels/person_application/xxxx2.xlsx", index_col=0)
df3 = pd.read_excel("excels/person_application/xxxx3.xlsx", index_col=0)
df4 = pd.read_excel("excels/person_application/xxxx4.xlsx", index_col=0)
# month = df['xxxx'].unique()

layout = html.Div([
    html.H3(id='title_app12', children=["xxxxxxxx"],
            style={
                'textAlign': 'left',
                'color': colors['text']
            }),
    html.H4("xxxxxx"),

    html.H6("1xxxxxxxxxxxx"),
    html.Div([
        dcc.Graph(id='graph1_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='graph2_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right', 'padding': '0 20'}),

    html.H6("2xxxxxxxxxxxxxxxxxxx"),
    html.Div([
        dcc.Graph(id='graph3_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='graph4_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right', 'padding': '0 20'}),


    html.H4("xxxxxxxx"),

    html.H6("1xxxxxxxxxxxx"),
    html.Div([
        dcc.Graph(id='graph2_1_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='graph2_2_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right', 'padding': '0 20'}),

    html.H6("2xxxxxxxxxxxx"),
    html.Div([
        dcc.Graph(id='graph2_3_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='graph2_4_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right', 'padding': '0 20'}),

    html.H6("3xxxxxxxx"),
    html.Div([
        dcc.Graph(id='graph2_5_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='graph2_6_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right', 'padding': '0 20'}),

    html.H6("xxx", style={'font-family': 'SimHei', 'font-size': '22px'}),
    html.P("xxxxxxxxxxxxxx", style={'font-family': 'STKaiti', 'font-size': '16px'}),
    html.Div([
        html.Div([
            html.Label('xxxx', style={'font-family': 'SimHei', 'font-size': '22px'}),
            dcc.Checklist(
                id='zflx_app12',
                options=[
                    {'label': 'xx', 'value': 'xx'},
                    {'label': 'xxx', 'value': 'xxx'}],
                values=['xx', 'xxx'],
                labelStyle={'display': 'inline'}),
            html.Label('xx', style={'font-family': 'SimHei', 'font-size': '22px'}),
            dcc.Checklist(
                id='tc_app12',
                options=[{'label': 'x', 'value': 1}, {'label': 'x', 'value': 0}],
                values=[0, 1],
                labelStyle={'display': 'inline'}),
            html.Label('xxxx', style={'font-family': 'SimHei', 'font-size': '22px'}),
            dcc.Checklist(
                id='ywlx_app12',
                options=[{'label': i, 'value': i} for i in ['xxx', 'xxxxx', 'xxx']],
                values=['xxx', 'xxxxx', 'xxx'],
                labelStyle={'display': 'inline'}),
            html.Label('xxxx', style={'font-family': 'SimHei', 'font-size': '22px'}),
            dcc.Checklist(
                id='qudao_app12',
                options=[{'label': a, 'value': a} for a in ('xx', 'xx', 'xxx', 'xxx')],
                values=['xx', 'xx', 'xxx', 'xxx'],
                labelStyle={'display': 'inline'}),
            html.Label(' xxxx', style={'font-family': 'SimHei', 'font-size': '22px'}),
            dcc.Checklist(
                id='cllx_app12',
                options=[{'label': i, 'value': i} for i in ['xxx', 'xx', 'xxx']],
                values=['xxx', 'xx', 'xxx'],
                labelStyle={'display': 'inline'}),
            html.Label('xx', style={'font-family': 'SimHei', 'font-size': '22px'}),
            dcc.Checklist(
                id='diqu_app12',
                options=[{'label': i, 'value': i} for i in ['xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx']],
                values=['xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx'],
                labelStyle={'display': 'inline'})],
            style={'columnCount': 3})]),

    html.H4("xxDetailxxxx"),

    html.H6("xxxxxxxx"),
    html.H6("1xxxxxxxx"),
    html.Div([
        dcc.Graph(id='graph3_1_app12')
    ], style={'width': '48%', 'padding': '0 20'}),

    html.H6("2xxxxxxx"),
    html.Div([
        dcc.Dropdown(id='riqi_dropdown_app12',
                     options=[{'label': i, 'value': i} for i in df1['xxxx'].sort_values(ascending=False).unique()],
                     value=df1['xxxx'].max(),
                     )], style={'width': '30%'}),

    html.Div([
        dcc.Graph(id='graph3_2_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='graph3_3_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right', 'padding': '0 20'}),

    html.H6("xxxxxDetail"),

    html.Div([
        html.Label('xxxx', style={'font-family': 'SimHei'}),
    ], style={'display': 'inline-block'}),
    html.Div([
        dcc.RadioItems(
            id='qunti_app12',
            options=[ {'label': 'xx', 'value': 'xx'},{'label': 'xx', 'value': 'xx'}],
            value='xx',
            labelStyle={'display': 'inline'})
    ], style={'display': 'inline-block'}),

    html.H6("1xxxxxxx"),
    html.Div([
        dcc.Graph(id='graph3_4_app12')
    ], style={'width': '90%', 'padding': '0'}),
    # html.H6("4xxxxxxxxxxx"),
    html.Div([
        dcc.Graph(id='graph3_5_app12')
    ], style={'width': '90%', 'padding': '0 20'}),

    html.H6("2xxxxxxxxxxx"),
    html.Div([
        dcc.Graph(id='graph3_6_app12')
    ], style={'width': '90%', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='graph3_7_app12')
    ], style={'width': '90%', 'padding': '0 20'}),

    html.H6("3xxxxxxxxxxxxx"),
    html.Div([
        dcc.Graph(id='graph3_8_app12')
    ], style={'width': '90%', 'padding': '0 20'}),

    html.H6("4xxxxxxxxx"),
    html.Div([
        dcc.Graph(id='graph3_9_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='graph3_10_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right', 'padding': '0 20'}),

    html.H6("5xxxxxxxxxx"),
    html.Div([
        dcc.Graph(id='graph3_11_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='graph3_12_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right', 'padding': '0 20'}),

    html.H6("6xxxxx"),
    html.Div([
        dcc.Graph(id='graph3_13_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='graph3_14_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right', 'padding': '0 20'}),

    html.H6("7xxxxxxx"),
    html.Div([
        dcc.Graph(id='graph3_15_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='graph3_16_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right', 'padding': '0 20'}),

    html.H6("8xxxxx"),
    html.Div([
        dcc.Graph(id='graph3_17_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='graph3_18_app12')
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right', 'padding': '0 20'}),
], style={'margin-left': '3%', 'margin-right': '3%', 'margin-bottom': '5%'})


@dash_app.callback(
    Output('graph1_app12', 'figure'),
    [Input('title_app12', 'children')])
def update_graph1(title):
    df = pd.read_excel("excels/person_application/xx_xxxx.xlsx", index_col=0)
    data = []
    x = df['xx'].values
    y = df['xxx'].values
    num_nticks = len(x)
    data.append(go.Bar(x=x, y=y, width=0.5))
    return {
        'data': data,
        'layout': go.Layout(title='xxxxxx',
                            titlefont=dict(color='rgb(148, 103, 189)', size=20),
                            height=600,
                            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
                            xaxis=dict(
                                nticks=num_nticks + 1,
                                tickangle=-30,
                                tickfont=dict(size=13)),
                            annotations=[{
                                'x': -0.05, 'y': -0.20, 'xanchor': 'left', 'yanchor': 'bottom',
                                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                                'font': {'size': 16, 'family': 'STKaiti'},
                                'text': 'xxxxxxxxxxxxxxxxxxx'
                            }],
                            yaxis=dict(  # title='xxx',
                                # tickformat = '%',
                                # tickformat = 'd',
                                nticks=4,
                                titlefont=dict(color='rgb(148, 103, 189)', size=14),  # xxxxxxxxxxxxx
                                tickfont=dict(size=13),  # xxxxxxxxxxxx
                                autorange=True))}


@dash_app.callback(
    Output('graph2_app12', 'figure'),
    [Input('title_app12', 'children')])
def update_graph1(title):
    df = pd.read_excel("excels/person_application/xx_xxxx.xlsx", index_col=0)
    data = []
    x = df['xx'].values
    y = df['xxx'].values
    num_nticks = len(x)
    data.append(go.Bar(x=x, y=y, width=0.5))
    return {
        'data': data,
        'layout': go.Layout(title='xxxxxxx',
                            titlefont=dict(color='rgb(148, 103, 189)', size=20),
                            height=600,
                            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
                            xaxis=dict(
                                nticks=num_nticks + 1,
                                tickangle=-30,
                                tickfont=dict(size=13)),
                            yaxis=dict(  # title='xxx',
                                # tickformat = '%',
                                # tickformat = 'd',
                                nticks=4,
                                # titlefont=dict(color='rgb(148, 103, 189)',size=14),#xxxxxxxxxxxxx
                                tickfont=dict(size=13),  # xxxxxxxxxxxx
                                autorange=True))}


@dash_app.callback(
    Output('graph3_app12', 'figure'),
    [Input('title_app12', 'children')])
def update_graph1(title):
    df = pd.read_excel("excels/person_application/xx_xxxx.xlsx", index_col=0)
    data = []
    x = df['xx'].values
    num_nticks = len(x)
    y1 = df['xx'].values
    y2 = (df['xxx'] * 100).round(2).values
    data.append(go.Bar(x=x, y=y1, width=0.5, name='xx'))
    data.append(go.Scatter(x=x, y=y2, yaxis='y2', name='xxx(%)'))  #
    return {
        'data': data,
        'layout': go.Layout(title='xxxxxxxxx',
                            titlefont=dict(color='rgb(148, 103, 189)', size=20),
                            height=600,
                            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
                            legend=dict(orientation="h"),  # ,x=0, y=1.1
                            xaxis=dict(
                                nticks=num_nticks + 1,
                                tickangle=-30,
                                tickfont=dict(size=13)),
                            yaxis=dict(  # title='xxx',
                                nticks=4,
                                # titlefont=dict(color='rgb(148, 103, 189)',size=14),#xxxxxxxxxxxxx
                                tickfont=dict(size=13),  # xxxxxxxxxxxx
                                showgrid=True,
                                autorange=True),
                            yaxis2=dict(overlaying='y',
                                        side='right',  # xxxx
                                        # tickformat = 'p', #'%'#'d'
                                        titlefont=dict(color='rgb(148, 103, 189)', size=14),  # xxxxxxxxxxxxx
                                        tickfont=dict(color='rgb(148, 103, 189)', size=12),  # xxxxxxxxxxxx
                                        autorange=False, range=[50, 80],
                                        showgrid=False))}


@dash_app.callback(
    Output('graph4_app12', 'figure'),
    [Input('title_app12', 'children')])
def update_graph1(title):
    df = pd.read_excel("excels/person_application/xx_xxxx.xlsx", index_col=0)
    data = []
    x = df['xx'].values
    num_nticks = len(x)
    y1 = df['xx'].values
    y2 = (df['xxx'] * 100).round(2).values
    data.append(go.Bar(x=x, y=y1, width=0.5, name='xx'))
    data.append(go.Scatter(x=x, y=y2, yaxis='y2', name='xxx(%)'))  #
    return {
        'data': data,
        'layout': go.Layout(title='xxxxxxxxx',
                            titlefont=dict(color='rgb(148, 103, 189)', size=20),
                            height=600,
                            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
                            legend=dict(orientation="h"),  # ,x=0, y=1.1
                            xaxis=dict(
                                nticks=num_nticks + 1,
                                tickangle=-30,
                                tickfont=dict(size=13)),
                            yaxis=dict(  # title='xxx',
                                nticks=4,
                                # titlefont=dict(color='rgb(148, 103, 189)',size=14),#xxxxxxxxxxxxx
                                tickfont=dict(size=13),  # xxxxxxxxxxxx
                                showgrid=True,
                                autorange=True),
                            yaxis2=dict(overlaying='y',
                                        side='right',  # xxxx
                                        # tickformat = 'p', #'%'#'d'
                                        titlefont=dict(color='rgb(148, 103, 189)', size=14),  # xxxxxxxxxxxxx
                                        tickfont=dict(color='rgb(148, 103, 189)', size=12),  # xxxxxxxxxxxx
                                        autorange=False, range=[50, 80],
                                        showgrid=False))}

@dash_app.callback(
    Output('graph2_1_app12', 'figure'),
    [Input('zflx_app12', 'values')])
def update_graph1(zflx):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df1.groupby(['xxxx', 'xxxx'])['xxx'].sum().reset_index()
    dff['xxxx'] = dff.groupby(['xxxx'])['xxx'].transform(lambda x: x / x.sum())
    dff['xxxx'] = (dff['xxxx'] * 100).round(2)
    dff = dff.groupby(['xxxx', 'xxxx'])['xxxx'].sum().unstack().fillna(0)
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(dff.columns):  # dff.columns
        y = dff[j].values
        data.append(go.Scatter(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            title='xxxxxx',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            height=500,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            xaxis=dict(
                tickformat='%Y%m',
                showgrid=False,
                nticks=20,
                tickangle=-30,
                tickfont=dict(size=13)),
            yaxis=dict(
                tickfont=dict(size=13),  # xxxxxxxxxxxx
                autorange=True))}


@dash_app.callback(
    Output('graph2_2_app12', 'figure'),
    [Input('zflx_app12', 'values')])
def update_graph1(zflx):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df1.groupby(['xxxx', 'xxxx'])['xxx'].sum().reset_index()
    dff['xxxx'] = dff.groupby(['xxxx'])['xxx'].transform(lambda x: x / x.sum())
    dff['xxxx'] = (dff['xxxx'] * 100).round(2)
    dff = dff.groupby(['xxxx', 'xxxx'])['xxxx'].sum().unstack().fillna(0)
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(dff.columns):  # dff.columns
        y = dff[j].values
        data.append(go.Scatter(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            title='xxxxxx',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            height=500,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            xaxis=dict(
                tickformat='%Y%m',
                showgrid=False,
                nticks=20,
                tickangle=-30,
                tickfont=dict(size=13)),
            yaxis=dict(
                tickfont=dict(size=13),  # xxxxxxxxxxxx
                autorange=True))}


@dash_app.callback(
    Output('graph2_3_app12', 'figure'),
    [Input('zflx_app12', 'values')])
def update_graph1(zflx):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df1.groupby(['xxxx', 'xxxx'])['xxx'].sum().reset_index()
    dff['xxxx'] = dff.groupby(['xxxx'])['xxx'].transform(lambda x: x / x.sum())
    dff['xxxx'] = (dff['xxxx'] * 100).round(2)
    dff = dff.groupby(['xxxx', 'xxxx'])['xxxx'].sum().unstack().fillna(0)
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(dff.columns):  # dff.columns
        y = dff[j].values
        data.append(go.Scatter(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            title='xxxxxx',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            height=500,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            xaxis=dict(
                tickformat='%Y%m',
                showgrid=False,
                nticks=20,
                tickangle=-30,
                tickfont=dict(size=13)),
            yaxis=dict(
                tickfont=dict(size=13),  # xxxxxxxxxxxx
                autorange=True))}


@dash_app.callback(
    Output('graph2_4_app12', 'figure'),
    [Input('zflx_app12', 'values')])
def update_graph1(zflx):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df1.groupby(['xxxx', 'xxxx'])['xxx'].sum().reset_index()
    dff['xxxx'] = dff.groupby(['xxxx'])['xxx'].transform(lambda x: x / x.sum())
    dff['xxxx'] = (dff['xxxx'] * 100).round(2)
    dff = dff.groupby(['xxxx', 'xxxx'])['xxxx'].sum().unstack().fillna(0)
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(dff.columns):  # dff.columns
        y = dff[j].values
        data.append(go.Scatter(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            title='xxxxxx',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            height=500,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            xaxis=dict(
                tickformat='%Y%m',
                showgrid=False,
                nticks=20,
                tickangle=-30,
                tickfont=dict(size=13)),
            yaxis=dict(
                tickfont=dict(size=13),  # xxxxxxxxxxxx
                autorange=True))}


@dash_app.callback(
    Output('graph2_5_app12', 'figure'),
    [Input('zflx_app12', 'values')])
def update_graph1(zflx):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df1.query("xx=='1'").groupby(['xxxx'])['xxx'].sum().reset_index()
    dff['xx'] = df1.query("xxxx=='xxx' & xxxx=='xxx'").groupby(['xxxx'])['xxx'].sum().tolist()
    dff['xxxx'] = (dff['xxx'] / dff['xx']).round(4) * 100
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff['xxxx']]
    y = dff['xxxx'].values
    data.append(go.Scatter(x=x, y=y, name='xxx%x', opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            showlegend=True,
            title='xxxx',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            height=500,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            annotations = [{
                'x': -0.05, 'y': -0.28, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False ,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'font':{'size':16,'family':'STKaiti'},
                'text': 'xxxxxx=xx/xxxxxx'
            }],
            xaxis=dict(
                tickformat='%Y%m',
                showgrid=False,
                nticks=20,
                tickangle=-30,
                tickfont=dict(size=13)),
            yaxis=dict(
                tickfont=dict(size=13),  # xxxxxxxxxxxx
                autorange=True))}


@dash_app.callback(
    Output('graph2_6_app12', 'figure'),
    [Input('zflx_app12', 'values')])
def update_graph1(zflx):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df1.groupby(['xxxx', 'xx'])['xxx'].sum().reset_index()
    dff['xxxx'] = dff.groupby(['xxxx'])['xxx'].transform(lambda x: x / x.sum())
    dff['xxxx'] = (dff['xxxx'] * 100).round(2)
    dff = dff.groupby(['xxxx', 'xx'])['xxxx'].sum().unstack().fillna(0)
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(dff.columns):  # dff.columns
        y = dff[j].values
        data.append(go.Scatter(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            title='xxxx',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            height=500,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            xaxis=dict(
                tickformat='%Y%m',
                showgrid=False,
                showline=True, #xxxxxxx
                nticks=20,
                tickangle=-30,
                tickfont=dict(size=13)),
            yaxis=dict(
                tickfont=dict(size=13),  # xxxxxxxxxxxx
                autorange=False,range=[5,25]))}


@dash_app.callback(
    Output('graph3_1_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df1.query(f" xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    dff = dff[dff['xxxx']!='-999'].copy()
    dff = dff.groupby(['xxxx', 'xxxx'])['xxx'].sum().unstack()
    if len(dff) == 0:
        data = []
    else:
        dff['total'] = dff.sum(axis=1)
        dff['xxxxx'] = (dff['xxxx'] + dff['xxxx']) / dff['total']
        dff['xxxxx'] = dff['xxxx'] / dff['total']
        dff['xxxxx'] = dff['xxxx'] / dff['total']
        dff[['xxxxx', 'xxxxx', 'xxxxx']] = (dff[['xxxxx', 'xxxxx', 'xxxxx']] * 100).round(2)
        dff = dff[-6:].copy()
        # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
        x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
        for i, j in enumerate(['xxxxx', 'xxxxx', 'xxxxx']):  # dff.columns
            y = dff[j].values
            data.append(go.Scatter(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            title='xxxxxxxx',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            height=500,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            xaxis=dict(
                tickformat='%Y%m',
                showgrid=False,
                nticks=6,
                tickangle=-30,
                tickfont=dict(size=13)),
            yaxis=dict(
                tickfont=dict(size=13),  # xxxxxxxxxxxx
                autorange=True))}


@dash_app.callback(
    Output('graph3_2_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('riqi_dropdown_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, riqi):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df1.query(f" xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    dff = dff[dff['xxxx'] == riqi]
    if len(dff) == 0:
        data = []
    else:
        dff = dff.groupby(['xxxx', 'xxxx'])['xxx'].sum().reset_index()
        dff['xxxx'] = dff.groupby('xxxx')['xxx'].transform(lambda x: x / x.sum())
        dff['xxxx'] = (dff['xxxx'] * 100).round(2)
        a = pd.DataFrame(['xxxx', 'xxxx', 'xxxx', 'xxxx', 'xxx', 'xx'], columns=['xxxx'])
        dff = a.merge(dff, on='xxxx', how='left').fillna(0)
        # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
        x = dff['xxxx'].values
        y1 = dff['xxx'].values
        y2 = dff['xxxx'].values
        data.append(go.Bar(x=x, y=y1, width=0.5, name='xxx'))
        data.append(go.Scatter(x=x, y=y2, yaxis='y2', name='xxxx(%)'))
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            title='xxxxxxxx',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            legend=dict(x=1, y=1.2),  # ,1orientation="h"
            height=500,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            xaxis=dict(
                tickformat='%Y%m',
                showgrid=False,
                tickangle=-30,
                tickfont=dict(size=13)),
            yaxis=dict(nticks=5,
                       tickfont=dict(size=13),  # xxxxxxxxxxxx
                       autorange=False, range=[0, 80000]),
            yaxis2=dict(overlaying='y',
                        side='right',  # xxxx
                        # tickformat = 'p', #'%'#'d'
                        titlefont=dict(color='rgb(148, 103, 189)', size=14),  # xxxxxxxxxxxxx
                        tickfont=dict(color='rgb(148, 103, 189)', size=12),  # xxxxxxxxxxxx
                        zeroline=False,
                        autorange=False, range=[0, 50],
                        showgrid=False))}


@dash_app.callback(
    Output('graph3_3_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('riqi_dropdown_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, riqi):
    data = []
    dff = df1.query(
        f"xxxx=={riqi} & xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    refuse_top10 = dff.query("xxxx == 'xxxx'").groupby(['xxxx'])['xxx'].sum().sort_values(ascending=False)[:10].reset_index()
    tt_mth = dff['xxx'].sum()
    refuse_top10['xx'] = refuse_top10['xxx'] / tt_mth
    x = refuse_top10['xxxx']
    y = (refuse_top10['xx'] * 100).round(2)
    data.append(go.Scatter(x=x, y=y, name='xx(%)'))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            title='xxxxxxxx_Top10',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            showlegend=True,
            height=500,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            xaxis=dict(
                tickangle=-30,
                tickfont=dict(size=13),
                showgrid=False,
                showline=True,
                zeroline=False,
                showticklabels=True),
            yaxis=dict(  # title='xxx',
                # tickformat = 'd',
                # titlefont=dict(color='rgb(148, 103, 189)',size=14),#xxxxxxxxxxxxx
                tickfont=dict(size=13),  # xxxxxxxxxxxx
                zeroline=False,
                autorange=True))}


@dash_app.callback(
    Output('graph3_4_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df1.query(f" xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    dff = dff.groupby(['xxxx', 'xxxx'])['xxx'].sum().unstack()
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(dff.columns):
        y = dff[j].values
        data.append(go.Bar(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i]),width=0.6
    return {
        'data': data,
        'layout': go.Layout(barmode='stack',
                            bargap=0.35,
                            title='xxxxxxx',
                            titlefont=dict(color='rgb(148, 103, 189)', size=20),
                            height=600,
                            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
                            xaxis=dict(
                                tickformat='%Y%m',
                                nticks=20,
                                tickangle=-30,
                                tickfont=dict(size=13)),
                            yaxis=dict(  # title='xxx',
                                # tickformat = '%',
                                # tickformat = 'd',
                                # titlefont=dict(color='rgb(148, 103, 189)',size=14),#xxxxxxxxxxxxx
                                tickfont=dict(size=13),  # xxxxxxxxxxxx
                                autorange=True))}


@dash_app.callback(
    Output('graph3_5_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df1.query(f" xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    dff = dff.query("xxxx=='xxx'").groupby(['xxxx', 'xxxx'])['xxx'].sum().unstack()
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(dff.columns):
        y = dff[j].values
        data.append(go.Bar(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(barmode='stack',
                            bargap=0.35,
                            # hovermode='closest',
                            title='xxxxxxxxxx',
                            titlefont=dict(color='rgb(148, 103, 189)', size=20),
                            height=600,
                            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
                            xaxis=dict(
                                tickformat='%Y%m',
                                nticks=20,
                                tickangle=-30,
                                tickfont=dict(size=13)),
                            yaxis=dict(  # title='xxx',
                                # tickformat = '%',
                                # tickformat = 'd',
                                # titlefont=dict(color='rgb(148, 103, 189)',size=14),#xxxxxxxxxxxxx
                                tickfont=dict(size=13),  # xxxxxxxxxxxx
                                autorange=True))}


@dash_app.callback(
    Output('graph3_6_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df1.query(
        f"xxxx=='xx' & xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    dff = dff.groupby(['xxxx', 'xxxx'])['xxx'].sum().unstack()
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(dff.columns):
        y = dff[j].values
        data.append(go.Bar(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i]),width=0.6
    return {
        'data': data,
        'layout': go.Layout(barmode='stack',
                            bargap=0.35,
                            # hovermode='closest',
                            title='xxxxxxx',
                            titlefont=dict(color='rgb(148, 103, 189)', size=20),
                            height=600,
                            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
                            xaxis=dict(
                                tickformat='%Y%m',
                                nticks=20,
                                tickangle=-30,
                                tickfont=dict(size=13)),
                            yaxis=dict(  # title='xxx',
                                # tickformat = '%',
                                # tickformat = 'd',
                                # titlefont=dict(color='rgb(148, 103, 189)',size=14),#xxxxxxxxxxxxx
                                tickfont=dict(size=13),  # xxxxxxxxxxxx
                                autorange=True))}


@dash_app.callback(
    Output('graph3_7_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df1.query(f" xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    a = dff['xxxx'].unique().tolist()
    a.sort(reverse=True)
    if len(a) == 2:
        a.append('total')
    for i in a:
        if i == 'total':
            dff2 = dff.copy()
        else:
            dff2 = dff.query(f"xxxx == '{i}'").copy()
        dff2 = dff2.groupby(['xxxx', 'xxxx'])['xxx'].sum().unstack()
        dff2['total'] = dff2.sum(axis=1)
        dff2['xxx'] = ((dff2['xx'] / dff2['total']) * 100).round(2)
        x = [str(a)[:4] + '-' + str(a)[4:] for a in dff2.index]
        # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff2.index]
        y = dff2['xxx'].values
        data.append(go.Scatter(x=x, y=y, name=i))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            title='xxxxx(%)',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            height=600,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            xaxis=dict(
                tickformat='%Y%m',
                nticks=20,
                tickangle=-30,
                tickfont=dict(size=13),
                showgrid=False,
                showline=True,
                showticklabels=True),
            yaxis=dict(  # title='xxx',
                # tickformat = '.0%',
                # tickformat = 'd',
                # titlefont=dict(color='rgb(148, 103, 189)',size=14),#xxxxxxxxxxxxx
                tickfont=dict(size=13),  # xxxxxxxxxxxx
                autorange=True))}


@dash_app.callback(
    Output('graph3_8_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df3.query(f" xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    data = []
    # x=[str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in df['xxxx'].values]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff['xxxx'].unique()]
    y1 = (dff.groupby('xxxx')['xxx'].sum() / dff.groupby('xxxx')['xxx'].sum()).round(4).values * 10000
    y2 = (dff.groupby('xxxx')['xxxx'].sum() / dff.groupby('xxxx')['xxx'].sum()).round(2).values
    data.append(go.Bar(x=x, y=y1, name='xxx'))
    data.append(go.Scatter(x=x, y=y2, yaxis='y2', name='xxxx'))  #
    return {
        'data': data,
        'layout': go.Layout(title='xxxxxxxxxx',
                            titlefont=dict(color='rgb(148, 103, 189)', size=20),
                            bargap=0.35,
                            height=600,
                            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
                            legend=dict(x=1, y=1.15),  # ,1orientation="h"
                            xaxis=dict(
                                type='date',
                                tickformat='%Y%m',
                                nticks=20,
                                tickangle=-30,
                                tickfont=dict(size=13)),
                            yaxis=dict(  # title='xxx',
                                # tickformat = '%',
                                # tickformat = 'd',
                                # nticks=4,
                                # titlefont=dict(color='rgb(148, 103, 189)',size=14),#xxxxxxxxxxxxx
                                tickfont=dict(size=13),  # xxxxxxxxxxxx
                                showgrid=True,
                                autorange=False, range=[60000, 90000]),
                            yaxis2=dict(overlaying='y',
                                        side='right',  # xxxx
                                        # tickformat = '.0%',
                                        titlefont=dict(color='rgb(148, 103, 189)', size=14),  # xxxxxxxxxxxxx
                                        tickfont=dict(color='rgb(148, 103, 189)', size=12),  # xxxxxxxxxxxx
                                        autorange=True, range=[0.25, 0.28],
                                        showgrid=False))}


@dash_app.callback(
    Output('graph3_9_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df2.query(f" xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    dff = dff.query("xxx!='-999'").groupby(['xxxx', 'xxx'])['xxx'].sum().unstack()
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(['(0,9]', '(9,12]', '(12,15]', '(15,20]', '(20,30]', '(30,40]', '40+']):  # dff.columns
        y = dff[j].values
        data.append(go.Bar(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(barmode='stack',
                            bargap=0.55,
                            # hovermode='closest',
                            title='xxxxx',
                            titlefont=dict(color='rgb(148, 103, 189)', size=20),
                            height=500,
                            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
                            xaxis=dict(
                                tickformat='%Y%m',
                                nticks=20,
                                tickangle=-30,
                                tickfont=dict(size=13)),
                            yaxis=dict(
                                tickfont=dict(size=13),  # xxxxxxxxxxxx
                                autorange=True))}


@dash_app.callback(
    Output('graph3_10_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df2.query(f" xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    if len(dff) == 0:
        data = []
    else:
        dff = dff.query("xxx!='-999'").groupby(['xxxx', 'xxx'])['xxx'].sum().reset_index()
        dff['xxxx'] = dff.groupby(['xxxx'])['xxx'].transform(lambda x: x / x.sum())
        dff['xxxx'] = (dff['xxxx'] * 100).round(2)
        dff = dff.groupby(['xxxx', 'xxx'])['xxxx'].sum().unstack().fillna(0)
        # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
        x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
        for i, j in enumerate(['(0,9]', '(9,12]', '(12,15]', '(15,20]', '(20,30]', '(30,40]', '40+']):  # dff.columns
            y = dff[j].values
            data.append(go.Scatter(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            title='xxxxx',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            height=500,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            xaxis=dict(
                tickformat='%Y%m',
                showgrid=False,
                nticks=20,
                tickangle=-30,
                tickfont=dict(size=13)),
            yaxis=dict(
                tickfont=dict(size=13),  # xxxxxxxxxxxx
                autorange=True))}


@dash_app.callback(
    Output('graph3_11_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df2.query(f" xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    dff = dff.query("xxxx!='-999'").groupby(['xxxx', 'xxxx'])['xxx'].sum().unstack()
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(['[0-10)', '[10-20)', '[20,30)', '[30,40)', '40+']):  # dff.columns
        y = dff[j].values
        data.append(go.Bar(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(barmode='stack',
                            bargap=0.55,
                            # hovermode='closest',
                            title='xxxxxx',
                            titlefont=dict(color='rgb(148, 103, 189)', size=20),
                            height=500,
                            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
                            xaxis=dict(
                                tickformat='%Y%m',
                                nticks=20,
                                tickangle=-30,
                                tickfont=dict(size=13)),
                            yaxis=dict(
                                tickfont=dict(size=13),  # xxxxxxxxxxxx
                                autorange=True))}


@dash_app.callback(
    Output('graph3_12_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df2.query(f" xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    dff = dff.query("xxxx!='-999'").groupby(['xxxx', 'xxxx'])['xxx'].sum().reset_index()
    dff['xxxx'] = dff.groupby(['xxxx'])['xxx'].transform(lambda x: x / x.sum())
    dff['xxxx'] = (dff['xxxx'] * 100).round(2)
    dff = dff.groupby(['xxxx', 'xxxx'])['xxxx'].sum().unstack().fillna(0)
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(['[0-10)', '[10-20)', '[20,30)', '[30,40)', '40+']):  # dff.columns
        y = dff[j].values
        data.append(go.Scatter(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            title='xxxxxx',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            height=500,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            xaxis=dict(
                tickformat='%Y%m',
                showgrid=False,
                nticks=20,
                tickangle=-30,
                tickfont=dict(size=13)),
            yaxis=dict(
                tickfont=dict(size=13),  # xxxxxxxxxxxx
                autorange=True))}


@dash_app.callback(
    Output('graph3_13_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df2.query(f" xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    dff = dff.groupby(['xxxx', 'xxxx'])['xxx'].sum().unstack()
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(['xxxx', 'xxx', 'xx']):  # dff.columns
        y = dff[j].values
        data.append(go.Bar(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(barmode='stack',
                            bargap=0.55,
                            # hovermode='closest',
                            title='xxxx',
                            titlefont=dict(color='rgb(148, 103, 189)', size=20),
                            height=500,
                            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
                            xaxis=dict(
                                tickformat='%Y%m',
                                nticks=20,
                                tickangle=-30,
                                tickfont=dict(size=13)),
                            yaxis=dict(
                                tickfont=dict(size=13),  # xxxxxxxxxxxx
                                autorange=True))}


@dash_app.callback(
    Output('graph3_14_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df2.query(f" xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    dff = dff.groupby(['xxxx', 'xxxx'])['xxx'].sum().reset_index()
    dff['xxxx'] = dff.groupby(['xxxx'])['xxx'].transform(lambda x: x / x.sum())
    dff['xxxx'] = (dff['xxxx'] * 100).round(2)
    dff = dff.groupby(['xxxx', 'xxxx'])['xxxx'].sum().unstack().fillna(0)
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(['xx', 'xxx', 'xxxx']):  # dff.columns
        y = dff[j].values
        data.append(go.Scatter(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            title='xxxx',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            height=500,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            xaxis=dict(
                tickformat='%Y%m',
                showgrid=False,
                nticks=20,
                tickangle=-30,
                tickfont=dict(size=13)),
            yaxis=dict(
                tickfont=dict(size=13),  # xxxxxxxxxxxx
                autorange=True))}


@dash_app.callback(
    Output('graph3_15_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df4.query(f"xxxx >= 201808 & xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    dff = dff.groupby(['xxxx', 'xxxx'])['xxx'].sum().unstack()

    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(['xxx','x','xx', 'xx']):  # dff.columns
        y = dff[j].values
        data.append(go.Bar(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(barmode='stack',
                            bargap=0.55,
                            # hovermode='closest',
                            title='xxxxxx',
                            titlefont=dict(color='rgb(148, 103, 189)', size=20),
                            height=500,
                            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
                            xaxis=dict(
                                tickformat='%Y%m',
                                nticks=13,
                                tickangle=-30,
                                tickfont=dict(size=13)),
                            yaxis=dict(
                                tickfont=dict(size=13),  # xxxxxxxxxxxx
                                autorange=True))}


@dash_app.callback(
    Output('graph3_16_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df4.query(f"xxxx >= 201808 & xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    dff = dff.groupby(['xxxx', 'xxxx'])['xxx'].sum().reset_index()
    dff['xxxx'] = dff.groupby(['xxxx'])['xxx'].transform(lambda x: x / x.sum())
    dff['xxxx'] = (dff['xxxx'] * 100).round(2)
    dff = dff.groupby(['xxxx', 'xxxx'])['xxxx'].sum().unstack().fillna(0)
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(['xx', 'xx', 'x', 'xxx']):  # dff.columns
        y = dff[j].values
        data.append(go.Scatter(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            title='xxxxxx',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            height=500,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            xaxis=dict(
                tickformat='%Y%m',
                showgrid=False,
                nticks=13,
                tickangle=-30,
                tickfont=dict(size=13)),
            yaxis=dict(
                tickfont=dict(size=13),  # xxxxxxxxxxxx
                autorange=True))}

@dash_app.callback(
    Output('graph3_17_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df4.query(f" xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    dff = dff.groupby(['xxxx', 'xx'])['xxx'].sum().unstack()
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(['50+','[46-50]','[41-45]','[36-40]','[31-35]','[26-30]','(0-25]']):  # dff.columns
        y = dff[j].values
        data.append(go.Bar(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(barmode='stack',
                            bargap=0.55,
                            # hovermode='closest',
                            title='xxxx',
                            titlefont=dict(color='rgb(148, 103, 189)', size=20),
                            height=500,
                            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
                            xaxis=dict(
                                tickformat='%Y%m',
                                nticks=20,
                                tickangle=-30,
                                tickfont=dict(size=13)),
                            yaxis=dict(
                                tickfont=dict(size=13),  # xxxxxxxxxxxx
                                autorange=True))}


@dash_app.callback(
    Output('graph3_18_app12', 'figure'),
    [Input('zflx_app12', 'values'),
     Input('tc_app12', 'values'),
     Input('ywlx_app12', 'values'),
     Input('qudao_app12', 'values'),
     Input('cllx_app12', 'values'),
     Input('diqu_app12', 'values'),
     Input('qunti_app12', 'value')])
def update_graph1(zflx, tc, ywlx, qudao, cllx, diqu, qunti):
    data = []
    # clr = ['#9d2933', '#425066', '#ff8936', '#065279', '#88ada6', '#a88462']
    dff = df4.query(f" xxxx in {zflx} & xx in {tc} & xxxx in {ywlx} & xxxx in {qudao} & xxxx in {cllx} & xx in {diqu}")
    if qunti == 'xx':
        dff = dff[dff['xxxx'] == 'xx'].copy()
    dff = dff.query("xx!='-999'").groupby(['xxxx', 'xx'])['xxx'].sum().reset_index()
    dff['xxxx'] = dff.groupby(['xxxx'])['xxx'].transform(lambda x: x / x.sum())
    dff['xxxx'] = (dff['xxxx'] * 100).round(2)
    dff = dff.groupby(['xxxx', 'xx'])['xxxx'].sum().unstack().fillna(0)
    # x = [str(a)[:4] + 'x' + str(a)[4:] + 'x' for a in dff.index]
    x = [str(a)[:4] + '-' + str(a)[4:] for a in dff.index]
    for i, j in enumerate(['(0-25]','[26-30]','[31-35]','[36-40]','[41-45]','[46-50]','50+']):  # dff.columns
        y = dff[j].values
        data.append(go.Scatter(x=x, y=y, name=j, opacity=0.9))  # , marker=dict(color=clr[i])
    return {
        'data': data,
        'layout': go.Layout(
            # hovermode='closest',
            title='xxxx',
            titlefont=dict(color='rgb(148, 103, 189)', size=20),
            height=500,
            margin={'l': 70, 'b': 100, 't': 100, 'r': 70, 'pad': 10},
            xaxis=dict(
                tickformat='%Y%m',
                showgrid=False,
                nticks=20,
                tickangle=-30,
                tickfont=dict(size=13)),
            yaxis=dict(
                tickfont=dict(size=13),  # xxxxxxxxxxxx
                autorange=True))}