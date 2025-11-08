from flask import Flask

app = Flask(__name__)

print(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# Used to run a script from the file
if __main__ == "__main__":
    app.run()
