--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2
DROP TABLE IF EXISTS riders;
DROP TABLE IF EXISTS rides;
DROP TABLE IF EXISTS students;

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: riders; Type: TABLE; Schema: public; Owner: ttadmins
--

CREATE TABLE public.riders (
    netid text,
    rideid text,
    starttime timestamp without time zone,
    endtime timestamp without time zone
);


--
-- Name: rides; Type: TABLE; Schema: public; Owner: ttadmins
--

CREATE TABLE public.rides (
    origin text,
    dest text,
    starttime timestamp without time zone,
    endtime timestamp without time zone,
    num integer,
    rideid text,
    reqrec text[],
    reqsent text[]
);


--
-- Name: students; Type: TABLE; Schema: public; Owner: ttadmins
--

CREATE TABLE public.students (
    netid text,
    firstname text,
    lastname text,
    email text,
    phone text,
    strikes integer,
    count integer
);


--
-- Data for Name: riders; Type: TABLE DATA; Schema: public; Owner: ttadmins
--

COPY public.riders (netid, rideid, starttime, endtime) FROM stdin;
sydneyp	sydneyp-2	2022-04-16 01:00:00	2022-04-17 01:00:00
otravis	otravis-10	2022-04-26 10:00:00	2022-04-26 11:30:00
otravis	otravis-9	2022-04-21 16:30:00	2022-04-21 17:30:00
sydneyp	otravis-9	2022-04-21 16:30:00	2022-04-21 17:30:00
otravis	otravis-11	2022-04-24 23:00:00	2022-04-25 01:00:00
sydneyp	sydneyp-5	2022-04-27 19:00:00	2022-04-27 21:00:00
otravis	otravis-12	2022-04-29 09:00:00	2022-04-29 12:00:00
sydneyp	sydneyp-8	2022-04-29 08:45:00	2022-04-29 09:46:00
otravis	otravis-14	2022-07-04 12:00:00	2022-07-04 14:00:00
otravis	otravis-15	2022-07-04 18:00:00	2022-07-04 19:30:00
manyaz	otravis-14	2022-07-04 12:00:00	2022-07-04 14:00:00
manyaz	otravis-15	2022-07-04 18:00:00	2022-07-04 19:30:00
otravis	otravis-16	2022-06-01 09:15:00	2022-06-01 09:55:00
sydneyp	otravis-16	2022-06-01 09:15:00	2022-06-01 09:55:00
sydneyp	sydneyp-13	2022-06-04 17:00:00	2022-06-04 18:30:00
otravis	otravis-17	2022-06-07 19:00:00	2022-06-07 19:45:00
manyaz	manyaz-5	2022-06-06 07:00:00	2022-06-06 09:00:00
manyaz	manyaz-6	2022-06-14 12:00:00	2022-06-14 13:00:00
otravis	otravis-18	2022-07-12 08:30:00	2022-07-12 08:45:00
manyaz	otravis-18	2022-07-12 08:30:00	2022-07-12 08:45:00
sydneyp	otravis-18	2022-07-12 08:30:00	2022-07-12 08:45:00
sydneyp	otravis-14	2022-07-04 12:00:00	2022-07-04 14:00:00
manyaz	manyaz-8	2022-08-20 16:30:00	2022-08-20 16:50:00
otravis	otravis-19	2022-08-25 11:00:00	2022-08-25 11:45:00
sydneyp	otravis-19	2022-08-25 11:00:00	2022-08-25 11:45:00
otravis	otravis-20	2022-04-29 17:45:00	2022-04-29 18:00:00
manyaz	otravis-20	2022-04-29 17:45:00	2022-04-29 18:00:00
sydneyp	otravis-20	2022-04-29 17:45:00	2022-04-29 18:00:00
tigertravel	otravis-20	2022-04-29 17:45:00	2022-04-29 18:00:00
sydneyp	sydneyp-16	2022-07-01 16:00:00	2022-07-01 17:00:00
tigertravel	tigertravel-3	2022-07-03 19:00:00	2022-07-03 20:00:00
\.


--
-- Data for Name: rides; Type: TABLE DATA; Schema: public; Owner: ttadmins
--

