#!/usr/bin/env python
 
#-----------------------------------------------------------------------
# ride.py
# Author: Manya Zhu
#-----------------------------------------------------------------------
 
class Ride:
 
   def __init__(self, rideid, startdate, enddate, origin, dest, starttime, endtime, num):
       self._rideid = rideid
       self._startdate = startdate
       self._enddate = enddate
       self._origin = origin
       self._dest = dest
       self._starttime = starttime
       self._endtime = endtime
       self._num = num
 
   def get_rideid(self):
       return self._rideid
 
   def get_startdate(self):
       return self._startdate
 
   def get_enddate(self):
       return self._enddate
 
   def get_origin(self):
       return self._origin
 
   def get_dest(self):
       return self._dest
 
   def get_starttime(self):
       return self._starttime
  
   def get_endtime(self):
       return self._endtime
  
   def get_num(self):
       return self._num
 
   def to_tuple(self):
       return (self._rideid, self._startdate, self._enddate, self._origin,
       self._dest, self._starttime, self._endtime, self._num)
 
   def to_dict(self):
       return {'rideid': self._rideid, 'startdate': self._startdate, 'enddate': self._enddate,
       'origin': self._origin, 'dest': self._dest, 'starttime': self._starttime,
       'endtime': self._endtime, 'num': self._num}
 
#-----------------------------------------------------------------------
 
def _test():
   ride = Ride('1', '2/4/2003', '2/4/2003', 'princeton', 'JFK', 100, 400, 1)
   print(ride.to_tuple())
   print()
   print(ride.to_dict())
 
if __name__ == '__main__':
   _test()
 