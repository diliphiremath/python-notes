'''
# why we need wrapper funtion?
def print_decorator(func):
    def wrapper():
        print("im here")
        print(func())
        print("im here 2")
    return wrapper

@print_decorator
def add():
    return 2

# throws error without wrapper function as it return None
print(add())
'''

def print_decorator(func):
    def wrapper(*args,**kwargs):
        return func(*args, **kwargs)
    return wrapper

@print_decorator
def add(x,y):
    return x + y

print(add(5,4))