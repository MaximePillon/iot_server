import sys
import psycopg2
import time
import datetime


conn = None
try:
    conn = psycopg2.connect("dbname = 'iotproject' user = 'iot_user' host = 'localhost' password = 'iot_password'")
except psycopg2.DatabaseError as ex:
    print("I am unable to connect the database: {0}".format(ex))
    sys.exit(1)

curs = conn.cursor()

# need to put name send by the board with the corresponding id created with create_station.py
sensors = {
    'Precipitation': 1,
    'Humidity': 2,
    'Temperature': 3
}


# do what it need to recieve data as tuple
def recieve_data():
    return {}


def data_pushing(infos):
    date = datetime.datetime.now()
    for key, val in infos.items():
        curs.execute("""
            INSERT INTO data (value, created_at, sensor_id)
            VALUES (%(info)s, %(date)s, %(id)s);
            """, {'info': val, 'date': date, 'id': sensors[key]})


if __name__ == '__main__':
    while 1:
        data = recieve_data()
        if data:
            data_pushing(data)
            data = []
        time.sleep(1)
