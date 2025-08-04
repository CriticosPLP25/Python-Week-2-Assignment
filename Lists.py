# A list of 5 numbers
List_a=[4, 5, 5, 6, 7] # int
print(List_a)
List_a.append(8)  # Adding a new item to the list
print(List_a)
# A list of two words
List_b=["Hello", "World"] # str
print(List_b)

# A list of numbers with decimals
List_c= [1.5, 4.5, 5.5] # float
print(List_c)
# Access item index 0(List_b)
print(List_b[0])
# Access item index 1(List_a)
print(List_a[1])
List_b.extend(List_a) # Adding List_b to List_a
print(List_b)
List_a[2] = 10  # Changing the value of index 2 in List_a
print(List_a)
del List_a[3]  # Deleting the item at index 3 in List_a
print(List_a)
List_b.remove("World")  # Removing "World" from List_b
print(List_b)
