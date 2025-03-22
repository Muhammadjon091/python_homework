def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test
print(is_prime(4))  # False
print(is_prime(7))  # True




def digit_sum(k):
    return sum(int(digit) for digit in str(k))

# Test
print(digit_sum(24))   # 6 (2 + 4)
print(digit_sum(502))  # 7 (5 + 0 + 2)




def powers_of_two(N):
    power = 1
    while power <= N:
        print(power, end=" ")
        power *= 2

# Test
powers_of_two(10)  # 2 4 8





