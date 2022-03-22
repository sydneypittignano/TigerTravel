#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Owen Travis
#-----------------------------------------------------------------------

from sys import stderr
from psycopg2 import connect
from ride import Ride

#-----------------------------------------------------------------------

def search_students(netid):

    with connect(
        host='localhost', port=5432, user='ttadmins', 
        password='071020010307200204262002oms', database='tigertravel') as connection:

        with connection.cursor() as cursor:

            query_str = "SELECT * FROM students "
            query_str += "WHERE netid LIKE %s"

            cursor.execute(query_str, ['%'+netid+'%'])


            student = cursor.fetchone()

    return student


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
 
def add_ride(netid, rideid, startdate, enddate, origin, dest, starttime, endtime, num):
   with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:
 
           info = [rideid, startdate, enddate, origin, dest, starttime, endtime, num]
           query_str = "INSERT INTO rides (rideid, startdate, enddate, origin, dest, "
           query_str += "starttime, endtime, num) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
 
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
 
def filter_rides(startdate, enddate, origin, dest, starttime, endtime):
   list = []
   if (startdate is not None) and (startdate != ''):
       list.append('%'+str(startdate)+'%')
   if (enddate is not None) and (enddate != ''):
       list.append('%'+str(enddate)+'%')
   if (origin is not None) and (origin != ''):
       list.append('%'+str(origin)+'%')
   if (dest is not None) and (dest != ''):
       list.append('%'+str(dest)+'%')
   if (starttime is not None) and (starttime != ''):
       list.append('%'+str(starttime)+'%')
   if (endtime is not None) and (endtime != ''):
       list.append('%'+str(endtime)+'%')
 
   with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:
 
            stmt_str = "SELECT rides.rideid, rides.startdate, rides.enddate, rides.origin, "
            stmt_str += "rides.dest, rides.starttime, rides.endtime, rides.num FROM rides, riders "
            stmt_str += "WHERE rides.rideid=riders.rideid "
 
            if (startdate is not None) and (startdate != ''):
                stmt_str += "AND rides.startdate LIKE %s "
            if (enddate is not None) and (enddate != ''):
               stmt_str += "AND rides.enddate "
               stmt_str += "LIKE %s "
            if (origin is not None) and (origin != ''):
               stmt_str += "AND rides.origin LIKE %s "
            if (dest is not None) and (dest != ''):
               stmt_str += "AND rides.dest LIKE %s "
            if (starttime is not None) and (starttime != ''):
               stmt_str += "AND rides.starttime LIKE %s "
            if (endtime is not None) and (endtime != ''):
               stmt_str += "AND rides.endtime LIKE %s "
 
            stmt_str += "ORDER BY rides.startdate ASC, "
            stmt_str += "rides.starttime ASC, "
            stmt_str += "rides.origin ASC;"
 
            cursor.execute(stmt_str, list)
            row = cursor.fetchone()
 
            table = []
 
            while row is not None:
               print(row[0], file=stderr)
               print(row[1], file=stderr)
               print(row[2], file=stderr)
               print(row[3], file=stderr)
               print(row[4], file=stderr)
               print(row[5], file=stderr)
               print(row[6], file=stderr)
               print(row[7], file=stderr)
               ride_row = Ride(str(row[0]), str(row[1]),
               str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]),
               str(row[7]))
               table.append(ride_row)
               row = cursor.fetchone()
 
            return table
 
#-----------------------------------------------------------------------


# For testing:

def _test():
    student = search_students('sydneyp')
    print(student)

if __name__ == '__main__':
    _test()
