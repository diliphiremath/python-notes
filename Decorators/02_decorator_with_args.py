# Decorators with arguments
# Decorator  factory

def repeat_decorator(times):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator

@repeat_decorator(times=3)
def print_message():
    print("This message will be repeated")

print_message()