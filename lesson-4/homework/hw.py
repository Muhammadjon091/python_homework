# Sample dictionary
my_dict = {'a': 3, 'b': 1, 'c': 2}

# Sorting in ascending order
ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sorting in descending order
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending:", ascending)
print("Descending:", descending)




my_dict = {0: 10, 1: 20}
my_dict[2] = 30  # Adding a new key-value pair

print(my_dict)




dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Merging all dictionaries
merged_dict = {**dic1, **dic2, **dic3}

print(merged_dict)




n = 5
squares_dict = {x: x*x for x in range(1, n+1)}

print(squares_dict)




squares_dict = {x: x*x for x in range(1, 16)}

print(squares_dict)




my_set = {1, 2, 3, 4, 5}
print(my_set)



my_set = {10, 20, 30, 40, 50}

for item in my_set:
    print(item)



my_set = {1, 2, 3}
my_set.add(4)  # Adding a single element
my_set.update([5, 6])  # Adding multiple elements

print(my_set)




my_set = {1, 2, 3, 4, 5}
my_set.remove(3)  # Removes 3, raises an error if not found

print(my_set)




my_set = {1, 2, 3, 4, 5}
my_set.discard(3)  # Removes 3 if it exists, does nothing if not found

print(my_set)
