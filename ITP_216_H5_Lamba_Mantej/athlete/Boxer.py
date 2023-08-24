# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Fall 2022
# Section: 31883R
# HW 5
# Description: assignment where we practice the basics of OOP, create a classes and its methods, call those methods, and use inheritance

from ITP_216_H5_Lamba_Mantej.athlete.Athlete import Athlete

class Boxer(Athlete):
    # boxer count
    boxer_count = 0

    def __init__(self, name_param, dob_param, origin_param, medals_param, weight_class: str):
        """
        :param name_param: name of boxer
        :param dob_param: dob of boxeer
        :param origin_param: origin of boxer
        :param medals_param: medals that the boxer has
        :param weight_class: the weight class of the boxer
        """
        self.name = name_param
        self.dob = dob_param
        self.origin = origin_param
        self.medals = medals_param
        self.weight_class = weight_class
        self.record = [0,0]
        self.boxer_count = self.boxer_count + 1

    def __str__(self):
        """
        :return: the edited string for boxer
        """
        return self.name + " is a " + self.weight_class + " boxer from " + self.origin + " born on " + self.dob + ". " + self.name + " has a " + str(self.record[0]) + "-" + str(self.record[1]) + " record, and has won " + str(len(self.medals)) + " medals: " + str(self.medals) + "."

    def get_weight_class(self):
        """

        :return: the weight class of the boxer
        """
        return self.weight_class

    def get_record(self):
        """
        :return: the record of the boxer
        """
        return self.record

    def set_weight_class(self, weight_class_param):
        # setting the weight class of the boxer to what we want
        self.weight_class = weight_class_param

    def win_fight(self):
        # adds one to the wins of the boxer's record
        self.record[0] = self.record[0] + 1

    def lose_fight(self):
        #  adds one to the losses of the boxer's record, then checks to see if the boxer needs to retire (after 10 losses)
        self.record[1] = self.record[1] + 1
        if (self.record[1] == 10):
            return "This boxer has retired"
        else:
            return "This boxer has " + str((10-self.record[1])) + " fights left before retirement."
