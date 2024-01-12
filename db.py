import mysql.connector
from mysql.connector import Error

hostname = "ze7.h.filess.io"
database = "hunterhub_raineleven"
port = "3307"
username = "hunterhub_raineleven"
password = "d90350b1dd4b20e532cc3a001a5c79fd6a25133e"

try:
    connection = mysql.connector.connect(
        host=hostname, database=database, user=username, password=password, port=port)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
