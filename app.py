import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    return "Logged in"

@app.route("/cmd")
def cmd():
    cmd = request.args.get("cmd")
    os.system(cmd)
    return "Command executed"

if __name__ == "__main__":
    app.run(debug=True)
