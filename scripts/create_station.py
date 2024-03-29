import sys
import psycopg2

conn = None
try:
    conn = psycopg2.connect("dbname = 'iotproject' user = 'iot_user' host = 'localhost' password = 'iot_password'")
except psycopg2.DatabaseError as ex:
    print("I am unable to connect the database: {0}".format(ex))
    sys.exit(1)

curs = conn.cursor()

try:
    curs.execute("""
            INSERT INTO station (station_id, city, country, postal_code, xlocation, ylocation)
            VALUES (%s, %s, %s, %s, %s, %s);
            """, (1, 'Zagreb', 'Croatia', '10000', '45.814', '15.945'))
except psycopg2.Error as e:
    print("exec create station error")

try:
    curs.execute("""
        INSERT INTO sensor (voltage, is_activated, data_type, name, station_id)
        VALUES (%s, %s, %s, %s, %s);
        """, ('12', 'true', 'm/s', 'Wind', '1'))
except psycopg2.Error as e:
    print("exec create sensor 1 error")

try:
    curs.execute("""
        INSERT INTO sensor (voltage, is_activated, data_type, name, station_id)
        VALUES (%s, %s, %s, %s, %s);
        """, ('12', 'true', 'mm/h', 'Precipitation', '1'))
except psycopg2.Error as e:
print("exec create sensor 2 error")

try:
    curs.execute("""
        INSERT INTO sensor (voltage, is_activated, data_type, name, station_id)
        VALUES (%s, %s, %s, %s, %s);
        """, ('12', 'true', '%', 'Humidity', '1'))
except psycopg2.Error as e:
    print("exec create sensor 3 error")

try:
    curs.execute("""
        INSERT INTO sensor (voltage, is_activated, data_type, name, station_id)
        VALUES (%s, %s, %s, %s, %s);
        """, ('12', 'true', '°C', 'Temperature', '1'))
except psycopg2.Error as e:
    print("exec create sensor 4 error")
