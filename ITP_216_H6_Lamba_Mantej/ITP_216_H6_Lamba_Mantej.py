# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Fall 2022
# Section: 31883R
# Assignment 6
# Description: assignment where we work with pythonic comprehensions, generators and iterators

def file_reader(file_name: str):
    """
    :param file_name: file name that we want to read
    :return: the header and the rest of the file in a list
    """
    # opening file and reading the header
    f_in = open(file_name, 'r')
    header = f_in.readline().split()
    # reading the rest of the data
    data = [line.strip() for line in f_in]
    # closing the file
    f_in.close()
    # returning
    return header, data

def read_score(file_name: str):
    """
    :param file_name: name of file we want to get the scores from
    :return: the list of scores from the file
    """
    # opening file to read and skipping header
    f_in = open(file_name,'r')
    _ = f_in.readline()
    # reading the data
    lines=f_in.readlines()
    data = []
    # going through each line, and stripping/splitting it to make it into a list
    for x in lines:
        # checking for empty strings to avoid indexing them and getting an error
        if (x.strip() != ''):
            x.strip()
            value = x.split()
            # adding just the scores to data list
            data.append(value[1].replace(',',''))
    # closing and returning data
    f_in.close()
    return data

def calculate_mean(average: list[int])->float:
    """
    :param average: collection of integers in a list format
    :return: the mean score as a float
    """
    # getting the sum
    sum_values = 0
    for n in average:
        sum_values = sum_values + int(n)
    # dividing it to get the mean and returning
    mean = float(sum_values/len(average))
    return mean

def find_movies_above_score(movies: list[str], score: float):
    """
    :param movies: a collection of movies as a list
    :param score: the score as a float
    :return: a collection of all movies in the format of year, score, title with a score above the given score
    """
    # looping through the movies list passed as an argument using comprehension and if the score is greater than what is given
    # adding a list of the movie criteria to the list created
    movieList = [[int(m[0]), int(m[1]), m[2]] for m in movies if m[1] > int(score)]
    return movieList

def main():
    """
    :return: none
    """
    # printing out intro message and calculating the mean
    print("I love Robert Deniro!")
    scores = read_score("deniro.csv")
    mean = calculate_mean(scores)
    print("The average Rotten Tomates score for his movies is " + str(mean) + ".")
    # creating a list of movies in the year, score, title format
    movies = []
    file = open("deniro.csv",'r')
    _ = file.readline()
    for line in file:
        if (line.strip() != ''):
            line.strip()
            value = line.split(",")
            movies.append([int(value[0].replace(',','')), int(value[1].replace(',','')), value[2]])
    # finding the movies that are above the specific score and printing them out
    above_average = find_movies_above_score(movies,mean)
    print("Of the 87 movies, " + str(len(above_average)) + " are above average.")
    print("Here they are:")
    # printing out the headers and above average movies
    header, data = file_reader("deniro.csv")
    print("     " + "     ".join(header).replace(",","").replace('"',""))
    for val in above_average:
        print("      " + str(val[0])+ "    " + str(val[1]) + "   " + val[2].strip())


# main call
if __name__ == '__main__':
    main()
