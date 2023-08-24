# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Spring 2023
# Section: 31883R
# Lab 13
# Description: lab where we practice using matplotlib and pandas to visualize data

import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)
df = pd.read_csv("penguins.csv")
df = df.dropna()

fig, ax = plt.subplots(1, 1)

species_list = df["species"].unique()
df_grouped = df.groupby("species")
color_list = ["blue", "#FF00FF", "green"]
marker_list = ["*", "D", "^"]

def get_freq_dict(ser_param):
    '''
    Get the frequency of occurency of a value in a collection
    :param ser_param: the collection to iterate over
    :return: a concordance dictionary, key is value, value is frequency of occurence
    '''
    freq_dict = {}
    for item in ser_param:
        if item not in freq_dict:
            freq_dict[item] = 1
        else:
            freq_dict[item] += 1
    return freq_dict

for index, species in enumerate(species_list):
    df_group = df_grouped.get_group(species)
    ax.bar(get_freq_dict(df_group["flipper_length_mm"]).keys(),
               get_freq_dict(df_group["flipper_length_mm"]).values(),
               label=species)
ax.legend()
ax.set_title("Penguin Flipper lengths")
ax.set_xlabel("Flipper length (mm)")
ax.set_ylabel("Frequency")

plt.show()
