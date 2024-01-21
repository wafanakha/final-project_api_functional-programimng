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


@app.route("/character", methods=['GET', 'POST'])
def play():
    conn = db_conn()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * from Player")
        player = [
            dict(
                Id=row['Id'],
                Name=row['Name'],
                Level=row['Level'],
                Class=row['Class'],
                Race=row["Race"],
                Gender=row["Gender"]
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
        return ("New character succesfully created!")


@app.route("/character/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def oneplay(id):
    conn = db_conn()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("select * from Player where id = %s", (id))
        player = cursor.fetchone()

        if player is not None:
            return jsonify(player)

    if request.method == 'PUT':
        name = request.form['Name']
        level = request.form['Level']
        race = request.form['Race']
        gender = request.form['Gender']
        clas = request.form['Class']
        cursor.execute(
            "update Player set Name = %s, Level = %s, Race = %s, Gender = %s, class = %s where Id = %s", (name, level, race, gender, clas, id))
        conn.commit()
        return ("Character data with id = {} updated!".format(id))

    if request.method == 'DELETE':
        cursor.execute("delete from Player where Id = %s", (id))
        conn.commit()
        return ("Character data with id = {} Deleted!".format(id))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
