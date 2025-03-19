def is_leap(year):
    """Determines whether a given year is a leap year.
    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)





def number(n):
    if n % 2 != 0:
        print('Weird')
    elif 2 <= n <= 5:
        print('Not Weird')
    elif 6 <= n <= 20:
        print('Weird')
    else:  # Bu yerda `elif n > 20:` o‘rniga `else` ishlatsa bo‘ladi
        print('Not Weird')

# Funksiyani chaqirish
num = int(input("Enter a number: "))
number(num)







def find_even_numbers(a, b):
    if a % 2 != 0:
        a += 1  # Agar `a` toq bo'lsa, uni keyingi juft songa o‘tkazamiz
    if b % 2 != 0:
        b -= 1  # Agar `b` toq bo'lsa, uni oldingi juft songa o‘tkazamiz
    if a > b:
        return []  # Agar `a` katta bo'lib ketsa, bo‘sh ro‘yxat qaytaramiz
    return list(range(a, b + 1, 2))  # `range(a, b + 1, 2)` faqat juft sonlarni oladi

# Funksiyani sinash
a, b = 3, 11
print(find_even_numbers(a, b))  # [4, 6, 8, 10]





def find_even_numbers_math(a, b):
    start = a + (a % 2)  # Agar `a` toq bo'lsa, uni keyingi juft songa chiqaramiz
    end = b - (b % 2)    # Agar `b` toq bo'lsa, uni oldingi juft songa tushiramiz
    return list(range(start, end + 1, 2)) * (start <= end)  # Start va end oraliqni tekshiramiz

# Funksiyani sinash
a, b = 3, 11
print(find_even_numbers_math(a, b))  # [4, 6, 8, 10]
