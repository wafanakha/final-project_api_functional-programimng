from mysql.connector import Error
import mysql.connector
from flask import Flask
from markupsafe import escape
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    hostname="eyn.h.filess.io",
    database="MMOPlayerDatabase_billrough",
    port="3307",
    username="MMOPlayerDatabase_billrough",
    password="b8687aac2fc979066ede1e01259edcc8db5a0b83",
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()
