#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import io

"""
Matplotlib Line Chart Exercises
"""

# 1. Write a Python program to draw a line with suitable label in the x axis, y axis and a title
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.grid(True)
plt.show()

# 2. Write a Python program to draw a line using given axis values with suitable label in the x axis, y axis and a title
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]  # y = x^2

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'ro-')  # red circles with solid line
plt.xlabel('X-axis values')
plt.ylabel('Y-axis values (x^2)')
plt.title('Line Plot with Given Axis Values')
plt.grid(True)
plt.show()

# 3. Write a Python program to draw a line using given axis values taken from a text file, with suitable label in the x axis, y axis and a title.
# Creating test data in memory since we can't rely on actual file
test_data = """1 2
2 4
3 1"""

# Reading data from string as if it were a file
x = []
y = []
for line in test_data.strip().split('\n'):
    values = line.split()
    x.append(float(values[0]))
    y.append(float(values[1]))

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'g-o', linewidth=2)
plt.xlabel('X Values from File')
plt.ylabel('Y Values from File')
plt.title('Line Plot from Text File Data')
plt.grid(True)
plt.show()

# Note: In a real scenario, you would read from a file like this:
# with open('test.txt', 'r') as file:
#     for line in file:
#         values = line.split()
#         x.append(float(values[0]))
#         y.append(float(values[1]))

# 4. Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016.
# Sample Financial data
data = """Date,Open,High,Low,Close
03-10-16,774.25,776.065002,769.5,772.559998
04-10-16,776.030029,778.710022,772.890015,776.429993
05-10-16,779.309998,782.070007,775.650024,776.469971
06-10-16,779,780.47998,775.539978,776.859985
07-10-16,779.659973,779.659973,770.75,775.080017"""

# Read data from string
df = pd.read_csv(io.StringIO(data))

plt.figure(figsize=(12, 8))
plt.plot(df['Date'], df['Open'], label='Open', marker='o')
plt.plot(df['Date'], df['High'], label='High', marker='^')
plt.plot(df['Date'], df['Low'], label='Low', marker='v')
plt.plot(df['Date'], df['Close'], label='Close', marker='s')

plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Alphabet Inc. Stock Prices (Oct 3-7, 2016)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Write a Python program to plot two or more lines on same plot with suitable legends of each line.
# Create data
x = np.arange(1, 11)
y1 = x * 2
y2 = x * 3
y3 = x * 4

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='Line 1 (y=2x)')
plt.plot(x, y2, label='Line 2 (y=3x)')
plt.plot(x, y3, label='Line 3 (y=4x)')

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Multiple Lines with Legends')
plt.legend()
plt.grid(True)
plt.show()

# 6. Write a Python program to plot two or more lines with legends, different widths and colors.
x = np.arange(1, 11)

plt.figure(figsize=(10, 6))
plt.plot(x, x, 'r-', linewidth=1, label='Line 1 (y=x)')
plt.plot(x, x**2, 'g--', linewidth=2, label='Line 2 (y=x²)')
plt.plot(x, x**3, 'b-.', linewidth=3, label='Line 3 (y=x³)')

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Lines with Different Styles, Widths, and Colors')
plt.legend()
plt.grid(True)
plt.show()

# 7. Write a Python program to plot two or more lines with different styles
x = np.arange(1, 11)

plt.figure(figsize=(10, 6))
plt.plot(x, x, 'r-', label='Solid Line')
plt.plot(x, x+1, 'g--', label='Dashed Line')
plt.plot(x, x+2, 'b-.', label='Dash-Dot Line')
plt.plot(x, x+3, 'y:', label='Dotted Line')

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Lines with Different Styles')
plt.legend()
plt.grid(True)
plt.show()

# 8. Write a Python program to plot two or more lines and set the line markers.
x = np.arange(1, 11)

plt.figure(figsize=(10, 6))
plt.plot(x, x, 'ro-', label='Circles')
plt.plot(x, x+1, 'g^-', label='Triangles')
plt.plot(x, x+2, 'bs-', label='Squares')
plt.plot(x, x+3, 'yd-', label='Diamonds')

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Lines with Different Markers')
plt.legend()
plt.grid(True)
plt.show()

# 9. Write a Python program to display the current axis limits values and set new axis values.
x = np.arange(1, 11)
y = x * 2

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'bo-')

# Get current axis limits
current_xlim = plt.xlim()
current_ylim = plt.ylim()

