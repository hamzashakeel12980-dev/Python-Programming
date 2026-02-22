"""
burger - function
extra cheese - extra functionality

main function > functionality > add
without changing the main function, we can add extra functionality using decorator
"""

def my_decorator(func):
    def wrapper():
        print("something is happening before the function is called.")
        func()
        print("something is happening after the function is called.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")

say_hello()