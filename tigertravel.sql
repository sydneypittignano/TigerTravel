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
    rideid integer,
    netid text
);


ALTER TABLE public.riders OWNER TO ttadmins;

--
-- Name: rides; Type: TABLE; Schema: public; Owner: ttadmins
--

CREATE TABLE public.rides (
    rideid integer,
    startdate text,
    enddate text,
    origin text,
    dest text,
    starttime integer,
    endtime integer,
    num integer
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
    strikes integer
);


ALTER TABLE public.students OWNER TO ttadmins;

--
-- Data for Name: riders; Type: TABLE DATA; Schema: public; Owner: ttadmins
--

COPY public.riders (rideid, netid) FROM stdin;
1	sydneyp
\.


--
-- Data for Name: rides; Type: TABLE DATA; Schema: public; Owner: ttadmins
--

COPY public.rides (rideid, startdate, enddate, origin, dest, starttime, endtime, num) FROM stdin;
1	2-6-2022	2-6-2022	Princeton	JFK	100	300	1
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: ttadmins
--

COPY public.students (netid, firstname, lastname, email, phone, strikes) FROM stdin;
sydneyp	Sydney	Pittignano	sydneyp@princeton.edu	(203)-914-7848	0
manyaz	Manya	Zhu	manyaz@princeton.edu	(609)-456-2795	0
otravis	Owen	Travis	otravis@princeton.edu	(847)-691-8322	1
bbob	Billy	Bob	bbob@bob.com	(111)-111-1111	1
jbob	Joey	Bob	jbob@bob.com	(222)-222-2222	2
\.


--
-- PostgreSQL database dump complete
--

