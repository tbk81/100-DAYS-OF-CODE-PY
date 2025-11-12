from flask import Flask

app = Flask(__name__)

# print(__name__)


def make_bold(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper


def make_italic(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper


def make_underline(func):
    def wrapper():
        return '<u>' + func() + '</u>'
    return wrapper


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@make_bold
@make_italic
@make_underline
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


## Advanced Python Decorator Functions

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
#
# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")
#
# new_user = User("angela")
# new_user.is_logged_in = True


# Create the logging_decorator() function
# def logging_decorator(func):
#     def wrapper(*args):
#         print(f"You called {func.__name__}{args}")
#         result = func(*args)
#         print(f"it returned {result}")
#         return result
#
#     return wrapper
#
#
# @logging_decorator
# def a_function(*args):
#     return sum(args)
#
#
# a_function(1, 2, 3)
