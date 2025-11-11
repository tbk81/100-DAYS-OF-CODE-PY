from flask import Flask

app = Flask(__name__)

print(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def say_bye():
    return "bye"


# @app.route("/username/<name>/1")  # <var> is the syntax for adding a variable to the path
# def greet(name):
#     return f"Hello, {name}"


@app.route("/<name>/<int:num>")  # <var> is the syntax for adding a variable to the path
def greet(name, num):
    return f"Hello {name}, you are {num} years old"


# Used to run a script from the file
if __name__ == "__main__":
    app.run(debug=True)  # debug activates automatic reloader