print(f"Current X-axis limits: {current_xlim}")
print(f"Current Y-axis limits: {current_ylim}")

# Set new axis limits
plt.xlim(0, 12)
plt.ylim(0, 25)

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Plot with Custom Axis Limits')
plt.grid(True)
plt.show()

# 10. Write a Python program to plot quantities which have an x and y position.
# Create random data
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
area = (30 * np.random.rand(50))**2  # 0 to 15 point radii

plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=area, c=colors, alpha=0.5)

plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Scatter Plot with X and Y Positions')
plt.colorbar(label='Color Value')
plt.grid(True)
plt.show()

# 11. Write a Python program to plot several lines with different format styles in one command using arrays.
# Create data
t = np.arange(0.0, 5.0, 0.1)

# Make array of lines with different styles
lines = [
    [t, t, 'r-', 'Line 1'],
    [t, t+0.5, 'g--', 'Line 2'],
    [t, t+1.0, 'b-.', 'Line 3'],
    [t, t+1.5, 'c:', 'Line 4']
]

plt.figure(figsize=(10, 6))

# Plot all lines in one command
for line in lines:
    plt.plot(line[0], line[1], line[2], label=line[3])

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Multiple Lines with Different Styles')
plt.legend()
plt.grid(True)
plt.show()

# 12. Write a Python program to create multiple types of charts
plt.figure(figsize=(15, 10))

# Plot 1: Line chart
plt.subplot(2, 2, 1)
x = np.arange(1, 11)
plt.plot(x, x*2, 'r-')
plt.title('Line Chart')
plt.grid(True)

# Plot 2: Scatter plot
plt.subplot(2, 2, 2)
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.grid(True)

# Plot 3: Bar chart
plt.subplot(2, 2, 3)
x = ['A', 'B', 'C', 'D']
y = [3, 7, 9, 4]
plt.bar(x, y)
plt.title('Bar Chart')
plt.grid(True)

# Plot 4: Pie chart
plt.subplot(2, 2, 4)
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')

plt.tight_layout()
plt.show()

# 13. Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc. between October 3, 2016 to October 7, 2016.
# Sample data
data = """Date,Close
03-10-16,772.559998
04-10-16,776.429993
05-10-16,776.469971
06-10-16,776.859985
07-10-16,775.080017"""

# Read data
df = pd.read_csv(io.StringIO(data))

plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], 'bo-', linewidth=2)

plt.xlabel('Date')
plt.ylabel('Closing Value')
plt.title('Alphabet Inc. Closing Values (Oct 3-7, 2016)')

# Customize grid lines
plt.grid(True, linestyle='-', linewidth=0.5, color='blue')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 14. Write a Python program to display the grid and draw line charts of the closing value with major and minor grid
# Sample data
data = """Date,Close
03-10-16,772.559998
04-10-16,776.429993
05-10-16,776.469971
06-10-16,776.859985
07-10-16,775.080017"""

# Read data
df = pd.read_csv(io.StringIO(data))

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.plot(df['Date'], df['Close'], 'bo-', linewidth=2)

ax.set_xlabel('Date')
ax.set_ylabel('Closing Value')
ax.set_title('Alphabet Inc. Closing Values with Major and Minor Grids')

# Turn on grid with major and minor grids
ax.grid(True, which='major', linestyle='-', linewidth=0.5, color='blue')
ax.grid(True, which='minor', linestyle=':', linewidth=0.5, color='gray')

# Turn on minor ticks
ax.minorticks_on()

# Turn off ticks
ax.tick_params(which='both', bottom=False, top=False, left=False, right=False)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 15. Write a Python program to create multiple plots.
# Create figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Plot 1: Line chart (top-left)
x = np.arange(0, 5, 0.1)
axs[0, 0].plot(x, np.sin(x), 'r-')
axs[0, 0].set_title('Sine Wave')
axs[0, 0].grid(True)

# Plot 2: Line chart (top-right)
axs[0, 1].plot(x, np.cos(x), 'g-')
axs[0, 1].set_title('Cosine Wave')
axs[0, 1].grid(True)

# Plot 3: Line chart (bottom-left)
axs[1, 0].plot(x, np.sin(x) * np.cos(x), 'b-')
axs[1, 0].set_title('Sine * Cosine')
axs[1, 0].grid(True)

# Plot 4: Scatter plot (bottom-right)
axs[1, 1].scatter(np.random.rand(50), np.random.rand(50))
axs[1, 1].set_title('Random Scatter')
axs[1, 1].grid(True)

