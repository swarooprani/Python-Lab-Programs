'''Create the following plots by using Matplotlib.

 Line plot
 Histogram
 Bar Chart
 Scatter plot
 Pie charts'''


'''Line Chart'''
'''Problem: We have monthly sales data. Create a line chart to show sales trends over 6 months.'''

import matplotlib.pyplot as plt

# Define data (Months and Sales)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [200, 250, 300, 280, 350, 400]

# Create a line chart
plt.plot(months, sales, marker='o', linestyle='-', color='blue', label='Sales')

# Add labels and title
plt.xlabel('Months')  # X-axis represents months
plt.ylabel('Sales')  # Y-axis represents sales numbers
plt.title('Monthly Sales Trend')

# Show the chart
plt.show()

'''Histogram'''

'''Problem: We have test scores of 50 students (out of 100). Create a histogram to see how scores are distributed.'''


import numpy as np

# Step 1: Create a dataset (Test scores of 50 students)
test_scores = np.random.randint(0, 101, 50)  # Random scores between 0 and 100

# Step 2: Create a histogram
plt.hist(test_scores, bins=10, color='blue', edgecolor='black')

# Step 3: Add labels and title
plt.xlabel('Score Range')  # X-axis: Score ranges (bins)
plt.ylabel('Number of Students')  # Y-axis: Count of students in each range
plt.title('Distribution of Student Test Scores')

# Step 4: Show the plot
plt.show()

''' Bar chart'''
'''Problem: We have sales data of different products. Create a bar chart to compare sales.'''
# Step 1: Define categories (Products) and their values (Sales)
products = ['Laptop', 'Tablet', 'Smartphone', 'Headphones']
sales = [150, 200, 350, 180]

# Step 2: Create a bar chart
plt.bar(products, sales, color=['red', 'blue', 'green', 'purple'])

# Step 3: Add labels and title
plt.xlabel('Products')  # X-axis represents product categories
plt.ylabel('Sales')  # Y-axis represents sales numbers
plt.title('Sales by Product')

# Step 4: Show the chart
plt.show()

'''Scatter plot'''
'''Problem: Study Time vs. Exam Scores

Imagine 5 students who study for different amounts of time, and we record their exam scores. '''
# Data
study_time = [1, 2, 3, 4, 5]  # Hours studied
exam_scores = [50, 55, 70, 85, 90]  # Exam scores in %

# Create scatter plot
plt.scatter(study_time, exam_scores, color='red', marker='o')

# Labels and title
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Score (%)')
plt.title('Study Time vs. Exam Score')

# Show the plot
plt.show()

'''Problem: Market Share of 4 Companies

Let’s say four companies share the market as follows: Company A: 40%, Company B:30%,Company C:20%, Company D: 10%'''

# Data
companies = ['Company A', 'Company B', 'Company C', 'Company D']
market_share = [40, 30, 20, 10]  # Percentage values

# Create Pie Chart
plt.figure()
plt.pie(market_share, labels=companies, autopct='%1.1f%%',
        colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'])

# Add Title
plt.title('Market Share of Companies')

# Show the Pie Chart
plt.show()
