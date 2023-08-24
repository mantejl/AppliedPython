# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Spring 2023
# Section: 31883R
# Final Project
# Description: creating a web app using Flask, pandas, scikit-learn, and matplotlib which manipulates and visualizes a Big Data datasetd

from flask import Flask, render_template, request, redirect, url_for
import os
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# creating Flask instance
app = Flask(__name__)

# returns a rendered template for the home.html page
@app.route('/')
def index():
    return render_template('home.html')

# checks if request method is POST, if it is then we create a plot with the method redirect to prediction page
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        year = int(request.form['year'])
        plot_cybersecurity_salaries(year)
        return redirect(url_for('prediction'))
    return render_template('home.html')

# returns a rendered template for the prediction.html page.
@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

# gets the years to fast forward and then calls a function to show an updated plot
@app.route('/fast_forward', methods=['POST'])
def fast_forward():
    years = int(request.form['years'])
    predict_cybersecurity_salaries(years)
    return redirect(url_for('prediction'))

# creating a plot
def plot_cybersecurity_salaries(year):
    # load the cybersecurity salaries data into a Pandas DataFrame
    df = pd.read_csv('cyber_salaries.csv')

    # filter the data to include only the specified year
    df = df[df['work_year'] == year]

    # calculate the average salary for each location
    avg_salaries = df.groupby('company_location')['salary_in_usd'].mean()

    # create a bar plot of the average salaries by location
    fig, ax = plt.subplots()
    ax.bar(avg_salaries.index, avg_salaries.values)
    ax.set_xlabel('Location')
    ax.set_ylabel('Average Salary in USD')
    ax.set_title(f'Average Cybersecurity Salaries in {year}')

    # rotate x-axis labels to avoid overlapping
    ax.tick_params(axis='x', rotation=90)

    # adjust layout to make room for rotated labels
    fig.tight_layout()

    # add a legend to the plot
    ax.legend(['Average Salary'])

    # save the plot to a file
    plt.savefig('static/plot.png', bbox_inches='tight')

# predicting the salaries for the upcoming years
# since there are only 3 years to go off of in the data set, the predictions aren't exactly precise
def predict_cybersecurity_salaries(years):
    # Load the dataset
    df = pd.read_csv('cyber_salaries.csv')

    # Group salaries by location and calculate the average for each group
    location_salaries = df.groupby('company_location')['salary_in_usd'].mean().to_frame()

    # Create a new column for the projected salaries
    location_salaries['projected_salary'] = 0

    # Fit a linear regression model to each location
    for location in location_salaries.index:
        loc_df = df.loc[df['company_location'] == location]
        X = loc_df[['work_year']]
        y = loc_df['salary_in_usd']
        model = LinearRegression()
        model.fit(X, y)

        # Predict the salary for the next `years` years
        X_pred = pd.DataFrame({'work_year': range(2022, 2022 + years)})
        y_pred = model.predict(X_pred)

        # Update the projected_salary column with the predicted values
        location_salaries.loc[location, 'projected_salary'] = y_pred[-1]

    # Create a bar plot of the projected salaries
    fig, ax = plt.subplots()
    ax.bar(x=location_salaries.index, height=location_salaries['projected_salary'], width=0.5)
    ax.set_title('Projected Cybersecurity Salaries by Location')
    ax.set_xlabel('Location')
    ax.set_ylabel('Salary (USD)')
    ax.set_xticks(range(len(location_salaries)))
    ax.set_xticklabels(location_salaries.index, rotation=45, ha='right')
    ax.tick_params(axis='x', which='major', pad=10)
    ax.legend(['Projected Salary'])
    plt.tight_layout()
    fig.savefig('static/plot.png')

# running the web app
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)