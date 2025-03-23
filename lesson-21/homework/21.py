df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)
print(df1[['Student_ID', 'Average']])


top_student = df1.loc[df1['Average'].idxmax()]
print("Student with Highest Average Grade:\n", top_student)

df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
print(df1[['Student_ID', 'Total']])



import matplotlib.pyplot as plt

subject_means = df1[['Math', 'English', 'Science']].mean()
subject_means.plot(kind='bar', color=['blue', 'green', 'red'])
plt.title("Average Grades in Each Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Grade")
plt.show()




import pandas as pd
import matplotlib.pyplot as plt

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# Exercise 1: Total sales for each product
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("Total Sales:\n", total_sales)

# Exercise 2: Date with highest total sales
df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
highest_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
print("Date with Highest Sales:", highest_sales_date)

# Exercise 3: Percentage change in sales for each product
df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100

# Exercise 4: Line chart for sales trends
df2.plot(x='Date', y=['Product_A', 'Product_B', 'Product_C'], kind='line', marker='o')
plt.title("Sales Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend(["Product A", "Product B", "Product C"])
plt.grid()
plt.show()





data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Exercise 1: Average salary for each department
avg_salary = df3.groupby('Department')['Salary'].mean()
print("Average Salary by Department:\n", avg_salary)

# Exercise 2: Employee with most experience
most_experienced_employee = df3.loc[df3['Experience (Years)'].idxmax()]
print("Most Experienced Employee:\n", most_experienced_employee)

# Exercise 3: Salary Increase from minimum salary
min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100

# Exercise 4: Bar chart for employees per department
df3['Department'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Employee Distribution Across Departments")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()




data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# Exercise 1: Total revenue from all orders
total_revenue = df4['Total_Price'].sum()
print("Total Revenue:", total_revenue)

# Exercise 2: Most ordered product
most_ordered_product = df4['Product'].value_counts().idxmax()
print("Most Ordered Product:", most_ordered_product)

# Exercise 3: Average quantity of products ordered
avg_quantity = df4['Quantity'].mean()
print("Average Quantity Ordered:", avg_quantity)

# Exercise 4: Pie chart for sales distribution
df4.groupby('Product')['Total_Price'].sum().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'salmon'])
plt.title("Sales Distribution by Product")
plt.ylabel("")  # Hide y-label
plt.show()
