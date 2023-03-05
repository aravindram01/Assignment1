# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:36:07 2023

@author: aravind
"""
import pandas as pd
import matplotlib.pyplot as plt

# Read in the CSV file and convert to a DataFrame
df = pd.read_csv('GHG4.csv', index_col=0)
print(df)

# Select the emissions data for two different years
year1 = '2000'
year2 = '2019'
data1 = df[year1]
data2 = df[year2]

# Select the emissions data for two different countries
country1 = 'China'
country2 = 'India'
data3 = df.loc[country1][2:]
data4 = df.loc[country2][2:]

#Line Plot - Function Starts from here
def plot_emissions_by_country(data_file: str) -> None:
    """
    Plots greenhouse gas emissions by BRICS countries  using a line plot.

    data_file (str): Name or path of the CSV file containing the data

    Displays the line plot
    """
# Create a figure with one subplot
fig, ax = plt.subplots(figsize=(15, 5))

# Loop through each country and create a line plot for their emissions data
for country in df.index:
    data = df.loc[country][2:]
    ax.plot(data.index, data, label=country)
    
# Add labels and a title to the plot
ax.set_xlabel('Year')
ax.set_ylabel('Emissions (MtCO2e)')
ax.set_title('Annual GHG Emissions by BRICS Country')

# Add a legend to the plot
ax.legend()
#Line Plot - Function Ends here

#Pie Chart - Function Starts from here
def pie_chart(data, year):
    """
    Display a pie chart of greenhouse gas emissions by BRICS countries 
    for a given year.

    data (pd.DataFrame): A pandas DataFrame containing  emissions data.
    year (int): The year for which the pie chart will be displayed.

    Example: pie_chart(df, 2018)
    """
    
# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))

# Create a pie chart for 2009 data
labels1 = data1.index
values1 = data1.values
ax1.pie(values1, labels=labels1, autopct='%1.1f%%')
ax1.set_title(f'Total GHG Emissions ({year1})')

# Create a pie chart for 2019 data
labels2 = data2.index
values2 = data2.values
ax2.pie(values2, labels=labels2, autopct='%1.1f%%')
ax2.set_title(f'Total GHG Emissions ({year2})')

# Add a title to the figure
fig.suptitle('Comparison of Greenhouse Gas Emissions by BRICS Countries')
#Pie Chart - Function Ends here

#Bar Plot - Function Starts from here
def plot_bar(year, country1, country2):
    """
    Plots a bar chart comparing the greenhouse gas emissions of 
    two BRICS countries for a specific year.
    
    - year (int): the year to plot emissions for
    - country1 (str): the name of the first country to compare emissions 
    - country2 (str): the name of the second country to compare emissions 
    
    plot_bar(2015, 'China', 'India')
    """
# Create a figure with one subplot
fig, ax = plt.subplots(figsize=(10, 5))

# Create a bar plot for the first country
ax.bar(data3.index, data3, alpha=0.5, label=country1)

# Create a bar plot for the second country
ax.bar(data4.index, data4, alpha=0.5, label=country2)

# Add labels and a title 
ax.set_xlabel('Year')
ax.set_ylabel('Emissions (MtCO2e)')
ax.set_title('Annual GHG Emissions by Country')

# Add a legend 
ax.legend()
#Bar Plot - Function Ends here

# Display the plot
plt.show()