# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Fall 2022
# Section: 31883R
# HW 5
# Description: assignment where we practice the basics of OOP, create a classes and its methods, call those methods, and use inheritance

class Athlete:
    athlete_count = 0
    def __init__(self, name_param, dob_param, origin_param, medals_param: list):
        """
        :param name_param: name of the athlete
        :param dob_param: dob of the athlete
        :param origin_param: origin of the athlete
        :param medals_param: the medals that the athlete has
        """
        self.name = name_param
        self.dob = dob_param
        self.origin = origin_param
        self.medals = medals_param
        self.athlete_count = self.athlete_count + 1

    def get_name(self):
        """
        :return: returning the name of the athlete
        """
        return self.name

    def get_dob(self):
        """
        :return: return dob of athlete
        """
        return self.dob

    def get_origin(self):
        """
        :return: the origin of the athlete
        """
        return self.origin

    def get_medals(self):
        """
        :return: the medals the athlete has
        """
        return self.medals

    def add_medal(self, medal_param):
        """
        :param medal_param: the new medal that needs to be added
        :return: none
        """
        self.medals.append(medal_param)


