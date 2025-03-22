def insert_underscore(txt):
    vowels = "aeiouAEIOU"  # Unli harflar
    result = []
    count = 0  # Har 3-belgini sanash uchun
    
    i = 0
    while i < len(txt):
        result.append(txt[i])
        count += 1
        
        # Har 3-belgidan keyin "_" qo'shamiz, lekin shartlarni tekshiramiz
        if count == 3 and i < len(txt) - 1:  # Oxirida "_" qo‘yilmasligi uchun
            if txt[i + 1] in vowels or (i + 1 < len(txt) - 1 and txt[i + 2] == "_"):
                result.append(txt[i + 1])  # Keyingi belgi unli bo‘lsa, `_` ni suramiz
                i += 1  # Keyingi belgini o‘tkazib yuboramiz
            
            result.append("_")  # `_` qo'shamiz
            count = 0  # Qayta sanashni boshlaymiz
        
        i += 1  # Keyingi belgi
    
    return "".join(result)

txt = input("Matn kiriting: ")
print(insert_underscore(txt))


# Read an integer from input
n = int(input())
# Loop from 0 to n-1 and print the square of each number
for i in range(n):
    print(i ** 2)


# Initialize counter
i = 1  
# Loop until 10
while i <= 10:
    print(i)
    i += 1

# Loop from 1 to 5
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Move to the next line


def sum_of_numbers(n):
    return n * (n + 1) // 2  # Using integer division
# Example usage
num = int(input("Enter a number: "))
print("Sum from 1 to", num, "is:", sum_of_numbers(num))


def multiplication_table(n, up_to=10):
    for i in range(1, up_to + 1):
        print(f"{n} x {i} = {n * i}")
# Example usage
num = int(input("Enter a number: "))
multiplication_table(num)


numbers = [12, 75, 150, 180, 145, 525, 50]
# Indekslar bo‘yicha kerakli elementlarni chiqarish
indekslar = [1, 2, 4]  # 75, 150 va 145 joylashgan indekslar
for i in indekslar:
    print(numbers[i])


num = 75869
print("Total digits:", len(str(num)))


n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


list1 = [10, 20, 30, 40, 50]
for num in reversed(list1):
    print(num)


for num in range(-10, 0):
    print(num)



for i in range(5):
    print(i)
print("Done!")



start, end = 25, 50
print("Prime numbers between", start, "and", end, ":")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)


n = 10
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b



def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = 5
print(f"{num}! =", factorial(num))


def uncommon_elements(list1, list2):
    return [item for item in list1 + list2 if (list1 + list2).count(item) == 1]
# Test
print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]


