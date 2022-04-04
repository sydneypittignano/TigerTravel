#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Owen Travis
#-----------------------------------------------------------------------

import os
from sys import stderr
from psycopg2 import connect
from ride import Ride

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
                filters.append('%'+str(starttime)+'%')
                stmt_str += "AND rides.starttime LIKE %s "
            if (endtime is not None) and (endtime != ''):
                filters.append('%'+str(endtime)+'%')
                stmt_str += "AND rides.endtime LIKE %s "

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
    with connect(
        host='localhost', port=5432, user='ttadmins', 
        password='071020010307200204262002oms', database='tigertravel') as connection:

        with connection.cursor() as cursor:

            stmt_str = "SELECT rideid FROM riders "
            stmt_str += "WHERE netid LIKE %s"

            cursor.execute(stmt_str, ['%'+my_netid+'%'])
            rideid = cursor.fetchone()[0]
            rides = []
            while rideid is not None:
                rides.append(from_rideid_get_ride(rideid))
                rideid = cursor.fetchone()

    return rides

#-----------------------------------------------------------------------

def from_rideid_get_ride(rideid):
    return get_rides(rideid, None, None, None, None)[0]

#-----------------------------------------------------------------------


# SELECT from the RIDERS table
# Given a rideid, return a list containing the netids of all riders
# that are associated with that rideid
def from_rideid_get_riders(rideid):
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
    info = [netid]
    stmt_str = "INSERT INTO students (netid, firstname, lastname, "
    stmt_str += "email, phone, strikes, count) VALUES (%s, '', '', '', '', 0, 1);"
    cursor.execute(stmt_str, info)

#-----------------------------------------------------------------------
 
def add_ride(netid, origin, dest, starttime, endtime):
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
 
           stmt_str = "INSERT INTO riders (rideid, netid) VALUES (%s, %s);"
          
           cursor.execute(stmt_str, [rideid, netid])

           from_netid_increment_count(cursor, netid)
 
#-----------------------------------------------------------------------

def from_netid_get_count(cursor, netid):
    stmt_str = "SELECT count FROM students WHERE netid LIKE %s"
    cursor.execute(stmt_str, [netid])
    return cursor.fetchone()[0]

#-----------------------------------------------------------------------

def from_netid_increment_count(cursor, netid):
    stmt_str = "UPDATE students SET count=count+1 WHERE netid LIKE %s"
    cursor.execute(stmt_str, [netid])

#-----------------------------------------------------------------------

# For testing:

#def _test():
    

# if __name__ == '__main__':
    # _test()
