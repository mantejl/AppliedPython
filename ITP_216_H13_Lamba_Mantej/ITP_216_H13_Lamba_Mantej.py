# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Spring 2023
# Section: 31883R
# Assignment 13
# Description: assignment where we practice using matplotlib and pandas to visualize data

import pandas as pd
import matplotlib.pyplot as plt


def main():
    # reading in the dataset
    df = pd.read_csv("weather.csv")

    # removing rows of data where the observed temp is null
    df = df[df["TOBS"].notnull()]

    # making a column for year: allows us to easily get the last 10 years
    df["YEAR"] = df["DATE"].str[0:4]
    # list of years till 2023
    years_list = list(df["YEAR"].unique())

    # making a column for month: allows us to group by month
    df["MONTH_DAY"] = df["DATE"].str[-5:]
    df = df[df['MONTH_DAY'] != '02-29']  # drop leap years
    # list of month days (01-01, 01-02, 01-03)
    month_days_list = list(df["MONTH_DAY"].unique())

    df.sort_values(inplace=True, by='MONTH_DAY')
    # sorted data frame by date (01-01 to 12-31) of all the years
    # print(df[['DATE', 'YEAR', 'MONTH_DAY', 'TOBS']])

    # list of months to label the x-axis of both graphs
    month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # creating the static
    fig,ax = plt.subplots(2,1)

    # list of colors and grouping by year
    color_list = ["blue", "red", "black", "green", "pink", "purple", "yellow", "orange", "#A23F2A", "#26AAB7", "#9973EA"]
    df_grouped = df.groupby("YEAR")

    # looping through years and plot each individual year
    i = 0
    for year in years_list:
        df_group = df_grouped.get_group(year)
        ax[0].plot(df_group["MONTH_DAY"],
                   df_group["TOBS"],
                   color = color_list[i],
                   label = year)
        i = i+ 1

    # setting titles, labels and ticks
    ax[0].set_title("Most recent 10 years")
    ax[0].set_xlabel("Month")
    ax[0].set_ylabel("temp (F)")
    interval_ticks = []
    for i in range(12):
        interval_ticks.append(i*365/12)
    ax[0].set_xticks(interval_ticks)
    ax[0].set_xticklabels(month_list)
    ax[0].legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax[0].grid(True)

    # creating separate dfs to separate 2019 from the historical years
    historical_df = df[df["YEAR"] != "2019"]
    current_df = df[df["YEAR"] == "2019"]

    # keeping just the first row of any unique date for the year 2019
    current_df = current_df.drop_duplicates(subset=["MONTH_DAY"], keep = "first")

    # making an empty list to store average temps for historical data
    # converting current year df to a list using typecasting to store observed temps for 2019
    # grouping historical years by 'MONTH_DAY' / contains dates NOT in 2019
    average_temps = []
    current_year_df = current_df["TOBS"].tolist()
    current_year_df.append(62.0)
    df2_group = historical_df.groupby("MONTH_DAY")

    # looping through each day of the year and adding average to a list
    for day in month_days_list:
        month_day_group = df2_group.get_group(day)
        avg_temp = month_day_group['TOBS'].mean()
        average_temps.append(avg_temp)


    # plotting the two bar static
    ax[1].bar(month_days_list, average_temps, color = "blue", label = 'historical average')
    ax[1].bar(month_days_list, current_year_df, color = "green", label = '2019')

    # setting titles, labels and ticks
    ax[1].set_title("Comparing current year and historical averages")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("temp (F)")
    interval_ticks = []
    for i in range(12):
        interval_ticks.append(i * 365 / 12)
    ax[1].set_xticks(interval_ticks)
    ax[1].set_xticklabels(month_list)
    ax[1].legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax[1].grid(True)

    # figure specifications
    fig.suptitle("Yearly climatological data for zip 94536 from 2013 to 2023")
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
