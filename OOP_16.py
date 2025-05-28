# Decorator Function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello! How are you?")

# Calling the decorated function
say_hello()