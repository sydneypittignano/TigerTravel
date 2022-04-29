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
    strikes integer,
    count integer
);

--
-- PostgreSQL database dump complete
--

