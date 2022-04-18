#!/usr/bin/env python

#-----------------------------------------------------------------------
# tigertravel.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

import os
from datetime import datetime
from time import localtime, asctime, strftime
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template, session

from olddatabase import get_rides, add_ride, from_netid_get_rides, from_rideid_get_riders, leave_ride, get_suggested
from olddatabase import check_student, from_rideid_get_ride, send_request, cancel_request, accept_request, delete_ride, decline_request
from ride import Ride
from keys import APP_SECRET_KEY
from emails import email_request_received

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')
# app.secret_key = os.environ['APP_SECRET_KEY']
app.secret_key = APP_SECRET_KEY
import auth

#-----------------------------------------------------------------------

# Displays the index page
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

    html = render_template('index.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

# Displays the add page
# Does NOT do the actual adding
@app.route('/add', methods=['GET'])
def add():

    msg = request.args.get('msg')
    if msg is None:
        msg = ''
    
    msg2 = request.args.get('msg2')
    if msg2 is None:
        msg2 = ''

    joining_rideid = request.args.get('joining_rideid')
    joining_ride = ""
    if joining_rideid is not None:
        joining_ride = from_rideid_get_ride(joining_rideid)
        msg = 'None of your current rides are compatible!'

    my_netid = auth.authenticate().strip()
    check_student(my_netid)
    
    html = render_template('add.html', msg=msg, joining_ride = joining_ride, msg2=msg2)
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

# Attempt to add a ride to the database
# Redirect to the Dashboard if successful
# Redirect to the Add page if not successful
@app.route('/addride', methods=['GET'])
def addride():
    my_netid = auth.authenticate().strip()
    check_student(my_netid)

    origin = request.args.get('origin')
    dest = request.args.get('dest')
    starttime = request.args.get('starttime')
    endtime = request.args.get('endtime')

    if (origin == '' or dest == '' or starttime == '' or endtime == ''):
        return redirect(url_for('add', msg="Your ride was not added! You left one or more fields blank. Try again!"))
    if (origin == dest):
        return redirect(url_for('add', msg="Your ride was not added! Your origin and destination are the same. Please enter a ride with a different origin and destination!"))
    
    starttime_datetime = datetime.strptime(starttime, '%m/%d/%Y, %I:%M %p')
    endtime_datetime = datetime.strptime(endtime, '%m/%d/%Y, %I:%M %p')

    if (starttime_datetime > endtime_datetime):
        return redirect(url_for('add', msg="Your ride was not added! Your start time occurs after your end time. Please enter a ride with a start time that occurs before the end time!"))

    if (starttime_datetime < datetime.now()):
        return redirect(url_for('add', msg="Your ride was not added! Your start time has already passed. Please enter a ride with a start time in the future!"))
    
    else: 
        add_ride(my_netid, origin, dest, starttime, endtime)
        return redirect(url_for('account', msg="Ride successfully added!"))

#-----------------------------------------------------------------------


@app.route('/addandjoin', methods=['GET'])
def addandjoin():
    my_netid = auth.authenticate().strip()
    check_student(my_netid)

    origin = request.args.get('origin')
    dest = request.args.get('dest')
    starttime = request.args.get('starttime')
    endtime = request.args.get('endtime')
    joining_rideid = request.args.get('joining_rideid')

    if (origin == '' or dest == '' or starttime == '' or endtime == ''):
        return redirect(url_for('add', joining_rideid= joining_rideid, msg2="Your ride was not added! You left one or more fields blank. Try again!"))
    if (origin == dest):
        return redirect(url_for('add', joining_rideid=joining_rideid, msg2="Your ride was not added! Your origin and destination are the same. Please enter a ride with a different origin and destination!"))
    
    starttime_datetime = datetime.strptime(starttime, '%m/%d/%Y, %I:%M %p')
    print(starttime_datetime)
    endtime_datetime = datetime.strptime(endtime, '%m/%d/%Y, %I:%M %p')

    if (starttime_datetime > endtime_datetime):
        return redirect(url_for('add', joining_rideid=joining_rideid, msg2="Your ride was not added! Your start time occurs after your end time. Please enter a ride with a start time that occurs before the end time!"))
    
    if (endtime_datetime < datetime.now()):
        return redirect(url_for('add', joining_rideid=joining_rideid, msg2="Your ride was not added! Your start time has already passed. Please enter a ride with an end time in the future!"))

    else:
        my_ride = Ride(None, None, origin, dest, starttime_datetime, endtime_datetime, None, None, None)
        joining_ride = from_rideid_get_ride(joining_rideid)

        if joining_ride.hasOverlapWith(my_ride) and joining_ride.matchesRouteOf(my_ride):
            my_rideid = add_ride(my_netid, origin, dest, starttime, endtime)
            send_request(joining_rideid, my_rideid)
            recipient_netids = from_rideid_get_riders(joining_rideid)
            email_request_received(recipient_netids)
            return redirect(url_for('account', msg="Request successfully sent!"))
        else:
            return redirect(url_for('add', joining_rideid=joining_rideid, msg2="Your ride was not compatible with the above ride! Try again, or use the \"Add Ride\" menu bar option to add a ride without joining."))


#-----------------------------------------------------------------------

@app.route('/browse', methods=['GET'])
def browse():

    my_netid = auth.authenticate().strip()
    check_student(my_netid)

    msg = request.args.get('msg')
    if msg is None:
        msg = ''

    html = render_template('browse.html', msg=msg)
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/browseresults', methods=['GET'])
def browseresults():
    my_netid = auth.authenticate().strip()
    check_student(my_netid)

    origin = request.args.get('origin')
    dest = request.args.get('dest')
    starttime = request.args.get('starttime')
    endtime = request.args.get('endtime')

    # array of Ride objects
    rides = get_rides(None, origin, dest, starttime, endtime)
    future_rides = []
    for ride in rides:
        if ride.get_endtime() >= datetime.now():
            future_rides.append(ride)
    html = render_template('browseresults.html', rides=future_rides, my_netid=my_netid)
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

    msg = request.args.get('msg')
    if msg is None:
        msg = ''

    rides = from_netid_get_rides(my_netid)

    future_rides = []
    past_rides = []
    for ride in rides:
        incoming = []
        outgoing = []
        suggested = []
        for reqrec in ride.get_reqrec():
            incoming.append(get_rides(reqrec, None, None, None, None)[0])
        for reqsent in ride.get_reqsent():
            outgoing.append(get_rides(reqsent, None, None, None, None)[0])
        
        #make suggested, which is an array of rides that have same origin, dest, and overlap
        suggested = get_suggested(ride, incoming, outgoing)

        full_ride = [ride, incoming, outgoing, suggested]
        if ride.get_endtime() < datetime.now():
            past_rides.append(full_ride)
        else:
            future_rides.append(full_ride)

    html = render_template('account.html', full_rides=future_rides, past_rides=past_rides, msg=msg)
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

    reqsent = joining_ride.get_reqsent()
    for ride in rides:
        # joining ride has requested to join ride
        if ride.get_endtime() > datetime.now():
            if ride.get_rideid() in reqsent:
                accept_request(ride.get_rideid(), joining_rideid)
                return redirect(url_for('account', msg="Ride successfully joined! You both requested each other :)"))
            if joining_ride.hasOverlapWith(ride) and joining_ride.matchesRouteOf(ride):
                send_request(joining_rideid, ride.get_rideid())
                recipient_netids = from_rideid_get_riders(joining_rideid)
                email_request_received(recipient_netids)
                return redirect(url_for('account', msg="Request successfully sent!"))
    
    return redirect(url_for('add', joining_rideid=joining_rideid, msg2="You can still request to join! Just tell us your departure window, making sure it overlaps with the above ride."))

#-----------------------------------------------------------------------

@app.route('/cancelrequest', methods=['GET'])
def cancelrequest():
    my_netid = auth.authenticate().strip()
    check_student(my_netid)

    joining_rideid = request.args.get('joining_rideid')
    sending_rideid = request.args.get('sending_rideid')
    cancel_request(joining_rideid, sending_rideid)
    return redirect(url_for('account', msg="Request cancelled!"))

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

@app.route('/deleteorleaveride', methods=['GET'])
def deleteorleaveride():
    my_netid = auth.authenticate().strip()
    check_student(my_netid)

    rideid = request.args.get('rideid')
    netid = request.args.get('netid')
    
    if len(from_rideid_get_riders(rideid)) == 1:
        delete_ride(rideid)
        return redirect(url_for('account', msg="Ride deleted!"))
    else:
        leave_ride(rideid, my_netid)
        return redirect(url_for('account', msg="Ride successfully left!"))

#-----------------------------------------------------------------------
@app.route('/declinerequest', methods=['GET'])
def declinerequest():
    my_netid = auth.authenticate().strip()
    check_student(my_netid)

    joining_rideid = request.args.get('joining_rideid')
    sending_rideid = request.args.get('sending_rideid')

    decline_request(joining_rideid, sending_rideid)
    return redirect(url_for('account'))

#-----------------------------------------------------------------------
# displays the editride page
@app.route('/edit', methods=['GET'])
def edit():
    my_netid = auth.authenticate().strip()
    check_student(my_netid)

    msg = request.args.get('msg')
    if msg is None:
        msg = ''

    rideid = request.args.get('rideid')
    ride = from_rideid_get_ride(rideid)
    if my_netid not in ride.get_riders():
        return redirect(url_for('account', msg="Naughty, naughty... you malicious user ;)"))

    html = render_template('edit.html', msg=msg, ride=ride)
    response = make_response(html)
    return response

#-----------------------------------------------------------------------
@app.route('/editride', methods=['GET'])
def editride():
    my_netid = auth.authenticate().strip()
    check_student(my_netid)

    origin = request.args.get('origin')
    dest = request.args.get('dest')
    starttime = request.args.get('starttime')
    endtime = request.args.get('endtime')
    rideid = request.args.get('rideid')

    if (origin == '' or dest == '' or starttime == '' or endtime == ''):
        return redirect(url_for('edit', rideid=rideid, msg="Your ride was not edited! You left one or more fields blank. Try again!"))
    if (origin == dest):
        return redirect(url_for('edit', rideid=rideid, msg="Your ride was not edited! Your origin and destination are the same. Please enter a ride with a different origin and destination!"))
    
    starttime_datetime = datetime.strptime(starttime, '%m/%d/%Y, %I:%M %p')
    endtime_datetime = datetime.strptime(endtime, '%m/%d/%Y, %I:%M %p')

    if (starttime_datetime > endtime_datetime):
        return redirect(url_for('edit', rideid=rideid, msg="Your ride was not edited! Your start time occurs after your end time. Please enter a ride with a start time that occurs before the end time!"))

    if (starttime_datetime < datetime.now()):
        return redirect(url_for('edit', rideid=rideid, msg="Your ride was not edited! Your start time has already passed. Please enter a ride with a start time in the future!"))
    
    else: 
        add_ride(my_netid, origin, dest, starttime, endtime)
        delete_ride(request.args.get('rideid'))
        return redirect(url_for('account', msg="Ride successfully edited!"))