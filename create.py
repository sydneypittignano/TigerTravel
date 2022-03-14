#!/usr/bin/env python

#-----------------------------------------------------------------------
# create.py
# Author: Owen Travis
#-----------------------------------------------------------------------

from sys import argv, stderr, exit
from psycopg2 import connect

#-----------------------------------------------------------------------

def main():

    if len(argv) != 1:
        print('Usage: python create.py', file=stderr)
        exit(1)

    try:
        with connect(
            host='localhost', port=5432, user='ttadmins', password='071020010307200204262002oms',
            database='tigertravel') as connection:

            with connection.cursor() as cursor:

                #-------------------------------------------------------

                cursor.execute("DROP TABLE IF EXISTS students")
                cursor.execute("CREATE TABLE students "
                    + "(netid TEXT, firstname TEXT, lastname TEXT, email TEXT,"+ 
                    " phone TEXT, strikes INTEGER)")
                cursor.execute("INSERT INTO students "
                    + "(netid, firstname, lastname, email, phone, strikes) "
                    + "VALUES ('sydneyp', 'Sydney', 'Pittignano', "
                    + "'sydneyp@princeton.edu', '(203)-914-7848', 1)")
                cursor.execute("INSERT INTO students "
                    + "(netid, firstname, lastname, email, phone, strikes) "
                    + "VALUES ('manyaz', 'Manya', 'Zhu', "
                    + "'manyaz@princeton.edu', '(609)-456-2795', 0)")
                cursor.execute("INSERT INTO students "
                    + "(netid, firstname, lastname, email, phone, strikes) "
                    + "VALUES ('otravis', 'Owen', 'Travis', "
                    + "'otravis@princeton.edu', '(847)-691-8322', 7)")

                #-------------------------------------------------------

                cursor.execute("DROP TABLE IF EXISTS rides")
                cursor.execute("CREATE TABLE rides "
                    + "(rideid INTEGER, startdate TEXT, enddate TEXT, "+ 
                    "origin TEXT, dest TEXT, starttime INTEGER, endtime INTEGER, num INTEGER)")
                cursor.execute("INSERT INTO rides (rideid, startdate, enddate, origin, dest, starttime, endtime, num) "
                    + "VALUES (1, '2-6-2022', '2-6-2022', 'Princeton', 'JFK', 100, 300, 1)")

                #-------------------------------------------------------

                cursor.execute("DROP TABLE IF EXISTS riders")
                cursor.execute("CREATE TABLE riders "
                    + "(rideid INTEGER, netid TEXT)")
                cursor.execute("INSERT INTO riders (rideid, netid) "
                    + "VALUES (1,'sydneyp')")

                #-------------------------------------------------------

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()