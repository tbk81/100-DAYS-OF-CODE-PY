import time

# Python decorator function

# def delay_decorator(func):
#     def wrapper_function():
#         time.sleep(2)
        # do something before the function is called
        # func()
        # func()  # run the function twice
        # do something after the function is called
#     return wrapper_function
#
# @delay_decorator
# def say_hello():
#     print("hello")
#
#
# def say_bye():
#     print("bye")
#
#
# def say_greeting():
#     print("how are you?")
#
#
# say_hello()

# alternative method instead of using the @
# decorated_func = delay_decorator(say_greeting)
# decorated_func()


def speed_calc_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}s")
        return result

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()

