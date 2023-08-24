# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Fall 2022
# Section: 31883R
# Assignment 4
# Description: assignment where we learn the basics of OOP and create a class, inehrited classes, and create its methods, and call those methods

import random

from Arthropod import Arthropod

class Insect(Arthropod):
    insect_count = 0
    def __init__(self, name_param, limbs_count_param, color_param, wings_count):
        """
        :param name_param: name of the Arthropod
        :param limbs_count_param: the number of limbs that the Arthropod has
        :param color_param: the color of the Arthropod
        :param wings_count: the number of wings that the Insect has
        """
        super().__init__(name_param, limbs_count_param, color_param)
        self.wings_count = wings_count
        self.insect_count = self.insect_count + 1

    def __str__(self):
        """
        :return: the string in the proper format
        """
        return "The " + self.color + " " + self.name + " has " + self.limbs + " limbs and " + self.wings_count + " wings."

    def get_wings_count(self):
        """
        :return: the number of wings
        """
        return self.wings_count

    def get_power(self):
        """
        :return: limbs count and wings count as power
        """
        return self.limbs + self.wings_count

    def lose_fight(self):
        """
        inheriting from parent class, then randomizing a number to subtract wings count with
        :return: nothing
        """
        super().lose_fight()
        number_of_wings = random.randint(0, self.wings_count)
        self.wings_count = self.wings_count - number_of_wings
