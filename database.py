#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Owen Travis
#-----------------------------------------------------------------------

from sys import stderr
from psycopg2 import connect
from ride import Ride

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
            stmt_str += "WHERE rideid = %s"

            cursor.execute(stmt_str, [rideid])
            riders = []
            rider = cursor.fetchone()
            while rider is not None:
                riders.append(rider[0])
                rider = cursor.fetchone()

    return riders

#-----------------------------------------------------------------------

# SELECT from the RIDERS table
# Given the netid of the current user, return a list of
# [rideid, reqrec, reqsent] for each matching row
def from_netid_get_reqinfos(my_netid):
    with connect(
        host='localhost', port=5432, user='ttadmins', 
        password='071020010307200204262002oms', database='tigertravel') as connection:

        with connection.cursor() as cursor:

            stmt_str = "SELECT rideid, reqrec, reqsent FROM riders "
            stmt_str += "WHERE netid LIKE %s"

            cursor.execute(stmt_str, ['%'+my_netid+'%'])
            reqinfos = []
            reqinfo = cursor.fetchone()
            while reqinfo is not None:
                reqinfos.append(reqinfo)
                reqinfo = cursor.fetchone()

    return reqinfos

#-----------------------------------------------------------------------
 
def add_student(netid, firstname, lastname, email, phone, strikes):
   with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:
 
           info = [netid, firstname, lastname, email, phone, strikes]
           stmt_str = "INSERT INTO students (netid, firstname, lastname, "
           stmt_str += "email, phone, strikes) VALUES ?;"
 
           cursor.execute(stmt_str, info)
 
   return
  
#-----------------------------------------------------------------------
 
def add_strike(netid):
   with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:

           stmt_str = "UPDATE students SET strikes=strikes+1 WHERE netid=?;"
 
           cursor.execute(stmt_str, [netid])
 
   return
 
#-----------------------------------------------------------------------
 
def add_ride(netid, rideid, origin, dest, starttime, endtime):
   with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:
 
           info = [rideid, origin, dest, starttime, endtime]
           stmt_str = "INSERT INTO rides (rideid, origin, dest, "
           stmt_str += "starttime, endtime, num) VALUES (%s, %s, %s, %s, %s, 1);"
 
           cursor.execute(stmt_str, info)
 
           stmt_str = "INSERT INTO riders (rideid, netid) VALUES (%s, %s);"
          
           cursor.execute(stmt_str, [rideid, netid])
 
   return
 
#-----------------------------------------------------------------------
 
def join_ride(netid, prev_rideid, new_rideid):
   with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:
 
           stmt_str = "UPDATE riders SET rideid = ? WHERE "
           stmt_str += "netid = ? AND rideid = ?;"
 
           cursor.execute(stmt_str, [prev_rideid, netid, new_rideid])
 
           #should the old ride in rides stay the same? should we change rideid?
 
   return
 
#-----------------------------------------------------------------------
 
def filter_rides(rideid, origin, dest, starttime, endtime):
 
   with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:
 
            rides = fetch_rides(cursor, rideid, origin, dest, starttime, endtime)
            return rides
 
#-----------------------------------------------------------------------

def fetch_rides(cursor, rideid, origin, dest, starttime, endtime):
    filters = []

    stmt_str = "SELECT * FROM rides WHERE true "
    if (rideid is not None) and (rideid != ''):
        stmt_str += "AND rides.rideid=%s "
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
        row = list(row)
        row[3] = row[3].strftime("%c")
        row[4] = row[4].strftime("%c")
        riders = from_rideid_get_riders(row[0])
        ride = Ride(row[0], riders, str(row[1]),
        str(row[2]), row[3], row[4], row[5])
        rides.append(ride)
        row = cursor.fetchone()

    return rides

# For testing:

#def _test():
    

# if __name__ == '__main__':
    # _test()
