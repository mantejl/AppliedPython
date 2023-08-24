# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Fall 2022
# Section: 31883R
# HW 5
# Description: assignment where we practice the basics of OOP, create a classes and its methods, call those methods, and use inheritance

# imports
from athlete.Athlete import Athlete
from athlete.Boxer import Boxer
from athlete.Swimmer import Swimmer

def main():
    # testing out the different functions
    athlete = Athlete("John Mackie", "1944/05/22", "USA", ['Silver(2012)','Bronze (2008)', 'Bronze (2008)'])
    print(athlete.get_name())
    print(athlete.get_dob())
    print(athlete.get_origin())
    print(athlete.get_medals())
    athlete.add_medal('Gold(2016)')
    print(athlete.get_medals())


    boxer = Boxer("Mary Berry", "1935/03/24", "UK", ['Gold(2012)','Gold (2016)'], "Light Flyweight")
    print(boxer)
    print(boxer.weight_class)
    print(boxer.record)
    boxer.set_weight_class("Heavyweight")
    print(boxer.weight_class)
    boxer.win_fight()
    boxer.win_fight()
    boxer.win_fight()
    boxer.win_fight()
    boxer.lose_fight()
    boxer.win_fight()
    boxer.win_fight()
    boxer.lose_fight()
    boxer.lose_fight()
    boxer.lose_fight()
    boxer.win_fight()
    print(boxer.record)
    boxer.lose_fight()
    boxer.lose_fight()
    print(boxer.lose_fight())
    boxer.lose_fight()
    print(boxer.lose_fight())
    print(boxer.lose_fight())
    print(boxer.record)



    swimmer = Swimmer("Dave Thomas", "1932/07/02", "USA", ['Silver (1992)', 'Gold (1996)'], ['freestyle', 'breaststroke'])
    # print(swimmer)
    print(swimmer.get_strokes())
    swimmer.add_strokes('freestyle')
    swimmer.add_strokes('backstroke')
    print(swimmer.get_strokes())

if __name__ == '__main__':
    main()