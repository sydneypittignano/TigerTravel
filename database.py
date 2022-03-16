#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Owen Travis
#-----------------------------------------------------------------------

from psycopg2 import connect

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
    list = []
    i = 0
    if startdate is not None:
        list.append(startdate)
    if enddate is not None:
        list.append(enddate)
    
    with connect(
        host='localhost', port=5432, user='ttadmins', 
        password='071020010307200204262002oms', database='tigertravel') as connection:

        with connection.cursor() as cursor:

            query_str = "SELECT * FROM rides"
            
            if startdate is not None:
                query_str += " WHERE startdate = %s"
                i = i + 1
            if enddate is not None:
                if (i != 0):
                    query_str += " AND enddate = %s"
                else:
                    query_str += " WHERE enddate = %s"
            
            print(list)
            cursor.execute(query_str, list)

            row = cursor.fetchone()
            while row is not None:
                rides.append(row)
                row = cursor.fetchone()

    return rides

#-----------------------------------------------------------------------

# For testing:

def _test():
    student = search_students('sydneyp')
    print(student)

if __name__ == '__main__':
    _test()
