from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def mainPage():
    return "Hello App"


if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=9002, debug=True )