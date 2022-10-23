import time
from functools import wraps


def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("--код перед--")
        res = func(*args, **kwargs)
        print("--код после--")
        return res

    return wrapper


@func_decorator
def some_func(br):
    print(f"Вызов some {br}_func")
    return "STOP"


# some_func = func_decorator(some_func)
some_func("HHHH")
print(some_func("HHHH"))
