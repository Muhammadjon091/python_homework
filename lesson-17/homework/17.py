import pandas as pd
import numpy as np

# Creating the DataFrame
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Renaming columns using a function
df.rename(columns=lambda x: x.lower().replace(" ", "_"), inplace=True)

# Printing first 3 rows
print("First 3 rows of the DataFrame:")
print(df.head(3))

# Finding the mean age
mean_age = df['age'].mean()
print("\nMean age of individuals:", mean_age)

# Selecting and printing 'name' and 'city' columns
print("\nSelected columns (first_name and city):")
print(df[['first_name', 'city']])

# Adding a new 'Salary' column with random values
df['salary'] = np.random.randint(40000, 100000, size=len(df))

# Displaying summary statistics
print("\nSummary statistics of the DataFrame:")
print(df.describe())


# Creating the sales_and_expenses DataFrame
sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

# Maximum sales and expenses
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
print("\nMaximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)

# Minimum sales and expenses
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()
print("\nMinimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)

# Average sales and expenses
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()
print("\nAverage Sales:", avg_sales)
print("Average Expenses:", avg_expenses)




# Creating the expenses DataFrame
expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

# Setting 'Category' as index
expenses.set_index('Category', inplace=True)

# Maximum expense per category
max_expense = expenses.max(axis=1)
print("\nMaximum expenses per category:")
print(max_expense)

# Minimum expense per category
min_expense = expenses.min(axis=1)
print("\nMinimum expenses per category:")
print(min_expense)

# Average expense per category
avg_expense = expenses.mean(axis=1)
print("\nAverage expenses per category:")
print(avg_expense)




