#!/usr/bin/env python

#-----------------------------------------------------------------------
# tigertravel.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

from time import localtime, asctime, strftime
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template, session

from keys import APP_SECRET_KEY
from database import filter_rides, add_ride, from_netid_get_rides
from database import from_rideid_get_riders, from_netid_get_rides

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')
app.secret_key = APP_SECRET_KEY
import auth

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

    html = render_template('index.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/add', methods=['GET'])
def add():

    my_netid = auth.authenticate().strip()

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

    my_netid = auth.authenticate().strip()

    origin = request.args.get('origin')
    dest = request.args.get('dest')
    starttime = request.args.get('starttime')
    endtime = request.args.get('endtime')

    # array of Ride objects
    rides = filter_rides(None, origin, dest, starttime, endtime)
    # list of lists
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

    my_netid = auth.authenticate().strip()
    
    html = render_template('about.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/tutorial', methods=['GET'])
def tutorial():

    my_netid = auth.authenticate().strip()
    
    html = render_template('tutorial.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/account', methods=['GET'])
def account():

    my_netid = auth.authenticate().strip()
    print(my_netid)
    my_rides = from_netid_get_rides(my_netid)
    for ride in my_rides:
        rides = filter_rides(ride[0], None, None, None, None)
    html = render_template('account.html', my_rides=rides)
    response = make_response(html)
    return response
