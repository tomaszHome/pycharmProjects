import random

i_out = []

for x in range(10):
    i_out.append(random.randint(70, 150))
    print(i_out)

i_out = sorted(i_out)
# print(i_out)
print(float(float((i_out[4]) + (i_out[5]))/2))
print(sum(i_out)/10)
print("\n")

value = 6
value2 = 2

value2 = 3 if value == 5 else 4
print(value2)



