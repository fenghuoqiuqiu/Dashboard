#!/usr/bin/env python
# -*- coding: utf-8 -*-


from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
import flask
from flask import Flask, Response, redirect, url_for, request, session, abort,render_template,make_response
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import pandas as pd
import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


from flask_app import server
# from index import dash_app

import mysql_db
from aes import pc


def protect_views(app):
    for view_func in app.server.view_functions:
        if view_func.startswith(app.url_base_pathname):
            app.server.view_functions[view_func] = login_required(app.server.view_functions[view_func])
    return app


server.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)

# flask-login
login_manager = LoginManager()
login_manager.session_protection='strong'
login_manager.init_app(server)
login_manager.login_view = "login"


# user model
class User(UserMixin):

    def __init__(self, id):
        self.id = id
        self.name = str(id)
        self.password = "555"

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)


# create some users with ids 1 to 20
users = [User("numpynewb")]


# somewhere to login
@server.route("/login", methods=["GET", "POST"])
def login():
    global username,password
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        df = mysql_db.data_get(username)
        if not df.empty:
            user_name=df['user_name'].unique().tolist()[0]
            pass_word=pc.decrypt(df['password'].unique().tolist()[0])
        else:
            user_name=None
            pass_word=None
        if username==user_name and password == pass_word:
            id = username
            user = User(id)
            login_user(user)
            session['username'] = username
            session['password'] = password
            return flask.redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return render_template('login.html')


# somewhere to logout
@server.route("/logout")
@login_required
def logout():
    logout_user()
    #return redirect(url_for('login'))
    return Response('<p>Logged out</p >')


# handle login failed
@server.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User(userid)

from index import dash_app
dash_app = protect_views(dash_app)



@server.route('/')
@login_required
def render_d1():
    return '333'



#run_simple('localhost', 8096, app)
#dash_app.run_server(port=8079,debug=True)
dash_app.run_server(host='localhost',port=2360,debug=True)


