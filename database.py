#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Owen Travis
#-----------------------------------------------------------------------

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

def filter_rides(startdate, enddate, origin, dest, starttime, endtime):

    rides = []
    #list = []
    #i = 0
    #if startdate is not None:
        #list.append(startdate)
    #if enddate is not None:
        #list.append(enddate)
    
    with connect(
        host='localhost', port=5432, user='ttadmins', 
        password='071020010307200204262002oms', database='tigertravel') as connection:

        with connection.cursor() as cursor:

            query_str = "SELECT * FROM rides"
            
            #if startdate is not None:
                #query_str += " WHERE startdate = %s"
                #i = i + 1
            #if enddate is not None:
                #if (i != 0):
                    #query_str += " AND enddate = %s"
                #else:
                    #query_str += " WHERE enddate = %s"
            
            #print(list)
            #cursor.execute(query_str, list)
            cursor.execute(query_str)

            row = cursor.fetchone()
            while row is not None:
                rides.append(row)
                row = cursor.fetchone()

    return rides

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
           query_str += "starttime, endtime, num) VALUES ?;"
 
           cursor.execute(query_str, info)
 
           query_str = "INSERT INTO riders (rideid, netid) VALUES ?;"
          
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
   if startdate is not None:
       list.append(startdate)
   if enddate is not None:
       list.append(enddate)
   if origin is not None:
       list.append(origin)
   if dest is not None:
       list.append(dest)
   if starttime is not None:
       list.append(starttime)
   if endtime is not None:
       list.append(endtime)
 
   with connect(
       host='localhost', port=5432, user='ttadmins',
       password='071020010307200204262002oms', database='tigertravel') as connection:
 
       with connection.cursor() as cursor:
 
           stmt_str = "SELECT riders.netid, rides.startdate, rides.enddate, rides.origin, "
           stmt_str += "rides.dest, rides.starttime, rides.endtime FROM rides, riders "
           stmt_str += "WHERE rides.rideid=riders.rideid "
 
           if startdate is not None:
               stmt_str += "AND rides.startdate LIKE ? "
           if enddate is not None:
               stmt_str += "AND rides.enddate "
               stmt_str += "LIKE ? "
           if origin is not None:
               stmt_str += "AND rides.origin LIKE ? "
           if dest is not None:
               stmt_str += "AND rides.dest LIKE ? "
           if starttime is not None:
               stmt_str += "AND rides.starttime LIKE ? "
           if endtime is not None:
               stmt_str += "AND rides.endtime LIKE ? "
 
           stmt_str += "ORDER BY rides.startdate ASC, "
           stmt_str += "rides.starttime ASC, "
           stmt_str += "rides.origin ASC;"
 
           cursor.execute(stmt_str, list)
           row = cursor.fetchone()
 
           table = []
 
           while row is not None:
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
