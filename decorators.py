import functools
# A decorator function takes another function as argument, wraps its behaviour inside
# an inner function, and returns the wrapped function.
# def start_end_decorator(func):
    
#     def wrapper():
#         print('Start')
#         func()
#         print('End')
#     return wrapper

# def print_name():
#     print('Alex')
    
# print_name()

# print()

# # Now wrap the function by passing it as argument to the decorator function
# # and asign it to itself -> Our function has extended behaviour!
# print_name = start_end_decorator(print_name)
# print_name()

# print('**************************************************************************')
# def start_end_decorator_2(func):
    
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')
#         return result
#     return wrapper

# @start_end_decorator_2
# def add_5(x):
#     return x + 5

# result = add_5(10)
# print(result)


# print('*'*75)

# # printing greetings x no of times using decorators

# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat



# @repeat(num_times=3)
# def greet(name):
#     print(f'Hello {name}')

# res = greet('XYZ')

# print(greet.__name__)
# # help(add_5)

# # a decorator function that prints debug information about the wrapped function
# def debug(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         print(f'args_repr - {args_repr}')
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         print(f'kwargs_repr - {kwargs_repr}')
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper

# def start_end_decorator_4(func):
    
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')
#         return result
#     return wrapper

# @debug
# @start_end_decorator_4
# def say_hello(name):
#     greeting = f'Hello {name}'
#     print(greeting)
#     return greeting

# # now `debug` is executed first and calls `@start_end_decorator_4`, which then calls `say_hello`
# say_hello(name='Alex')

class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls +=1
        print(f'This is executed {self.num_calls} times') 


@CountCalls
def sayhello():
    print('Hello')


sayhello()
sayhello()

