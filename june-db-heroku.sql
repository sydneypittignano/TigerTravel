--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

DROP TABLE IF EXISTS riders;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS rides;

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
sydneyp	sydneyp-2	2022-06-16 01:00:00	2022-06-17 01:00:00
otravis	otravis-6	2022-06-25 19:15:00	2022-06-25 22:15:00
beid	beid-2	2022-06-16 11:51:00	2022-06-16 12:51:00
otravis	beid-2	2022-06-16 11:17:00	2022-06-16 12:17:00
sl55	otravis-6	2022-06-25 19:15:00	2022-06-25 19:45:00
otravis	otravis-9	2022-06-21 16:37:00	2022-06-21 17:37:00
otravis	otravis-10	2022-06-26 10:00:00	2022-06-26 11:30:00
\.


--
-- Data for Name: rides; Type: TABLE DATA; Schema: public; Owner: ttadmins
--

COPY public.rides (origin, dest, starttime, endtime, num, rideid, reqrec, reqsent) FROM stdin;
LaGuardia Airport (LGA)	John F. Kennedy International Airport (JFK)	2022-06-25 19:15:00	2022-06-25 19:45:00	2	otravis-6	{}	{}
Nassau Park Pavilion (Wegmans, Party City, etc.)	Philadelphia International Airport (PHL)	2022-06-21 16:37:00	2022-06-21 17:37:00	1	otravis-9	{}	{}
Princeton University	Nassau Park Pavilion (Wegmans, Party City, etc.)	2022-06-16 01:00:00	2022-06-17 01:00:00	1	sydneyp-2	{}	{}
Princeton University	Nassau Park Pavilion (Wegmans, Party City, etc.)	2022-06-16 11:51:00	2022-06-16 12:17:00	2	beid-2	{}	{}
Princeton University	LaGuardia Airport (LGA)	2022-06-26 10:00:00	2022-06-26 11:30:00	1	otravis-10	{}	{}
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: ttadmins
--

COPY public.students (netid, firstname, lastname, email, phone, strikes, count) FROM stdin;
sydneyp					0	2
sl55					0	2
beid					0	2
otravis					0	10
\.


--
-- PostgreSQL database dump complete
--

