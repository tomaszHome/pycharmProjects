# the below @ are called decorators
# is a function that gets called before another function
# @staticmethod
# @classmethod

import functools

# creating a decorator
def my_decorator(func):
    # in order to create a decorator you need to call @functools decorator
    # that will wrap around the function that gets passed as a parameter
    @functools.wraps(func)
    # define the function that runs in the decorator
    def function_that_runs_func():
        # you can define what will be executed before the func
        print("In the decorator")
        # executing func() is optional
        func()
        # and after the function
        print("After the decorator")
    return function_that_runs_func

# we apply my_decorator to my_function
@my_decorator
def my_function():
    print("I am the function")

# my_function()


######### Complex decorators


def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        # *args and *kwargs have to be used if the function passed to the
        # decorator takes in arguments
        # it doesn't matter how many arguments or key word it takes in
        def function_that_runs_func(*args, **kwargs):
            print("I'm the decorator")
            # we can use the number to determine what happens inside the function
            if number == 56:
                print("We are not running the function!")
            else:
                func(*args, **kwargs)
            print("After the decorator")
        return function_that_runs_func
    return my_decorator

# decorators which take in arguments can be used for example
# to pass in users credentials if we are creating a website with login
# or it could be used to insert elements to a data base. We can check if the
# element is passing required criteria before storing it in the data base
@decorator_with_arguments(5)
def my_function_two(x, y, z):
    print((x + y) / z)

my_function_two(2, 2, 2)


