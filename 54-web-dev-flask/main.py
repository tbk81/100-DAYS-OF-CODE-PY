import time

# Python decorator function

def delay_decorator(func):
    def wrapper_function():
        time.sleep(2)
        # do something before the function is called
        func()
        func()  # run the function twice
        # do something after the function is called
    return wrapper_function

@delay_decorator
def say_hello():
    print("hello")


def say_bye():
    print("bye")


def say_greeting():
    print("how are you?")


say_hello()

# alternative method instead of using the @
decorated_func = delay_decorator(say_greeting)
decorated_func()

