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


