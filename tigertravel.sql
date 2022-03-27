--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

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
    rideid text
);


ALTER TABLE public.riders OWNER TO ttadmins;

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


ALTER TABLE public.rides OWNER TO ttadmins;

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


ALTER TABLE public.students OWNER TO ttadmins;

--
-- Data for Name: riders; Type: TABLE DATA; Schema: public; Owner: ttadmins
--

COPY public.riders (netid, rideid) FROM stdin;
cpm6	cpm6-1
jbob	jbob-1
bbob	bbob-1
manyaz	manyaz-1
sydneyp	sydneyp-1
otravis	otravis-1
\.


--
-- Data for Name: rides; Type: TABLE DATA; Schema: public; Owner: ttadmins
--

COPY public.rides (origin, dest, starttime, endtime, num, rideid, reqrec, reqsent) FROM stdin;
LGA	Princeton	2021-05-22 13:00:00	2021-05-22 15:00:00	1	manyaz-1	{}	{}
Princeton	JFK	2020-06-24 12:00:00	2020-06-24 14:00:00	1	sydneyp-1	{}	{}
Forbes	Dinky	2022-03-23 10:00:00	2022-03-23 10:01:00	1	cpm6-1	{}	{}
Evanston	Princeton	2022-06-07 14:00:00	2022-06-07 15:00:00	1	jbob-1	{}	{}
Princeton	Pennsylvania	2022-05-22 15:00:00	2022-05-22 18:00:00	1	bbob-1	{}	{}
Princeton	JFK	2020-06-24 10:00:00	2020-06-24 13:00:00	1	otravis-1	{}	{}
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: ttadmins
--

COPY public.students (netid, firstname, lastname, email, phone, strikes, count) FROM stdin;
sydneyp	Sydney	Pittignano	sydneyp@princeton.edu	(203)-914-7848	0	1
cpm6					0	1
manyaz					0	1
bbob					0	1
jbob					0	1
otravis					0	1
\.


--
-- PostgreSQL database dump complete
--

