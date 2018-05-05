grade_one = 77
grade_two = 80
grade_three = 90

print((grade_one + grade_two + grade_three) / 3)

###############################################################################################

list_grades = [70, 80, 90, 95, 100]         # we can append items to the list
tuple_grades = (70, 80, 90, 95, 100)        # we can't append items in tuple (immutable)
set_grades = {77, 80, 90, 95, 100, 100}     # unique and unordered, removes repeatable numbers

print("List avg: " + str(sum(list_grades) / len(list_grades)))  # calculating average using sum and len

list_grades.append(108)  # add an item at the end
print(list_grades)

print(set_grades)   # print set
set_grades.add(60)  # add and item to set. It does not add same item multiple times.
print(set_grades)

tuple_grades = tuple_grades + (100, )   # calculating a new tuple
print(tuple_grades)

print(list_grades[0])   # printing element 0 from the list

list_grades[0] = 60     # changing the value at element 0. Can't be done in tuple and set!
print (list_grades)

#############################################################################################

set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

print(set_one.intersection(set_two))    # intersection produces new set with common items between set_one and set_two
print (set_one.union(set_two))          # combines both sets, do duplicates
print (set_one.difference(set_two))     # produces a new set with numbers that are different between two sets




