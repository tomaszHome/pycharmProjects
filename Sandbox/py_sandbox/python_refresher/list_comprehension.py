my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)]   # range 5 is a list of 5 elements

multiply_list = [x * 3 for x in range(5)]

print (an_equal_list)
print (multiply_list)

even_list = [n for n in range(10) if n % 2 == 0 and n > 0]
print (even_list)

people_you_know = ["Ralf", "anna", " John"]
normalised_people = [person.strip().lower() for person in people_you_know]
print (normalised_people)
