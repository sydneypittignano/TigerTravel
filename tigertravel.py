#!/usr/bin/env python

#-----------------------------------------------------------------------
# tigertravel.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

import os
from time import localtime, asctime, strftime
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template, session

from database import get_rides, add_ride, from_netid_get_rides
from database import check_student, from_rideid_get_ride, send_request, cancel_request, accept_request, delete_ride
from keys import APP_SECRET_KEY

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')
app.secret_key = os.environ['APP_SECRET_KEY']
# app.secret_key = APP_SECRET_KEY
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
    check_student(my_netid)

    origin = request.args.get('origin')
    dest = request.args.get('dest')
    starttime = request.args.get('starttime')
    endtime = request.args.get('endtime')

    # including this for now, to stop lots of inserts
    if (origin is not None):
        add_ride(my_netid, origin, dest, starttime, endtime)

    return redirect(url_for('account'))

#-----------------------------------------------------------------------

@app.route('/browse', methods=['GET'])
def browse():

    my_netid = auth.authenticate().strip()
    check_student(my_netid)

    origin = request.args.get('origin')
    dest = request.args.get('dest')
    starttime = request.args.get('starttime')
    endtime = request.args.get('endtime')

    # array of Ride objects
    rides = get_rides(None, origin, dest, starttime, endtime)

    html = render_template('browse.html', rides=rides)
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/about', methods=['GET'])
def about():

    my_netid = auth.authenticate().strip()
    check_student(my_netid)
    
    html = render_template('about.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/tutorial', methods=['GET'])
def tutorial():

    my_netid = auth.authenticate().strip()
    check_student(my_netid)
    
    html = render_template('tutorial.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/account', methods=['GET'])
def account():

    my_netid = auth.authenticate().strip()
    # Make sure the student is in our database
    check_student(my_netid)

    rides = from_netid_get_rides(my_netid)
    
    full_rides = []
    for ride in rides:
        incoming = []
        outgoing = []
        for reqrec in ride.get_reqrec():
            incoming.append(get_rides(reqrec, None, None, None, None)[0])
        for reqsent in ride.get_reqsent():
            outgoing.append(get_rides(reqsent, None, None, None, None)[0])
        full_ride = [ride, incoming, outgoing]
        full_rides.append(full_ride)

    html = render_template('account.html', full_rides=full_rides)
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/tryrequest', methods=['GET'])
def tryrequest():
    my_netid = auth.authenticate().strip()
    check_student(my_netid)

    joining_rideid = request.args.get('rideid')
    joining_ride = from_rideid_get_ride(joining_rideid)
    rides = from_netid_get_rides(my_netid)

    for ride in rides:
        if joining_ride.hasOverlapWith(ride):
            send_request(joining_rideid, ride.get_rideid())
            break
        else:
            print('Nay')
    return redirect(url_for('account'))

#-----------------------------------------------------------------------

@app.route('/cancelrequest', methods=['GET'])
def cancelrequest():
    my_netid = auth.authenticate().strip()
    check_student(my_netid)

    joining_rideid = request.args.get('joining_rideid')
    sending_rideid = request.args.get('sending_rideid')
    cancel_request(joining_rideid, sending_rideid)
    return redirect(url_for('account'))

#-----------------------------------------------------------------------
@app.route('/acceptrequest', methods=['GET'])
def acceptrequest():
    my_netid = auth.authenticate().strip()
    check_student(my_netid)

    joining_rideid = request.args.get('joining_rideid')
    sending_rideid = request.args.get('sending_rideid')

    accept_request(joining_rideid, sending_rideid)
    return redirect(url_for('account'))

#-----------------------------------------------------------------------
@app.route('/deleteride', methods=['GET'])
def delteride():
    my_netid = auth.authenticate().strip()
    check_student(my_netid)

    rideid = request.args.get('rideid')
    delete_ride(rideid)
    return redirect(url_for('account'))
