def my_method(arg1, arg2):
    return arg1 + arg2

my_method(5, 6)

def my_list_addition(list_arg):
    return sum(list_arg)

###

def what_are_args_and_kwargs(*args, **kwargs):
    print(args)     # all arguments are printed out in form of the list ()
    print(kwargs)   # all key word arguments are print out in form of the set {}

what_are_args_and_kwargs(12, 13, 14, name='Jose', location='UK')

