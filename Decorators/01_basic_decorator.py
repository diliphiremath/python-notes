# creating a Decorator
def print_decorator(func):
    def wrapper():
        print("Function is about to exectute")
        func()
        print("Function has finished executing")
    return wrapper

# applying the decorator
@print_decorator
def greet():
    print("Hello there")


# invoking the decorated function
greet()
