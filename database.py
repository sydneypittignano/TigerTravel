#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Owen Travis
#-----------------------------------------------------------------------

from sys import stderr
from psycopg2 import connect
from ride import Ride
from datetime import datetime

#-----------------------------------------------------------------------

def from_rideid_get_riders(rideid):
    with connect(
        host='localhost', port=5432, user='ttadmins', 
        password='071020010307200204262002oms', database='tigertravel') as connection:

        with connection.cursor() as cursor:

            query_str = "SELECT netid FROM riders "
            query_str += "WHERE rideid = %s"

            cursor.execute(query_str, [rideid])
            riders = []
            rider = cursor.fetchone()
            while rider is not None:
                riders.append(rider[0])
                rider = cursor.fetchone()

    return riders

#-----------------------------------------------------------------------
 
def add_student(netid, firstname, lastname, email, phone, strikes):
   with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:
 
           info = [netid, firstname, lastname, email, phone, strikes]
           query_str = "INSERT INTO students (netid, firstname, lastname, "
           query_str += "email, phone, strikes) VALUES ?;"
 
           cursor.execute(query_str, info)
 
   return
  
#-----------------------------------------------------------------------
 
def add_strike(netid):
   with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:

           query_str = "UPDATE students SET strikes=strikes+1 WHERE netid=?;"
 
           cursor.execute(query_str, [netid])
 
   return
 
#-----------------------------------------------------------------------
 
def add_ride(netid, rideid, origin, dest, starttime, endtime):
   with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:
 
           info = [rideid, origin, dest, starttime, endtime]
           query_str = "INSERT INTO rides (rideid, origin, dest, "
           query_str += "starttime, endtime, num) VALUES (%s, %s, %s, %s, %s, 1);"
 
           cursor.execute(query_str, info)
 
           query_str = "INSERT INTO riders (rideid, netid) VALUES (%s, %s);"
          
           cursor.execute(query_str, [rideid, netid])
 
   return
 
#-----------------------------------------------------------------------
 
def join_ride(netid, prev_rideid, new_rideid):
   with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:
 
           query_str = "UPDATE riders SET rideid = ? WHERE "
           query_str += "netid = ? AND rideid = ?;"
 
           cursor.execute(query_str, [prev_rideid, netid, new_rideid])
 
           #should the old ride in rides stay the same? should we change rideid?
 
   return
 
#-----------------------------------------------------------------------
 
def filter_rides(origin, dest, starttime, endtime):
   filters = []
   if (origin is not None) and (origin != ''):
       filters.append('%'+str(origin)+'%')
   if (dest is not None) and (dest != ''):
       filters.append('%'+str(dest)+'%')
   if (starttime is not None) and (starttime != ''):
       filters.append('%'+str(starttime)+'%')
   if (endtime is not None) and (endtime != ''):
       filters.append('%'+str(endtime)+'%')
 
   with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:
 
            stmt_str = "SELECT rides.rideid, rides.origin, "
            stmt_str += "rides.dest, rides.starttime, rides.endtime, rides.num FROM rides, riders "
            stmt_str += "WHERE rides.rideid=riders.rideid "
 
            if (origin is not None) and (origin != ''):
               stmt_str += "AND rides.origin LIKE %s "
            if (dest is not None) and (dest != ''):
               stmt_str += "AND rides.dest LIKE %s "
            if (starttime is not None) and (starttime != ''):
               stmt_str += "AND rides.starttime LIKE %s "
            if (endtime is not None) and (endtime != ''):
               stmt_str += "AND rides.endtime LIKE %s "
 
            stmt_str += "ORDER BY rides.starttime ASC, "
            stmt_str += "rides.origin ASC;"
 
            cursor.execute(stmt_str, filters)
            row = cursor.fetchone()
 
            table = []
 
            while row is not None:
                row = list(row)
                row[3] = row[3].strftime("%c")
                row[4] = row[4].strftime("%c")
                ride_row = Ride(str(row[0]), str(row[1]),
                str(row[2]), row[3], row[4], str(row[5]))
                table.append(ride_row)
                row = cursor.fetchone()
 
            return table
 
#-----------------------------------------------------------------------


# For testing:

#def _test():
    

# if __name__ == '__main__':
    # _test()
