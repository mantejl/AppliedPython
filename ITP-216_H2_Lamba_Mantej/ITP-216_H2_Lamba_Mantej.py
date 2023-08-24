# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Fall 2022
# Section: 31883R
# Assignment 2
# Description: assignment where we work with dictionaries, take user input and modify values in various data sets

def main():

    # given data collections
    cats_names = ('Cassandra', 'Sir Whiskington', 'Truck')
    dogs_names = {'Barkey McBarkface', 'Leeloo Dallas', 'Taro'}
    parrots_names = ['Squawk', 'Squawk 2: the Squawkquel', 'Larry']

    # names and animals data collections
    names = ['peter', 'paul', 'mary']
    animals = ('cat', 'cat', 'hamster')

    # converting all data collections to lists
    cats = list(cats_names)
    dogs = list(dogs_names)
    parrots = list(parrots_names)

    # creating dictionary that maps animal to names
    animalDict = {
        "cat": cats,
        "dog": dogs,
        "parrot": parrots,
    }

    # variable to keep track of number of pets
    pets = len(cats) + len(dogs) + len(parrots)

    # looping through the animals list and adding the names/new animals to the dictionary to keep track of all of them
    for i in range(0,len(animals)):
        # checking if a list for a certain animal exists
        animalList = animalDict.get(animals[i])
        # if it doesn't then we create a new one and increment pet count
        if animalList is None:
            animalList = [names[i].capitalize()]
            animalDict[animals[i]] = animalList
            pets = pets + 1
        # if it does exist, then we add it to the existing list and increment pet count
        else:
            animalList.append(names[i].capitalize())
            pets = pets + 1

    # starting program
    print("Hi Mantej!")

    # while loop to keep looping through the menu after every turn
    while(True):
        # showing menu
        print("Please choose from the following options: \n"
              "    1. See all your pet's names. \n"
              "    2. Add a pet. \n"
              "    3. Exit \n")

        # looping through to see if the input is valid
        while(True):
            # asking for option
            option = input("What would you like to do? (1,2,3): ")
            # validating if it's a digit
            if (option.isdigit() == False):
                print("That's not a number.")
                continue
            # checking if it's out of range
            elif(int(option) > 3 or int(option) < 1):
                print("Number is out of range. ")
                continue
            # if it's valid, then break
            else:
                break

        # if the option is 1
        if (int(option) == 1):
            # printing number of pets
            print("You have", pets, "pets.")
            # looping through dictionary
            for a in animalDict:
                # printing the key
                print(a, ":", end=' ')
                # counter to print commas
                i = 0
                # printing out the list values
                for n in animalDict[a]:
                    # only printing out comma in front of the second value, so we don't have a misprint
                    if (i == 0):
                        print(n, end='')
                        i = i + 1
                    else:
                        print(", " + n, end='')
                # printing for new line
                print()
        # if the option is 2
        elif (int(option) == 2):
            # asking for kind of animal
            animalKind = input("What kind of animal is this? : ")
            # asking for the name
            animalName = input("What is the name of the " + animalKind + "? : ")
            # checking to see if there is key for the animalKind
            newAnimalList = animalDict.get(animalKind)
            # if it doesn't then we create a new one and increment pet count
            if newAnimalList is None:
                newAnimalList = [animalName]
                animalDict[animalKind] = newAnimalList
                pets = pets + 1
            # if it does exist, then we add it to the existing list and increment pet count
            else:
                newAnimalList.append(animalName)
                pets = pets + 1
            # confirmation statement
            print("Great! " + animalName + " the " + animalKind + " is now added to your pets. ")
        # if the option is 3
        elif (int(option) == 3):
            # goodbye printing and break
            print("Goodbye!")
            break


if __name__ == '__main__':
    main()