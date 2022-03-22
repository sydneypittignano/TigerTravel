#!/usr/bin/env python

#-----------------------------------------------------------------------
# penny.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

from time import localtime, asctime, strftime
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template
from database import filter_rides, add_ride, from_rideid_get_riders

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

    html = render_template('index.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/login', methods=['GET'])
def login():

    html = render_template('login.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/add', methods=['GET'])
def add():
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
    
    html = render_template('about.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/tutorial', methods=['GET'])
def tutorial():
    
    html = render_template('tutorial.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/account', methods=['GET'])
def account():
    
    html = render_template('account.html')
    response = make_response(html)
    return response
