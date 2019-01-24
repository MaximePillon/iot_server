import sys
import psycopg2

conn = None
try:
    conn = psycopg2.connect("dbname = 'iotproject' user = 'iot_user' host = 'localhost' password = 'iot_password'")
except psycopg2.DatabaseError as ex:
    print("I am unable to connect the database: {0}".format(ex))
    sys.exit(1)

curs = conn.cursor()
curs.execute("""
        INSERT INTO station (station_id, city, country, postal_code, xlocation, ylocation)
        VALUES (%s, %s, %s, %s, %s, %s);
        """, (1, 'Zagreb', 'Croatia', '10000', '45.814', '15.945'))

# Maybe we will have to replace true with 1 don't know yet
# duplicate this line has many time has needed for each sensor
curs.execute("""
        INSERT INTO sensor (sensor_id, voltage, is_activated, data_type, name, station_id)
        VALUES (%s, %s, %s, %s, %s, %s);
        """, (1, '12', 'true', 'mm', 'Precipitation', '1'))
