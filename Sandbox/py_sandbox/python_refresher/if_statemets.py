should_continue = True
if should_continue == True:
    print("Hello")

if should_continue:
    print("Hello")

known_people = ["John", "Anna", "Mark"]
person = raw_input("Enter the person you know:")

if person in known_people:
    print("You know {}".format(person))
else:   # if not in also can be used but not practical
    print("You do not know {}".format(person))

# Exercise


def who_do_you_know():
    # Ask the user for the list of ppl you know
    user_input = raw_input("Give the list of ppl you know:")
    # Split the string into the list
    list_of_ppl = user_input.split(",")
    # Return the list

    people_without_spaces = [people.strip() for people in list_of_ppl]
    #for people in list_of_ppl:
        #people_without_spaces.append(people.strip())    # remove white spaces

    return people_without_spaces


def ask_user():
    # Ask user for a name
    user_input = raw_input("Enter a name of someone you know:")
    # See if the name is in the list of ppl they know
    if user_input in who_do_you_know():
        # Print out that they know the person
        print("You know {}".format(user_input))
    else:
        print("You don't know {}".format(user_input))

ask_user()