plt.tight_layout()
plt.show()

"""
Matplotlib Bar Chart Exercises
"""

# 1. Write a Python programming to display a bar chart of the popularity of programming Languages.
# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.figure(figsize=(10, 6))
plt.bar(languages, popularity)

plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 2. Write a Python programming to display a horizontal bar chart of the popularity of programming Languages.
# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.figure(figsize=(10, 6))
plt.barh(languages, popularity)

plt.xlabel('Popularity (%)')
plt.ylabel('Programming Languages')
plt.title('Popularity of Programming Languages')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 3. Write a Python programming to display a bar chart of the popularity of programming Languages. Use uniform color.
# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.figure(figsize=(10, 6))
plt.bar(languages, popularity, color='skyblue')

plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages (Uniform Color)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 4. Write a Python programming to display a bar chart of the popularity of programming Languages. Use different color for each bar.
# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']

plt.figure(figsize=(10, 6))
plt.bar(languages, popularity, color=colors)

plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages (Different Colors)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 5. Write a Python programming to display a bar chart of the popularity of programming Languages. Attach a text label above each bar displaying its popularity.
# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.figure(figsize=(10, 6))
bars = plt.bar(languages, popularity, color='skyblue')

# Attach text labels above each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.3,
             f'{height}%', ha='center', va='bottom')

plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages with Labels')
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(0, max(popularity) + 3)  # Add space for labels
plt.show()

# 6. Write a Python programming to display a bar chart of the popularity of programming Languages. Make blue border to each bar.
# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.figure(figsize=(10, 6))
plt.bar(languages, popularity, color='skyblue', edgecolor='blue', linewidth=1.5)

plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages with Blue Borders')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 7. Write a Python programming to display a bar chart of the popularity of programming Languages. Specify the position of each bar plot.
# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Specify positions (here we're just using default positioning)
positions = np.arange(len(languages))

plt.figure(figsize=(10, 6))
plt.bar(positions, popularity, align='center', alpha=0.7)

plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages with Custom Positions')
plt.xticks(positions, languages)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 8. Write a Python programming to display a bar chart of the popularity of programming Languages. Select the width of each bar and their positions.
# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Specify positions and width
positions = np.arange(len(languages))
width = 0.5  # width of bars

plt.figure(figsize=(12, 6))
plt.bar(positions, popularity, width=width, align='center', alpha=0.7)

plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages with Custom Width')
plt.xticks(positions, languages)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 9. Write a Python programming to display a bar chart of the popularity of programming Languages. Increase bottom margin.
# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.figure(figsize=(10, 6))

# Adjust bottom margin
plt.subplots_adjust(bottom=0.2)

plt.bar(languages, popularity, color='skyblue')

plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages with Increased Bottom Margin')
plt.xticks(rotation=45)  # Rotate labels to demonstrate the increased margin
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 10. Write a Python program to create bar plot of scores by group and gender. Use multiple X values on the same chart for men and women.
# Sample data
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]

# Set position of bars on X-axis
ind = np.arange(len(means_men))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(ind - width/2, means_men, width, label='Men', color='blue', alpha=0.7)
plt.bar(ind + width/2, means_women, width, label='Women', color='pink', alpha=0.7)

plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(ind, ['Group A', 'Group B', 'Group C', 'Group D', 'Group E'])
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 11. Write a Python program to create bar plot from a DataFrame.
# Create sample DataFrame
data = {
    'a': [2, 4, 6, 8, 10],
    'b': [4, 2, 4, 2, 2],
    'c': [8, 3, 7, 4, 4],
    'd': [5, 4, 4, 8, 3],
    'e': [7, 6, 8, 6, 2]
}
df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))

# Plot all columns of the DataFrame
df.plot(kind='bar', figsize=(12, 8))

plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Bar Plot from DataFrame')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 12. Write a Python program to create bar plots with error bars on the same figure.
# Sample data
mean_velocity = [0.2474, 0.1235, 0.1737, 0.1824]
std_velocity = [0.3314, 0.2278, 0.2836, 0.2645]

ind = np.arange(len(mean_velocity))

plt.figure(figsize=(10, 6))
plt.bar(ind, mean_velocity, yerr=std_velocity, capsize=10, error_kw={'elinewidth': 2, 'capthick': 2})

