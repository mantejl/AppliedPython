# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Fall 2022
# Section: 31883R
# HW 5
# Description: assignment where we practice the basics of OOP, create a classes and its methods, call those methods, and use inheritance

from ITP_216_H5_Lamba_Mantej.athlete.Athlete import  Athlete

class Swimmer(Athlete):
    swimmer_count = 0

    def __init__(self, name_param, dob_param, origin_param, medals_param, strokes: list):
        """
        :param name_param: name of swimmer
        :param dob_param: dob of swimmer
        :param origin_param: origin of swimmer
        :param medals_param: medals of the swimmer
        :param strokes: the strokes that the swimmer knows
        """
        self.name = name_param
        self.dob = dob_param
        self.origin = origin_param
        self.medals = medals_param
        self.strokes = strokes
        self.swimmer_count = self.swimmer_count + 1

    def __str__(self):
        """
        :return: the proper string formatting for a swimmer object
        """
        return self.name + " is a swimmer from " + self.origin + " born on " + self.dob + ". " + self.name + " knows " + str(self.strokes) + ", and has won " + str(len(self.medals)) + " medals: " + str(self.medals) + "."

    def get_strokes(self):
        # returning the strokes of the swimmer
        return self.strokes

    def add_strokes(self, stroke_param):
        #  adds a new stroke to the swimmer's repertoire. Checks to make sure the stroke is not already in the list
        if stroke_param not in self.strokes:
            self.strokes.append(stroke_param)