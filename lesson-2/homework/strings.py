name = input("What is your name? ")
birth_year = input("What year were you born? ")
age = 2025 - int(birth_year)
print(f"Hello, {name}! You are {age} years old in 2025.")


t='LMaasleitbtui'
car1 = t[1::2]
car2 = t[::2]
print(car1, car2)



t='MsaatmiazD'
car3 = t[10::-2]
car4 = t[::2]
print(car3, car4)



t1="I'm John. I am from London."
L=t1[-7:-1]
print(L)




text = input("Enter some text: ")
a = text[::-1]
print(a)



text = input("Enter a text: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)




numbers = [5, 3, 8, 2, 9, 4]
max_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num

print("Maximum number:", max_number)



number = int(input("Enter a number: "))  
l = len(str(number)) // 2  
n1 = str(number)[:l]  
n2 = str(number)[l:]  

if sum(int(i) for i in n1) == sum(int(i) for i in n2):  
    print("This is palindrome number")  
else:  
    print("This is ordinary number")




email = input("Elektron pochta manzilini kiriting: ")
domain = email.split('@')[-1] if '@' in email else "Noto‘g‘ri email manzil"
print("Domen:", domain)




import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user-defined password length (optional)
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
