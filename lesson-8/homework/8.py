try:
    num = int(input("Enter a number: "))
    result = num / 0  # Bu xatolik keltirib chiqaradi
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: Invalid integer input.")



try:
    with open("non_existing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")



try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    if not (a.isdigit() and b.isdigit()):
        raise TypeError("Both inputs must be numbers.")
    result = int(a) + int(b)
except TypeError as e:
    print("Error:", e)




try:
    with open("/root/protected_file.txt", "r") as file:  # Linuxda root huquqlar kerak
        content = file.read()
except PermissionError:
    print("Error: Permission denied.")




my_list = [1, 2, 3]
try:
    print(my_list[5])  # Indeks mavjud emas
except IndexError:
    print("Error: Index out of range.")




try:
    num = input("Enter a number: ")
except KeyboardInterrupt:
    print("\nError: Input was cancelled by the user.")





try:
    x = 1 / float("nan")  # NaN (Not a Number) arifmetik xato keltirishi mumkin
except ArithmeticError:
    print("Error: Arithmetic error occurred.")




try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
except UnicodeDecodeError:
    print("Error: Unicode decoding issue.")




try:
    num = 5
    num.append(10)  # Raqamlar uchun append() metodi yo‘q
except AttributeError:
    print("Error: Attribute does not exist.")







with open("sample.txt", "r") as file:
    print(file.read())

n = 3
with open("sample.txt", "r") as file:
    for _ in range(n):
        print(file.readline(), end="")

with open("sample.txt", "a") as file:
    file.write("\nNew line appended!")

with open("sample.txt", "r") as file:
    print(file.read())

n = 3
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("".join(lines[-n:]))

with open("sample.txt", "r") as file:
    lines = file.readlines()
print(lines)

with open("sample.txt", "r") as file:
    content = file.read()
print(content)

with open("sample.txt", "r") as file:
    words = file.read().split()
print(max(words, key=len))

with open("sample.txt", "r") as file:
    print(len(file.readlines()))

from collections import Counter
with open("sample.txt", "r") as file:
    words = file.read().split()
print(Counter(words))

import os
print(os.path.getsize("sample.txt"))

data = ["Apple", "Banana", "Cherry"]
with open("output.txt", "w") as file:
    file.write("\n".join(data))

with open("sample.txt", "r") as file1, open("copy.txt", "w") as file2:
    file2.write(file1.read())

with open("file1.txt") as f1, open("file2.txt") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip(), line2.strip())

import random
with open("sample.txt") as file:
    lines = file.readlines()
print(random.choice(lines))

file = open("sample.txt")
print(file.closed)
file.close()
print(file.closed)

with open("sample.txt") as file:
    lines = [line.strip() for line in file]
print(lines)

with open("sample.txt") as file:
    words = file.read().replace(",", " ").split()
print(len(words))

import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(letter)



