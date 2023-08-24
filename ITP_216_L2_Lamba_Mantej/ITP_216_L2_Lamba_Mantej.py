# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Fall 2022
# Section: 31883R
# Lab 2 (there is no lab 1)
# Description: convert the user input to different data types and then iterate through to print out each individual value

# user input
input_str = input('Please enter an input to be converted:')

# type cast the string input to a list
my_list = list(input_str)
# type cast the string input to a tuple
my_tuple = tuple(input_str)
# type cast the string input to a set to remove duplicates
my_set = set(input_str)

# printing out the individual values in the string
print('string: ', end = "")
for char in input_str:
    print(char + ", ", end = "")
print()

# printing out the individual values in the list
print('list: ', end = "")
for char in my_list:
    print(char + ", ", end = "")
print()

# printing out the individual values in the tuple
print('tuple: ', end ="")
for char in my_tuple:
    print(char + ", ", end = "")
print()

# printing out the individual values in the set
print('set: ', end ="")
for char in my_set:
    print(char + ", ", end ="")
print()

print("dictionary: ")
my_dict = {}
# for each letter in my input string
for c in input_str:
    # if current letter not already in dict key set
    if c not in my_dict:
        # first time seeing this letter
        my_dict[c] = 1
    else: # I've seen this letter before
        # increment the freq/occurrence count by 1
        my_dict[c] = my_dict[c] + 1

for k, v in my_dict.items():
    # key: value
    print(k+ ":", v)