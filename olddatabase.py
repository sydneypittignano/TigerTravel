#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Owen Travis
#-----------------------------------------------------------------------

import os
from sys import stderr
from psycopg2 import connect
from ride import Ride
from datetime import datetime

#-----------------------------------------------------------------------



#-----------------------------------------------------------------------

# returns a list of Ride objects that contain all relevant information
# about the rides. takes filters as arguments.
def get_rides(rideid, origin, dest, starttime, endtime):
    with connect(
    host='localhost', port=5432, user='ttadmins',
    password='071020010307200204262002oms', database='tigertravel') as connection:

        with connection.cursor() as cursor:
            filters = []
            stmt_str = "SELECT * FROM rides WHERE true "
            if (rideid is not None) and (rideid != ''):
                stmt_str += "AND rides.rideid LIKE %s "
                filters.append(rideid)
            if (origin is not None) and (origin != ''):
                filters.append('%'+str(origin)+'%')
                stmt_str += "AND rides.origin LIKE %s "
            if (dest is not None) and (dest != ''):
                filters.append('%'+str(dest)+'%')
                stmt_str += "AND rides.dest LIKE %s "
            if (starttime is not None) and (starttime != ''):
                filters.append(starttime)
                stmt_str += "AND rides.endtime >= %s "
            if (endtime is not None) and (endtime != ''):
                filters.append(endtime)
                stmt_str += "AND rides.starttime <= %s "

            stmt_str += "ORDER BY rides.starttime ASC, "
            stmt_str += "rides.origin ASC;"

            cursor.execute(stmt_str, filters)
            row = cursor.fetchone()

            rides = []

            while row is not None:
                riders = from_rideid_get_riders(row[5])
                ride = Ride(riders, row[5], row[0],
                row[1], row[2], row[3], row[4], row[6], row[7])
                rides.append(ride)
                row = cursor.fetchone()

            return rides

#-----------------------------------------------------------------------

def from_netid_get_rides(my_netid):

    assert my_netid is not None

    with connect(
        host='localhost', port=5432, user='ttadmins', 
        password='071020010307200204262002oms', database='tigertravel') as connection:

        with connection.cursor() as cursor:

            stmt_str = "SELECT riders.rideid FROM riders, rides "
            stmt_str += "WHERE riders.netid LIKE %s AND riders.rideid = rides.rideid "
            stmt_str += "ORDER BY rides.starttime ASC, "
            stmt_str += "rides.origin ASC;"

            cursor.execute(stmt_str, ['%'+my_netid+'%'])
            rideid = cursor.fetchone()
            rides = []
            while rideid is not None:
                rides.append(from_rideid_get_ride(rideid[0]))
                rideid = cursor.fetchone()

    return rides

#-----------------------------------------------------------------------

def from_rideid_get_ride(rideid):
    assert rideid is not None
    return get_rides(rideid, None, None, None, None)[0]

#-----------------------------------------------------------------------


# SELECT from the RIDERS table
# Given a rideid, return a list containing the netids of all riders
# that are associated with that rideid
def from_rideid_get_riders(rideid):
    assert rideid is not None
    with connect(
        host='localhost', port=5432, user='ttadmins', 
        password='071020010307200204262002oms', database='tigertravel') as connection:

        with connection.cursor() as cursor:

            stmt_str = "SELECT netid FROM riders "
            stmt_str += "WHERE rideid LIKE %s"

            cursor.execute(stmt_str, [rideid])
            riders = []
            rider = cursor.fetchone()
            while rider is not None:
                riders.append(rider[0])
                rider = cursor.fetchone()

    return riders

#-----------------------------------------------------------------------

def check_student(netid):
    assert netid is not None
    with connect(
    host='localhost', port=5432, user='ttadmins',
    password='071020010307200204262002oms', database='tigertravel') as connection:
 
        with connection.cursor() as cursor:
 
            info = [netid]
            stmt_str = "SELECT * FROM students WHERE netid = %s"
            cursor.execute(stmt_str, info)

            row = cursor.fetchone()
            if row is None:
                add_student(cursor, netid)

#-----------------------------------------------------------------------

def add_student(cursor, netid):
    assert cursor is not None
    assert netid is not None
    info = [netid]
    stmt_str = "INSERT INTO students (netid, strikes, count) VALUES (%s, 0, 1);"
    cursor.execute(stmt_str, info)

#-----------------------------------------------------------------------
 
