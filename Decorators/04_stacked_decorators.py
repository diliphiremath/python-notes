def uppercase_decorator(func):
    def wrapper():
        print("upper")
        return func().upper()
    return wrapper

def lowercase_decorator(func):
    def wrapper():
        print("lower")
        return func().lower()
    return wrapper

@uppercase_decorator
@lowercase_decorator
def print_something():
    return("Hello, world")

print(print_something())