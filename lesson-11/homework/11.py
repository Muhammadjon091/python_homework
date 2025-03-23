# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
# On Windows:
myenv\Scripts\activate
# On macOS/Linux:
source myenv/bin/activate

# Install necessary packages
pip install numpy pandas



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


geometry/
    __init__.py
    circle.py


file_operations/
    __init__.py
    file_reader.py
    file_writer.py



def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()



def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)




from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

# Math operations
print(add(5, 3))
print(subtract(10, 4))
print(multiply(6, 7))
print(divide(8, 2))

# String utilities
print(reverse_string("hello"))
print(count_vowels("beautiful"))

# Geometry
print(calculate_area(5))
print(calculate_circumference(5))

# File operations
write_file("test.txt", "Hello, World!")
print(read_file("test.txt"))