def add_ride(netid, origin, dest, starttime, endtime):
   assert netid is not None 
   assert origin is not None
   assert dest is not None
   assert starttime is not None
   assert endtime is not None


   with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:

           count = from_netid_get_count(cursor, netid)
           rideid = netid + '-' + str(count+1)
 
           info = [rideid, origin, dest, starttime, endtime]
           stmt_str = "INSERT INTO rides (rideid, origin, dest, "
           stmt_str += "starttime, endtime, num, reqrec, reqsent) VALUES (%s, %s, %s, %s, %s, 1, '{}', '{}');"
 
           cursor.execute(stmt_str, info)
 
           stmt_str = "INSERT INTO riders (rideid, netid, starttime, endtime) VALUES (%s, %s, %s, %s);"
          
           cursor.execute(stmt_str, [rideid, netid, starttime, endtime])

           from_netid_increment_count(cursor, netid)

           return rideid
 
#-----------------------------------------------------------------------

def from_netid_get_count(cursor, netid):
    assert cursor is not None
    assert netid is not None
    stmt_str = "SELECT count FROM students WHERE netid LIKE %s"
    cursor.execute(stmt_str, [netid])
    return cursor.fetchone()[0]

#-----------------------------------------------------------------------

def from_netid_increment_count(cursor, netid):
    assert cursor is not None
    assert netid is not None
    stmt_str = "UPDATE students SET count=count+1 WHERE netid LIKE %s"
    cursor.execute(stmt_str, [netid])

#-----------------------------------------------------------------------

def send_request(joining_rideid, sending_rideid):
    assert joining_rideid is not None
    assert sending_rideid is not None
    with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:
           send_request_stmt(cursor, joining_rideid, sending_rideid)

#-----------------------------------------------------------------------

def send_request_stmt(cursor, joining_rideid, sending_rideid):
    assert cursor is not None
    assert joining_rideid is not None
    assert sending_rideid is not None
    stmt_str = "UPDATE rides SET reqrec=array_append(reqrec, %s)"
    stmt_str += " WHERE rideid = %s"
    cursor.execute(stmt_str, [sending_rideid, joining_rideid])

    stmt_str = "UPDATE rides SET reqsent=array_append(reqsent, %s)"
    stmt_str += " WHERE rideid = %s"
    cursor.execute(stmt_str, [joining_rideid, sending_rideid])

#-----------------------------------------------------------------------

def cancel_request(joining_rideid, sending_rideid):
    assert joining_rideid is not None
    assert sending_rideid is not None
    with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:
           cancel_request_stmt(cursor, joining_rideid, sending_rideid)

#-----------------------------------------------------------------------

def cancel_request_stmt(cursor, joining_rideid, sending_rideid):
    assert cursor is not None
    assert joining_rideid is not None
    assert sending_rideid is not None
    stmt_str = "UPDATE rides SET reqrec=array_remove(reqrec, %s)"
    stmt_str += " WHERE rideid = %s"
    cursor.execute(stmt_str, [sending_rideid, joining_rideid])

    stmt_str = "UPDATE rides SET reqsent=array_remove(reqsent, %s)"
    stmt_str += " WHERE rideid = %s"
    cursor.execute(stmt_str, [joining_rideid, sending_rideid])

#-----------------------------------------------------------------------

