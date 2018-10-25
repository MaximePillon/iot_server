CREATE TABLE IF NOT EXISTS station (
	id serial,
	city text,
	country text,
	postal_code text,
	xlocation text,
	ylocation text,
	PRIMARY KEY( id )
);

CREATE TABLE IF NOT EXISTS sensor (
	sensor_id serial,
	station_id INTEGER REFERENCES station(id),
	voltage numeric(9,4),
	is_activated BOOLEAN NOT NULL,
	data_type text,
	name text,
	PRIMARY KEY( sensor_id )
);

CREATE TABLE IF NOT EXISTS data (
	data_id serial,
	sensor_id INTEGER REFERENCES sensor(sensor_id),
	value numeric(9,4),
	created_at timestamp,
	PRIMARY KEY( data_id )
);

CREATE TABLE IF NOT EXISTS "user" (
	id serial,
	firstname text,
	lastname text,
	email text,
	password text,
	status text,
	PRIMARY KEY( id )
);