from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def mainPage():
    return  render_template("index.html")


if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=9002, debug=True )