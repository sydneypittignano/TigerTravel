#!/usr/bin/env python

#-----------------------------------------------------------------------
# display.py
# Authors: Owen Travis, Manya Zhu
#-----------------------------------------------------------------------

from sys import argv, stderr, exit
from psycopg2 import connect

#-----------------------------------------------------------------------

def main():

    if len(argv) != 1:
        print('Usage: python display.py', file=stderr)
        exit(1)

    try:
        with connect(
            host='localhost', port=5432, user='ttadmins', password='071020010307200204262002oms',
            database='tigertravel') as connection:

            with connection.cursor() as cursor:

                print('-------------------------------------------')
                print('students')
                print('-------------------------------------------')
                cursor.execute("SELECT * FROM students")
                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    row = cursor.fetchone()

                print('-------------------------------------------')
                print('rides')
                print('-------------------------------------------')
                cursor.execute("SELECT * FROM rides")
                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    row = cursor.fetchone()

                print('-------------------------------------------')
                print('riders')
                print('-------------------------------------------')
                cursor.execute("SELECT * FROM riders")
                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    row = cursor.fetchone()

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
