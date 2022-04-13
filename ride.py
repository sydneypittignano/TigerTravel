#!/usr/bin/env python
 
#-----------------------------------------------------------------------
# ride.py
# Author: Manya Zhu
#-----------------------------------------------------------------------
 
class Ride:
 
   def __init__(self, riders, rideid, origin, dest, starttime, endtime, 
    num, reqrec, reqsent):
       self._riders = riders
       self._rideid = rideid
       self._origin = origin
       self._dest = dest
       self._starttime = starttime
       self._endtime = endtime
       self._num = num
       self._reqrec = reqrec
       self._reqsent = reqsent
 
   def get_riders(self):
       return self._riders

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

   def get_reqrec(self):
       return self._reqrec

   def get_reqsent(self):
       return self._reqsent
 
   def to_tuple(self):
       return (self._rideid, self._riders, self._origin,
       self._dest, self._starttime, self._endtime, self._num, self._reqrec, self._reqsent)
 
   def to_dict(self):
       return {'rideid': self._rideid, 'riders': self._riders,
       'origin': self._origin, 'dest': self._dest, 'starttime': self._starttime,
       'endtime': self._endtime, 'num': self._num, 'reqrec': self._reqrec, 'reqsent': self._reqsent
       }
    
   def hasOverlapWith(self, other):
       selfstart = self.get_starttime()
       selfend = self.get_endtime()
       otherstart = other.get_starttime()
       otherend = other.get_endtime()
       lateststart = max(selfstart, otherstart)
       earliestend = min(selfend, otherend)
       return (lateststart <= earliestend)

   def matchesRouteOf(self, other):
       if (self.get_dest() != other.get_dest()) or (self.get_origin() != other.get_origin()):
           return False
       return True
       
#-----------------------------------------------------------------------
 
def _test():
   ride = Ride('1', ['otravis'], 'princeton', 'JFK', '2020-06-23 15:00:00', '2020-06-23 19:00:00', 1, [1], [])
   print(ride.to_tuple())
   print()
   print(ride.to_dict())
 
if __name__ == '__main__':
   _test()
 