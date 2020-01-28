
def decorator(func):
    def wrapper_function():
        print('****')
        func()
        print('****')
    return wrapper_function


def hello():
    print('heloooooooooo')


decorator(hello)()