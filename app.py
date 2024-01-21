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


@app.route("/player", methods=['GET', 'POST'])
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

    if request.method == "POST":
        add_name = request.form['Name']
        add_level = request.form['Level']
        add_race = request.form['Race']
        add_gender = request.form['Gender']
        add_class = request.form['Class']
        cursor.execute(
            "insert into Player (Name, Level, Class, Race, Gender) values (%s, %s, %s, %s, %s)", (add_name, add_level, add_class, add_race, add_gender))
        conn.commit()
        return ("player succesfully created")


@app.route("/player/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def oneplay(id):
    conn = db_conn()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("select * from Player where id = %s", (id))
        player = cursor.fetchone()

        if player is not None:
            return jsonify(player)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
