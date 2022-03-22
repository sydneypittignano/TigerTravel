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
    origin text,
    dest text,
    starttime timestamp without time zone,
    endtime timestamp without time zone,
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
2	otravis
3	manyaz
4	bbob
5	jbob
\.


--
-- Data for Name: rides; Type: TABLE DATA; Schema: public; Owner: ttadmins
--

COPY public.rides (rideid, origin, dest, starttime, endtime, num) FROM stdin;
1	Princeton	JFK	2020-06-22 19:00:00	2020-06-22 21:00:00	1
2	Princeton	JFK	2020-06-24 12:00:00	2020-06-24 14:00:00	1
3	LGA	Princeton	2021-05-22 13:00:00	2021-05-22 15:00:00	1
4	Evanston	Princeton	2022-06-07 14:00:00	2022-06-07 15:00:00	1
5	Princeton	Pennsylvania	2022-05-22 15:00:00	2022-05-22 18:00:00	1
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: ttadmins
--

COPY public.students (netid, firstname, lastname, email, phone, strikes) FROM stdin;
sydneyp	Sydney	Pittignano	sydneyp@princeton.edu	(203)-914-7848	0
\.


--
-- PostgreSQL database dump complete
--

