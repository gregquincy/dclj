-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.8.2
-- PostgreSQL version: 9.6
-- Project Site: pgmodeler.com.br
-- Model Author: ---


-- Database creation must be done outside an multicommand file.
-- These commands were put in this file only for convenience.
-- -- object: swift | type: DATABASE --
-- -- DROP DATABASE IF EXISTS swift;
-- CREATE DATABASE swift
-- 	ENCODING = 'UTF8'
-- 	LC_COLLATE = 'en_US.UTF8'
-- 	LC_CTYPE = 'en_US.UTF8'
-- 	TABLESPACE = pg_default
-- 	OWNER = swift
-- ;
-- -- ddl-end --
-- 

-- object: public.activity__field | type: TABLE --
DROP TABLE IF EXISTS public.activity__field CASCADE;
CREATE TABLE public.activity__field(
	id serial NOT NULL,
	id_activity integer,
	id_field integer,
	CONSTRAINT activity__field_pk PRIMARY KEY (id)

);
-- ddl-end --
-- ALTER TABLE public.activity__field OWNER TO swift;
-- ddl-end --

-- object: public.report__activity__field | type: TABLE --
DROP TABLE IF EXISTS public.report__activity__field CASCADE;
CREATE TABLE public.report__activity__field(
	id_report integer NOT NULL,
	id_activity__field integer NOT NULL,
	payload character varying,
	CONSTRAINT report__activity__field_pk PRIMARY KEY (id_report,id_activity__field)

);
-- ddl-end --
-- ALTER TABLE public.report__activity__field OWNER TO swift;
-- ddl-end --

-- object: public."user" | type: TABLE --
DROP TABLE IF EXISTS public."user" CASCADE;
CREATE TABLE public."user"(
	id serial NOT NULL,
	login character varying,
	password character varying,
	display_name character varying,
	settings json,
	CONSTRAINT user_primary_key PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public."user" OWNER TO swift;
-- ddl-end --

-- object: public.activity | type: TABLE --
DROP TABLE IF EXISTS public.activity CASCADE;
CREATE TABLE public.activity(
	id serial,
	CONSTRAINT activity_primary_key PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.activity OWNER TO swift;
-- ddl-end --

-- object: public.report | type: TABLE --
DROP TABLE IF EXISTS public.report CASCADE;
CREATE TABLE public.report(
	id serial,
	user_id integer,
	activity_id integer,
	media_id integer,
	CONSTRAINT report_primary_key PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.report OWNER TO swift;
-- ddl-end --

-- object: public.media | type: TABLE --
DROP TABLE IF EXISTS public.media CASCADE;
CREATE TABLE public.media(
	id serial,
	media_type_id integer,
	name character varying,
	location character varying,
	CONSTRAINT media_primary_key PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.media OWNER TO swift;
-- ddl-end --

-- object: public.media_type | type: TABLE --
DROP TABLE IF EXISTS public.media_type CASCADE;
CREATE TABLE public.media_type(
	id serial,
	label character varying,
	CONSTRAINT media_type_primary_key PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.media_type OWNER TO swift;
-- ddl-end --

-- object: public.field | type: TABLE --
DROP TABLE IF EXISTS public.field CASCADE;
CREATE TABLE public.field(
	id serial,
	label character varying,
	CONSTRAINT field_primary_key PRIMARY KEY (id)

);
-- ddl-end --
-- ALTER TABLE public.field OWNER TO swift;
-- ddl-end --

-- object: activity_fk | type: CONSTRAINT --
-- ALTER TABLE public.activity__field DROP CONSTRAINT IF EXISTS activity_fk CASCADE;
ALTER TABLE public.activity__field ADD CONSTRAINT activity_fk FOREIGN KEY (id_activity)
REFERENCES public.activity (id) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: field_fk | type: CONSTRAINT --
-- ALTER TABLE public.activity__field DROP CONSTRAINT IF EXISTS field_fk CASCADE;
ALTER TABLE public.activity__field ADD CONSTRAINT field_fk FOREIGN KEY (id_field)
REFERENCES public.field (id) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: activity__field_fk | type: CONSTRAINT --
-- ALTER TABLE public.report__activity__field DROP CONSTRAINT IF EXISTS activity__field_fk CASCADE;
ALTER TABLE public.report__activity__field ADD CONSTRAINT activity__field_fk FOREIGN KEY (id_activity__field)
REFERENCES public.activity__field (id) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: report_user_fk | type: CONSTRAINT --
-- ALTER TABLE public.report DROP CONSTRAINT IF EXISTS report_user_fk CASCADE;
ALTER TABLE public.report ADD CONSTRAINT report_user_fk FOREIGN KEY (user_id)
REFERENCES public."user" (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: report_activity_id_fk | type: CONSTRAINT --
-- ALTER TABLE public.report DROP CONSTRAINT IF EXISTS report_activity_id_fk CASCADE;
ALTER TABLE public.report ADD CONSTRAINT report_activity_id_fk FOREIGN KEY (activity_id)
REFERENCES public.activity (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: report_media_id_fk | type: CONSTRAINT --
-- ALTER TABLE public.report DROP CONSTRAINT IF EXISTS report_media_id_fk CASCADE;
ALTER TABLE public.report ADD CONSTRAINT report_media_id_fk FOREIGN KEY (media_id)
REFERENCES public.media (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: media_media_type_id_fk | type: CONSTRAINT --
-- ALTER TABLE public.media DROP CONSTRAINT IF EXISTS media_media_type_id_fk CASCADE;
ALTER TABLE public.media ADD CONSTRAINT media_media_type_id_fk FOREIGN KEY (media_type_id)
REFERENCES public.media_type (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --


