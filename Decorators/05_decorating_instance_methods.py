# decorting instance methods without arguments
def method_decorator(func):
    def wrapper(self):
        print("Entering decorator function")
        func(self)
        print("Ending decorator function")
    return wrapper

def method_decorator_with_args(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper



class Greet:
    @method_decorator
    def print_greet(self):
        print("Hello friend")

    @method_decorator_with_args
    def add_numbers(self, a, b):
        print(a+b)
    

greetings = Greet()
greetings.print_greet()
greetings.add_numbers(2,7)
