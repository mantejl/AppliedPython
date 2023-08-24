# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Fall 2022
# Section: 31883R
# Assignment 4
# Description: assignment where we learn the basics of OOP and create a class, inehrited classes, and create its methods, and call those methods

from Arthropod import Arthropod

class Arachnid(Arthropod):
    arachnid_count = 0

    def __init__(self,name_param, limbs_count_param, color_param, venomous):
        """
        :param venomous: whether or not the arachnid is venomous
        :param name_param: name of the Arthropod
        :param limbs_count_param: the number of limbs that the Arthropod has
        :param color_param: the color of the Arthropod
        """
        super().__init__(self, name_param, limbs_count_param, color_param)
        self.venomous = venomous
        self.arachnid_count = self.arachnid_count + 1

    def __str__(self):
        """
        :return:
        """
        venom = ""
        if(self.get_venomous() == False):
            venom = "non-"
        return "The " + self.color + " " + venom + "venomous " + self.name + " has " + self.limbs + " limbs."

    def get_venomous(self):
        """
        :return: whether the arachnid is venomous or not
        """
        return self.venomous

    def get_power(self):
        """
        :return: returning the number of limbs the arachnid has based on whether it is venomous
        """
        if(self.get_venomous()):
            return self.limbs * 2
        else:
            return self.limbs