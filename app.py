from mysql.connector import Error
import mysql.connector
import json
from flask import Flask, request, jsonify
from markupsafe import escape
import pymysql

app = Flask(__name__)


def db_conn():
    conn = None
    try:
        conn = pymysql.connect(
            host="eyn.h.filess.io",
            database="MMOPlayerDatabase_billrough",
            port=3307,
            user="MMOPlayerDatabase_billrough",
            password="b8687aac2fc979066ede1e01259edcc8db5a0b83",
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.Error as e:
        print(e)
    return conn


@app.route("/player", methods=['GET'])
def play():
    conn = db_conn()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * from Player")
        player = [
            dict(
                id=row['Id'],
                name=row['Name'],
                level=row['Level'],
                clas=row['Class'],
                race=row["Race"],
                gender=row["Gender"]
            )
            for row in cursor.fetchall()
        ]
        if player is not None:
            return jsonify(player)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
