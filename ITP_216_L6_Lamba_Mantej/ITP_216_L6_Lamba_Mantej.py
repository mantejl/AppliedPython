# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Fall 2022
# Section: 31883R
# Lab 6
# Description: assignment where we learn the basics of list comprehension

new_list = []

# writing out the comprehension with a normal for loop
for i in range(1, 1000):
    if i % 7 == 0:
        new_list.append(i)

print(new_list)
print(len(new_list))

# writing it in an actual list comprehension format
new_list2 = [i for i in range(1,1000) if i % 7 == 0]

print(new_list2)
print(len(new_list2))

# creating new dictionaries
birdos = {}
my_dict = {}

# doing the normal for loop iteration
names = ['Great potoo', 'Smew', 'Tundra bean goose', 'Southern pied, babbler']
genus_and_species = ['Nyctibius grandis', 'Mergellus albellus', 'Anser ,serrirostris', 'Turdoides bicolor']

for name, gen_spec in zip(names, genus_and_species):
    my_dict[name] = gen_spec
print(my_dict)

# writing the actual dictionary comprehension code
birdos = {name: gen_spec for name,gen_spec in zip(names, genus_and_species)}
print(birdos)

# generator function
def square_gen_old(n):
    for i in range(n):
        yield i, i*i

# generator expression
square_gen = ((i, i*i) for i in range(10))

# testing generator expression code
for number, square in square_gen:
    print(number, 'squared:', square)