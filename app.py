from mysql.connector import Error
import mysql.connector
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


hostname = "ze7.h.filess.io"
database = "hunterhub_raineleven"
port = "3307"
username = "hunterhub_raineleven"
password = "d90350b1dd4b20e532cc3a001a5c79fd6a25133e"

connection = mysql.connector.connect(
    host=hostname, database=database, user=username, password=password, port=port)


@app.route("/")
def hello():
    if connection.is_connected():
        cursor = connection.cursor
        cursor.execute("show tables")


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'
