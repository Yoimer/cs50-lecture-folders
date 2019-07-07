-- Adminer 4.6.3-dev PostgreSQL dump

\connect "d42oslhd6lgnv4";

DROP TABLE IF EXISTS "checkin";
DROP SEQUENCE IF EXISTS checkin_id_seq;
CREATE SEQUENCE checkin_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."checkin" (
    "id" integer DEFAULT nextval('checkin_id_seq') NOT NULL,
    "zipcode" character varying(10) NOT NULL,
    "username" character varying(50) NOT NULL,
    "comment" character varying(2000) NOT NULL,
    CONSTRAINT "checkin_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "locations";
DROP SEQUENCE IF EXISTS locations_id_seq;
CREATE SEQUENCE locations_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."locations" (
    "id" integer DEFAULT nextval('locations_id_seq') NOT NULL,
    "zipcode" character varying(10) NOT NULL,
    "city" character varying(50) NOT NULL,
    "state" character varying(50) NOT NULL,
    "lat" numeric,
    "long" numeric,
    "population" integer,
    CONSTRAINT "locations_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "login";
DROP SEQUENCE IF EXISTS login_id_seq;
CREATE SEQUENCE login_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."login" (
    "id" integer DEFAULT nextval('login_id_seq') NOT NULL,
    "username" character varying(20) NOT NULL,
    "password" character varying(20) NOT NULL,
    CONSTRAINT "login_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


-- 2018-07-12 12:59:48.053641+00
