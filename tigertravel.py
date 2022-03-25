#!/usr/bin/env python

#-----------------------------------------------------------------------
# penny.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

from time import localtime, asctime, strftime
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template, session

from keys import APP_SECRET_KEY
from database import filter_rides, add_ride, from_rideid_get_riders

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')
app.secret_key = APP_SECRET_KEY
import auth

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

    username = auth.authenticate()

    html = render_template('index.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/login', methods=['GET'])
def login():

    username = auth.authenticate()

    html = render_template('login.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/add', methods=['GET'])
def add():

    username = auth.authenticate()

    netid = request.args.get('netid')
    rideid = request.args.get('rideid')
    origin = request.args.get('origin')
    dest = request.args.get('dest')
    starttime = request.args.get('starttime')
    endtime = request.args.get('endtime')

    # including this for now, to stop lots of inserts
    if (netid is not None):
        add_ride(netid, rideid, origin, dest, starttime, endtime)
    
    html = render_template('add.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/browse', methods=['GET'])
def browse():

    username = auth.authenticate()

    origin = request.args.get('origin')
    dest = request.args.get('dest')
    starttime = request.args.get('starttime')
    endtime = request.args.get('endtime')

    rides = filter_rides(origin, dest, starttime, endtime)
    all_riders = []
    for ride in rides:
        rideid = ride.get_rideid()
        riders = from_rideid_get_riders(rideid)
        all_riders.append(riders)

    html = render_template('browse.html', rides=rides, all_riders=all_riders)
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/about', methods=['GET'])
def about():

    username = auth.authenticate()
    
    html = render_template('about.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/tutorial', methods=['GET'])
def tutorial():

    username = auth.authenticate()
    
    html = render_template('tutorial.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/account', methods=['GET'])
def account():

    username = auth.authenticate()
    
    html = render_template('account.html')
    response = make_response(html)
    return response