plt.xlabel('Categories')
plt.ylabel('Velocity')
plt.title('Bar Plot with Error Bars')
plt.xticks(ind, ['Category A', 'Category B', 'Category C', 'Category D'])
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 13. Write a Python program to create bar plots with errorbars on the same figure. Attach a text label above each bar displaying men means.
# Sample data
mean_velocity = [0.2474, 0.1235, 0.1737, 0.1824]
std_velocity = [0.3314, 0.2278, 0.2836, 0.2645]

ind = np.arange(len(mean_velocity))

plt.figure(figsize=(10, 6))
bars = plt.bar(ind, mean_velocity, yerr=std_velocity, capsize=10, error_kw={'elinewidth': 2, 'capthick': 2})

# Attach text labels above each bar
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.05,
             f'{int(mean_velocity[i] * 100)}', ha='center', va='bottom')

plt.xlabel('Categories')
plt.ylabel('Velocity')
plt.title('Bar Plot with Error Bars and Labels')
plt.xticks(ind, ['Category A', 'Category B', 'Category C', 'Category D'])
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(0, max(mean_velocity) + max(std_velocity) + 0.1)  # Add space for labels
plt.show()

"""
Matplotlib Pie Chart Exercises
"""

# 1. Write a Python programming to create a pie chart of the popularity of programming Languages.
# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.figure(figsize=(10, 8))
plt.pie(popularity, labels=languages, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle
plt.show()

# 2. Write a Python programming to create a pie chart with a title of the popularity of programming Languages.
# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.figure(figsize=(10, 8))
plt.pie(popularity, labels=languages, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Popularity of Programming Languages', fontsize=14)

plt.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle
plt.show()

# 3. Write a Python programming to create a pie chart of gold medal achievements of five most successful countries in 2016 Summer Olympics.
# Sample data (from the provided CSV data)
countries = ['United States', 'Great Britain', 'China', 'Russia', 'Germany']
gold_medals = [46, 27, 26, 19, 17]

plt.figure(figsize=(10, 8))
plt.pie(gold_medals, labels=countries, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Gold Medal Achievements in 2016 Summer Olympics', fontsize=14)

plt.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle
plt.show()

"""
Matplotlib Scatter Plot Exercises
"""

# 1. Write a Python program to draw a scatter graph taking a random distribution in X and Y and plotted against each other.
# Generate random data
x = np.random.randn(100)
y = np.random.randn(100)

plt.figure(figsize=(10, 6))
plt.scatter(x, y)

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Random Scatter Plot')
plt.grid(True)
plt.show()

# 2. Write a Python program to draw a scatter plot with empty circles taking a random distribution in X and Y and plotted against each other.
x = np.random.randn(100)
y = np.random.randn(100)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, facecolors='none', edgecolors='blue')

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Scatter Plot with Empty Circles')
plt.grid(True)
plt.show()

# 3. Write a Python program to draw a scatter plot using random distributions to generate balls of different sizes.
x = np.random.randn(100)
y = np.random.randn(100)
sizes = np.random.rand(100) * 100  # Random point sizes between 0 and 100

plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=sizes, alpha=0.5)

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Scatter Plot with Random Ball Sizes')
plt.grid(True)
plt.show()

# 4. Write a Python program to draw a scatter plot comparing two subject marks of Mathematics and Science. Use marks of 10 students.
# Test Data
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.figure(figsize=(10, 6))
plt.scatter(math_marks, science_marks, color='blue', alpha=0.8)

plt.xlabel('Math Marks')
plt.ylabel('Science Marks')
plt.title('Scatter Plot of Math vs Science Marks')
plt.grid(True)

# Add a reference line
plt.plot(marks_range, marks_range, 'r--')

plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()

# 5. Write a Python program to draw a scatter plot for three different groups comparing weights and heights.
# Sample data
group1_heights = [165, 170, 175, 180, 160]
group1_weights = [60, 65, 70, 75, 55]

group2_heights = [168, 172, 178, 185, 162]
group2_weights = [70, 75, 80, 85, 65]

group3_heights = [175, 180, 185, 190, 170]
group3_weights = [75, 80, 90, 95, 70]

plt.figure(figsize=(10, 6))
plt.scatter(group1_heights, group1_weights, color='red', alpha=0.7, label='Group 1')
plt.scatter(group2_heights, group2_weights, color='blue', alpha=0.7, label='Group 2')
plt.scatter(group3_heights, group3_weights, color='green', alpha=0.7, label='Group 3')

plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Scatter Plot of Height vs Weight for Different Groups')
plt.legend()
plt.grid(True)
plt.show()
