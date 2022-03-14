DROP TABLE IF EXISTS students;

CREATE TABLE students
(netid TEXT, firstname TEXT, lastname TEXT, email TEXT, phone TEXT, strikes INTEGER);

INSERT INTO students (netid, firstname, lastname, email, phone, strikes)
   VALUES ('sydneyp','Sydney', 'Pittignano', 'sydneyp@princeton.edu', '(203)-914-7848', 0);
INSERT INTO students (netid, firstname, lastname, email, phone, strikes)
   VALUES ('manyaz','Manya', 'Zhu', 'manyaz@princeton.edu', '(609)-456-2795', 0);
INSERT INTO students (netid, firstname, lastname, email, phone, strikes)
   VALUES ('otravis','Owen', 'Travis', 'otravis@princeton.edu', '(847)-691-8322', 1);
INSERT INTO students (netid, firstname, lastname, email, phone, strikes)
   VALUES ('bbob','Billy', 'Bob', 'bbob@bob.com', '(888)-888-8888', 20);

-- ---------------------------------------------------------------------

DROP TABLE IF EXISTS rides;

CREATE TABLE rides
(rideid INTEGER, startdate TEXT, enddate TEXT, origin TEXT, dest TEXT, starttime INTEGER, endtime INTEGER, num INTEGER);

INSERT INTO rides (rideid, startdate, enddate, origin, dest, starttime, endtime, num)
   VALUES (1, '2-6-2022', '2-6-2022', 'Princeton', 'JFK', 100, 300, 1);

-- ---------------------------------------------------------------------

DROP TABLE IF EXISTS riders;

CREATE TABLE orders
(rideid INTEGER, netid TEXT);

INSERT INTO rider (rideid, netid)
   VALUES (1,'sydneyp');