def accept_request(joining_rideid, sending_rideid):
    assert joining_rideid is not None
    assert sending_rideid is not None
    with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:

           joining_ride = from_rideid_get_ride(joining_rideid)
           sending_ride = from_rideid_get_ride(sending_rideid)

           lateststart = max(joining_ride.get_starttime(), sending_ride.get_starttime())

           earliestend = min(joining_ride.get_endtime(), sending_ride.get_endtime())

           newnum = joining_ride.get_num() + sending_ride.get_num()

           stmt_str = "UPDATE rides SET starttime = %s, endtime=%s, num=%s, reqrec=array_remove(reqrec, %s) WHERE rideid=%s"
           cursor.execute(stmt_str, [lateststart, earliestend, newnum, sending_rideid, joining_rideid])

           # look at reqrec and reqsent for joining_ride. if any are not valid, we delete them.
           temp_new_ride = Ride(None, None, None, None, lateststart, earliestend, None, None, None)

           for reqrec in joining_ride.get_reqrec():
               reqrec_ride = from_rideid_get_ride(reqrec)
               
               if (not reqrec_ride.hasOverlapWith(temp_new_ride)):
                   cancel_request_stmt(cursor, joining_rideid, reqrec)
           
           for reqsent in joining_ride.get_reqsent():
               reqsent_ride = from_rideid_get_ride(reqsent)

               if (not reqsent_ride.hasOverlapWith(temp_new_ride)):
                   cancel_request_stmt(cursor, reqsent, joining_rideid)

           # look at reqrec and reqsent for sending_ride. we must cancel all of these requests. if any are valid, we check that they are not already in joining_ride reqrec and reqsent and then add them.

           for sending_reqrec in sending_ride.get_reqrec():
               if (sending_reqrec != joining_rideid):
                   sending_reqrec_ride = from_rideid_get_ride(sending_reqrec)
                   if (sending_reqrec_ride.hasOverlapWith(temp_new_ride) and sending_reqrec not in joining_ride.get_reqrec()):

                       # joining_rideid is joining_ride
                       # sending_reqrec is sending_ride
                       send_request_stmt(cursor, joining_rideid, sending_reqrec)

                   # sending_rideid is joining_ride
                   # sending_reqrec is sending_ride
                   cancel_request_stmt(cursor, sending_rideid, sending_reqrec)
            
           for sending_reqsent in sending_ride.get_reqsent():
               if (sending_reqsent != joining_rideid):
                   sending_reqsent_ride = from_rideid_get_ride(sending_reqsent)
                   if (sending_reqsent_ride.hasOverlapWith(temp_new_ride) and sending_reqsent not in joining_ride.get_reqsent()):
                       
                       # sending_reqsent is joining_ride
                       # joining_rideid is sending_ride
                       send_request_stmt(cursor, sending_reqsent, joining_rideid)
                    
                   # sending_reqsent is joining_ride
                   # sending_rideid is sending_ride
                   cancel_request_stmt(cursor, sending_reqsent, sending_rideid)
                   
           # delete sending ride
           stmt_str = "DELETE FROM rides WHERE rideid = %s"
           cursor.execute(stmt_str, [sending_rideid])

           # change riders table
           stmt_str = "UPDATE riders SET rideid=%s WHERE rideid=%s"
           cursor.execute(stmt_str, [joining_rideid, sending_rideid])

#-----------------------------------------------------------------------

def delete_ride(rideid):
    assert rideid is not None
    with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:

           # delete reqrec and reqsent of ride being deleted
           ride = from_rideid_get_ride(rideid)

           for reqrec in ride.get_reqrec():
               # joining_rideid is rideid
               # sending_rideid is reqrec
               cancel_request_stmt(cursor, rideid, reqrec)
            
           for reqsent in ride.get_reqsent():
               # joining_rideid  is reqsent
               # sending_rideid is rideid
               cancel_request_stmt(cursor, reqsent, rideid)
            
           # delete from rides table
           stmt_str = "DELETE FROM rides WHERE rideid = %s"
           cursor.execute(stmt_str, [rideid])

           # delete from riders table
           stmt_str = "DELETE FROM riders WHERE rideid=%s"
           cursor.execute(stmt_str, [rideid])

#-----------------------------------------------------------------------

def decline_request(joining_rideid, sending_rideid):
    assert joining_rideid is not None
    assert sending_rideid is not None
    cancel_request(joining_rideid, sending_rideid)

#-----------------------------------------------------------------------

def leave_ride(rideid, netid):
    assert rideid is not None
    assert netid is not None
    with connect(
        host='localhost', port=5432, user='ttadmins',
        password='071020010307200204262002oms', database='tigertravel') as connection:
 
        with connection.cursor() as cursor:
            # give new_rideid in riders table
            count = from_netid_get_count(cursor, netid)
            new_rideid = netid + '-' + str(count+1)
            stmt_str = "UPDATE riders SET rideid=%s WHERE netid=%s AND rideid=%s"
            cursor.execute(stmt_str, [new_rideid, netid, rideid])
            from_netid_increment_count(cursor, netid)

            # get my starttime/endtime
            stmt_str = "SELECT starttime, endtime FROM riders WHERE rideid=%s"
            cursor.execute(stmt_str, [new_rideid])
            row = cursor.fetchone()
            my_starttime = row[0]
            my_endtime = row[1]

            # make new ride in rides table
            ride = from_rideid_get_ride(rideid)
            info = [new_rideid, ride.get_origin(), ride.get_dest(), my_starttime, my_endtime]
            stmt_str = "INSERT INTO rides (rideid, origin, dest, "
            stmt_str += "starttime, endtime, num, reqrec, reqsent) VALUES (%s, %s, %s, %s, %s, 1, '{}', '{}');"
            cursor.execute(stmt_str, info)

            # find new starttime/endtime
            stmt_str = "SELECT starttime, endtime FROM riders WHERE rideid=%s"
            cursor.execute(stmt_str, [rideid])
            row = cursor.fetchone()
            starttimes = []
            endtimes = []
            while row is not None:
                starttimes.append(row[0])
                endtimes.append(row[1])
                row = cursor.fetchone()
            lateststart = max(starttimes)
            earliestend = min(endtimes)

            # update starttime/endtime/num
            stmt_str = "UPDATE rides SET starttime=%s, endtime=%s, num=num-1 WHERE rideid=%s"
            cursor.execute(stmt_str, [lateststart, earliestend, rideid])

            
