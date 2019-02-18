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
    curs.execute("INSERT INTO sensor (voltage, is_activated, data_type, name, station_id) VALUES (%s, %s, %s, %s, %s);", ('12', 'true', 'V', 'Voltage', '1'))
except psycopg2.Error as e:
    print("exec create sensor 1 error")
print(curs.query)
