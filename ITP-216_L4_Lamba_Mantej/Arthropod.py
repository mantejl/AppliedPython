# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Fall 2022
# Section: 31883R
# Lab 4
# Description: assignment where we learn the basics of OOP and create a class and its methods, and call those methods

import random

class Arthropod ():

    arthropod_count = 0

    def __init__(self, name_param, limbs_count_param, color_param):
        """
        :param name_param: name of the Arthropod
        :param limbs_count_param: the number of limbs that the Arthropod has
        :param color_param: the color of the Arthropod
        """
        self.name = name_param
        self.limbs = limbs_count_param
        self.color = color_param
        self.arthropod_count = self.arthropod_count + 1

    def get_name(self):
        """
        :return: returning the name of the Arthropod
        """
        return self.name

    def get_color(self):
        """
        :return: returning the color of the Arthropod
        """
        return self.color

    def get_limbs_count(self):
        """
        :return: returning the number of limbs that the Arthropod has
        """
        return self.limbs

    def set_color(self, color:str ):
        """
        :param color: the color of the Arthropod that we want to change to
        :return: nothing
        """
        self.color = color

    def lose_fight(self):
        """
        - randomly generate a number and lose that number of limbs
        - update self.limbs_count instance attribute.
        :return: nothing
        """
        number_of_limbs = random.randint(0,5)
        self.limbs = self.limbs - number_of_limbs

def main():
    """
    main function where we are creating an Arthropod object and calling the various methods to see if they are working they way we want them to
    """
    arth = Arthropod('Bobby', 6, 'blue')
    print(arth.get_name())
    print(arth.get_color())
    print(arth.get_limbs_count())
    arth.set_color('green')
    print(arth.get_color())
    arth.lose_fight()
    print(arth.get_limbs_count())

if __name__ == '__main__':
     main()

