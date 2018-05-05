def methodception(another):
    return another()

def add_two_numbers():
    return 1 + 1

# print(methodception(add_two_numbers))

# Lambda function
# lambda function can only be one line function
# here we define lambda function with one parameter x and body x * 5
# next we pass 3 as an argument to the function
print((lambda x: x * 5)(3))
# lambda function in other words
def f(x):
    return x * 5

print(f(3))
# they are both identical

# print(methodception(lambda: 1 + 1))

my_list = [13, 4, 54, 23]
# my_list.remove(13)
# list comprehantion methofd to filter list
print(x for x in my_list if x != 13)

# we are going to filter my_list using the lambda function
print(list(filter(lambda x: x != 13, my_list)))

# we could also use a normal function to filter the numbers
def not_thirteen(x):
    return x != 13

print(list(filter(not_thirteen, my_list)))
##########################################



