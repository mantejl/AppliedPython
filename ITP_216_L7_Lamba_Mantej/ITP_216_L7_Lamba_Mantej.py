# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Fall 2022
# Section: 31883R
# Lab 6
# Description: assignment where we learn and practice the basics of Decorators and Functional Programming


# Write a decorator function validator_decorator which will validate the decorated function's input:
# a. All the decorated function's args should be strings.
# b. All the decorated function's kwargs values should be dictionaries with two key:value pairs.
# c. Display a message informing the user of whether or not the decorated function's arguments pass the test

import functools

def validator_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Testing arguments: ")
        all_strs = True
        for arg in args:
            if type(arg) is not str:
                all_strs = False
        good_kwargs = True
        for kwarg in kwargs.items():
            if type(kwarg) is dict and len(kwarg) != 2:
                good_kwargs = False
        if all_strs and good_kwargs:
            print("\t Arguments accepted: all args are Strings, and all kwargs are dictionaries with two k:v pairs.")
        else:
            print('\tArguments rejected: not all kwargs have two key:value pairs.')
        func(*args, **kwargs)

    return wrapper

# Write a function to be decorated called print_all_the_things() which prints out the args all on one line, and
# the kwargs' key:value pairs on separate, indented lines
@validator_decorator
def print_all_things(*args, **kwargs):
    print("Printing arguments: ")
    for arg in args:
        print('\t', arg)

    print("Printing kwargs: ")
    for k in kwargs.items():
        print('\t',end='')
        print(*k, sep= ': ')

    print("This will print all the things:")
    print('\t', " ".join(args))
    for k, v in kwargs.items():
        print('\t',f"{k}: {v}", end=" ")

print_all_things('another', 'lab', 'involving', 'animals', animals = {'cat': True, 'dog': False})