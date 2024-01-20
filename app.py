from mysql.connector import Error
import mysql.connector
from flask import Flask
from markupsafe import escape
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    hostname="ze7.h.filess.io",
    database="hunterhub_raineleven",
    port="3307",
    username="hunterhub_raineleven",
    password="d90350b1dd4b20e532cc3a001a5c79fd6a25133e",
    cursorclass=pymysql.cursors.DictCursor
)
cursor = conn.cursor()
