from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h2>CRLF Injection Lab - Fixed Version</h2>

    <form action="/demo" method="GET">
        Enter value:
        <input type="text" name="value">
        <button type="submit">Submit</button>
    </form>
    """


@app.route("/demo")
def demo():
    value = request.args.get("value", "")

    # MITIGATION:
    # Remove CR and LF characters so user input
    # cannot create additional lines.
    value = value.replace("\r", "").replace("\n", "")

    simulated_response = "X-Custom-Value: " + value

    return "<pre>" + simulated_response + "</pre>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
