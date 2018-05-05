my_variable = "hello"

# print(my_variable[0])

for character in my_variable:
    print (character)

my_list = [1, 2, 3, 4]

for number in my_list:
    print (number ** 2)

user_wants_number = True
while user_wants_number == True:
    print(10)

    user_input = raw_input("Should we print again? (y/n)")  # raw_input works with Python2.7
    if user_input == 'n':
        user_wants_number = False
