from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h2>Log Injection Lab - Fixed Version</h2>

    <form action="/login" method="GET">
        Username:
        <input type="text" name="username">
        <button type="submit">Login</button>
    </form>
    """


@app.route("/login")
def login():
    username = request.args.get("username", "")

    # Mitigation:
    # Remove carriage-return and line-feed characters
    # so user input cannot create additional log lines.
    username = username.replace("\r", "").replace("\n", "")

    with open("app.log", "a") as log:
        log.write("Login attempt by: " + username + "\n")

    return "Login attempt recorded safely."


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