#-----------------------------------------------------------------------

def get_suggested(ride, incoming, outgoing):
    assert ride is not None
    assert incoming is not None
    assert outgoing is not None
    suggested = []
    my_origin = ride.get_origin()
    my_dest = ride.get_dest()
    my_starttime = ride.get_starttime()
    my_endtime = ride.get_endtime()

    unfiltered_suggestions = get_rides(None, my_origin, my_dest, my_starttime, my_endtime)

    for suggestion in unfiltered_suggestions:
        valid = True
        if suggestion.get_rideid() == ride.get_rideid():
            valid = False
            continue
        for incomingride in incoming:
            if suggestion.get_rideid() == incomingride.get_rideid():
                valid = False
                break
        if valid == False:
            continue
        for outgoingride in outgoing:
            if suggestion.get_rideid() == outgoingride.get_rideid():
                valid = False
                break
        if valid == True:
            suggested.append(suggestion)

    return suggested

#-----------------------------------------------------------------------

def from_netid_get_reqnum(my_netid):
    assert my_netid is not None
    my_rides = from_netid_get_rides(my_netid)
    future_rides = []
    for ride in my_rides:
        if ride.get_endtime() >= datetime.now():
            future_rides.append(ride)

    request_num = 0
    for ride in future_rides:
        request_num += len(ride.get_reqrec())
    return request_num

#-----------------------------------------------------------------------

def edit_ride(old_rideid, new_origin, new_dest, new_starttime, new_endtime):
    assert old_rideid is not None
    assert new_origin is not None
    assert new_dest is not None
    assert new_starttime is not None
    assert new_endtime is not None

    with connect(
        host='localhost', port=5432, user='ttadmins',
        password='071020010307200204262002oms', database='tigertravel') as connection:
 
        with connection.cursor() as cursor:

            old_ride = from_rideid_get_ride(old_rideid)
            new_starttime_datetime = datetime.strptime(new_starttime, '%m/%d/%Y, %I:%M %p')
            new_endtime_datetime = datetime.strptime(new_endtime, '%m/%d/%Y, %I:%M %p')
            temp_new_ride = Ride(None, None, None, None, new_starttime_datetime, new_endtime_datetime, None, None, None)

            #clear reqrec and reqsent if origin or destination change
            if ((old_ride.get_origin() != new_origin) or (old_ride.get_dest() != new_dest)):

                for reqrec in old_ride.get_reqrec():
                    # joining_rideid is old_rideid
                    # sending_rideid is reqrec
                    cancel_request_stmt(cursor, old_rideid, reqrec)
                
                for reqsent in old_ride.get_reqsent():
                    # joining_rideid is reqsent
                    # sending_rideid is old_rideid
                    cancel_request_stmt(cursor, reqsent, old_rideid)
    
            #for every reqrec and reqsent
            else:
                for reqrec in old_ride.get_reqrec():
                    reqrec_ride = from_rideid_get_ride(reqrec)
                    if (not reqrec_ride.hasOverlapWith(temp_new_ride)):
                        cancel_request_stmt(cursor, old_rideid, reqrec)
                for reqsent in old_ride.get_reqsent():
                    reqsent_ride = from_rideid_get_ride(reqsent)
                    if (not reqsent_ride.hasOverlapWith(temp_new_ride)):
                        cancel_request_stmt(cursor, reqsent, old_rideid)

            stmt_str = "UPDATE rides SET origin=%s, dest=%s, starttime=%s, endtime=%s WHERE rideid=%s"
            cursor.execute(stmt_str, [new_origin, new_dest, new_starttime, new_endtime, old_rideid])

            # only works if editing as a single rider, which is all we permit at the moment
            stmt_str = "UPDATE riders SET starttime=%s, endtime=%s WHERE rideid=%s"
            cursor.execute(stmt_str, [new_starttime, new_endtime, old_rideid])

#-----------------------------------------------------------------------

def report_riders(reported):
    with connect(
        host='localhost', port=5432, user='ttadmins',
        password='071020010307200204262002oms', database='tigertravel') as connection:
 
        with connection.cursor() as cursor:
            for reported_rider in reported:
                stmt_str = "UPDATE students SET strikes=strikes+1 WHERE netid=%s"
                cursor.execute(stmt_str, [reported_rider])

#-----------------------------------------------------------------------

# For testing:

#def _test():
    

# if __name__ == '__main__':
    # _test()
