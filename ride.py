#!/usr/bin/env python
 
#-----------------------------------------------------------------------
# ride.py
# Author: Manya Zhu
#-----------------------------------------------------------------------
 
class Ride:
 
   def __init__(self, rideid, origin, dest, starttime, endtime, num):
       self._rideid = rideid
       self._origin = origin
       self._dest = dest
       self._starttime = starttime
       self._endtime = endtime
       self._num = num
 
   def get_rideid(self):
       return self._rideid
 
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
       return (self._rideid, self._origin,
       self._dest, self._starttime, self._endtime, self._num)
 
   def to_dict(self):
       return {'rideid': self._rideid, 
       'origin': self._origin, 'dest': self._dest, 'starttime': self._starttime,
       'endtime': self._endtime, 'num': self._num}
 
#-----------------------------------------------------------------------
 
def _test():
   ride = Ride('1', 'princeton', 'JFK', '2020-06-23 15:00:00', '2020-06-23 19:00:00', 1)
   print(ride.to_tuple())
   print()
   print(ride.to_dict())
 
if __name__ == '__main__':
   _test()
 