COPY public.rides (origin, dest, starttime, endtime, num, rideid, reqrec, reqsent) FROM stdin;
Princeton University	Nassau Park Pavilion (Wegmans, Party City, etc.)	2022-04-16 01:00:00	2022-04-17 01:00:00	1	sydneyp-2	{}	{}
Princeton University	LaGuardia Airport (LGA)	2022-04-26 10:00:00	2022-04-26 11:30:00	1	otravis-10	{}	{}
Nassau Park Pavilion (Wegmans, Party City, etc.)	Philadelphia International Airport (PHL)	2022-04-21 16:30:00	2022-04-21 17:30:00	2	otravis-9	{}	{}
Philadelphia International Airport (PHL)	Princeton University	2022-04-24 23:00:00	2022-04-25 01:00:00	1	otravis-11	{}	{}
Nassau Park Pavilion (Wegmans, Party City, etc.)	Princeton University	2022-04-27 19:00:00	2022-04-27 21:00:00	1	sydneyp-5	{}	{}
John F. Kennedy International Airport (JFK)	Princeton University	2022-04-29 09:00:00	2022-04-29 12:00:00	1	otravis-12	{sydneyp-8}	{}
John F. Kennedy International Airport (JFK)	Princeton University	2022-04-29 08:45:00	2022-04-29 09:46:00	1	sydneyp-8	{}	{otravis-12}
Princeton University	Philadelphia International Airport (PHL)	2022-06-06 07:00:00	2022-06-06 09:00:00	1	manyaz-5	{}	{}
Philadelphia International Airport (PHL)	Princeton University	2022-06-14 12:00:00	2022-06-14 13:00:00	1	manyaz-6	{}	{}
Princeton University	LaGuardia Airport (LGA)	2022-04-29 17:45:00	2022-04-29 18:00:00	4	otravis-20	{}	{}
Nassau Park Pavilion (Wegmans, Party City, etc.)	Princeton University	2022-07-01 16:00:00	2022-07-01 17:00:00	1	sydneyp-16	{}	{}
Princeton University	LaGuardia Airport (LGA)	2022-07-12 08:30:00	2022-07-12 08:45:00	3	otravis-18	{}	{}
Princeton University	Nassau Park Pavilion (Wegmans, Party City, etc.)	2022-07-04 12:00:00	2022-07-04 14:00:00	3	otravis-14	{}	{}
Trenton-Mercer Airport (TTN)	Princeton University	2022-08-20 16:30:00	2022-08-20 16:50:00	1	manyaz-8	{}	{}
Nassau Park Pavilion (Wegmans, Party City, etc.)	Princeton University	2022-07-03 19:00:00	2022-07-03 20:00:00	1	tigertravel-3	{}	{}
John F. Kennedy International Airport (JFK)	Princeton University	2022-08-25 11:00:00	2022-08-25 11:45:00	2	otravis-19	{}	{}
Nassau Park Pavilion (Wegmans, Party City, etc.)	Princeton University	2022-07-04 18:00:00	2022-07-04 19:30:00	2	otravis-15	{}	{}
Newark Liberty International Airport (EWR)	Princeton University	2022-06-04 17:00:00	2022-06-04 18:30:00	1	sydneyp-13	{}	{}
Newark Liberty International Airport (EWR)	Princeton University	2022-06-07 19:00:00	2022-06-07 19:45:00	1	otravis-17	{}	{}
Princeton University	Newark Liberty International Airport (EWR)	2022-06-01 09:15:00	2022-06-01 09:55:00	2	otravis-16	{}	{}
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: ttadmins
--

COPY public.students (netid, firstname, lastname, email, phone, strikes, count) FROM stdin;
nicoles	\N	\N	\N	\N	0	1
nicoles	\N	\N	\N	\N	0	1
cpm6	\N	\N	\N	\N	0	1
otravis					1	20
manyaz					0	9
sydneyp					0	18
tigertravel	\N	\N	\N	\N	0	5
trucn	\N	\N	\N	\N	0	6
\.


--
-- PostgreSQL database dump complete
--

