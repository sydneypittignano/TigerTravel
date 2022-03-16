#!/usr/bin/env python

#-----------------------------------------------------------------------
# penny.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

from time import localtime, asctime, strftime
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template
from database import search_students, filter_rides

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')

#-----------------------------------------------------------------------

def get_ampm():
    if strftime('%p') == "AM":
        return 'morning'
    return 'afternoon'

def get_current_time():
    return asctime(localtime())

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
    
    html = render_template('add.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/browse', methods=['GET'])
def browse():

    startdate = request.args.get('startdate')
    enddate = request.args.get('enddate')
    origin = request.args.get('origin')
    dest = request.args.get('dest')
    starttime = request.args.get('starttime')
    endtime = request.args.get('endtime')

    rides = filter_rides(startdate, enddate, origin, dest, starttime, endtime)
    
    html = render_template('browse.html', rides=rides)
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

#-----------------------------------------------------------------------

@app.route('/searchform', methods=['GET'])
def search_form():

    error_msg = request.args.get('error_msg')
    if error_msg is None:
        error_msg = ''

    prev_netid = request.cookies.get('prev_netid')
    if prev_netid is None:
        prev_netid = '(None)'

    html = render_template('searchform.html',
        ampm=get_ampm(),
        current_time=get_current_time(),
        error_msg=error_msg,
        prev_netid=prev_netid)
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/searchresults', methods=['GET'])
def search_results():

    netid = request.args.get('netid')
    if (netid is None) or (netid.strip() == ''):
        error_msg = 'Please type an netid.'
        return redirect(url_for('search_form', error_msg=error_msg))

    student = search_students(netid)  # Exception handling omitted

    html = render_template('searchresults.html',
        ampm=get_ampm(),
        current_time=get_current_time(),
        netid=netid,
        student=student)
    response = make_response(html)
    response.set_cookie('prev_netid', netid)
    return response
