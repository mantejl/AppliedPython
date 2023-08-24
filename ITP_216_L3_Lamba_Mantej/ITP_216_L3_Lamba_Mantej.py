# file_read_header()
# a. Description: Retrieves the first line from a text file.
# b. Parameters: 1
# i. File name (string)
# c. Returns: 1
# i. The first line of the file (String)

def file_read_header(file_name: str )-> str:
    """
    Reads in a file  and returns the first line/header
    :param file_name: input csv file name
    :return: the first line or header
    """
    f_in = open(file_name, 'r')
    header_line = f_in.readline()
    f_in.close()
    return header_line

# 2. file_read_data()
# a. Description: Retrieves all data from a text file except the first line.
# b. Parameters: 1
# i. File name (String)
# c. Returns: 1
# i. All the data from the file except for the first line (list)
def file_read_data(file_name:str) -> list[str]:
    """
    Gets the data portion of the file as a list of strings
    :param file_name: input file
    :return: the file as a list of string w/o the header and first line
    """
    f_in = open(file_name, 'r')
    _ = f_in.readline() # skip the header
    # lines = f_in.readlines()
    # or
    data = []
    for line in f_in:
        data.append(line.strip())
    f_in.close() # remember to close anything you open
    return data


# 3. main()
# a. Description: Primary entrypoint to your codebase.
# b. Parameters: 0
# c. Returns: 0
# d. Loads the contents of the file into two variables by calling their respective functions. Then prints the header
# row and iterates through (item by item) and prints the rest of the data.
def main():
    """
    Main calls read header and read data and loops through both printing them out
    :return: none
    """
    input_file_name = "oscar_age_female.csv"
    header_portion = file_read_header(input_file_name)
    data_portion = file_read_data(input_file_name)
    print("Header:")
    print("\t")
    print(header_portion)
    # print(data_portion)
    print("Data:")

    for line in data_portion:
        print("\t"+line)

if __name__ == '__main__':
    main()
