from flask import Flask, request
import sqlite3

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("users.db")
    return conn


@app.route("/")
def home():
    return """
    <h2>SQL Injection Lab - Fixed Version</h2>

    <form action="/login" method="GET">
        Username:
        <input type="text" name="username">

        Password:
        <input type="text" name="password">

        <button type="submit">Login</button>
    </form>
    """


@app.route("/login")
def login():
    username = request.args.get("username", "")
    password = request.args.get("password", "")

    conn = get_db()
    cursor = conn.cursor()

    query = """
        SELECT * FROM users
        WHERE username = ? AND password = ?
    """

    print("SQL Query:", query)
    print("Parameters:", username, password)

    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        return "Login successful!"
    else:
        return "Invalid username or password."


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002)
