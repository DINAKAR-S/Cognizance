import numpy as np
print("Enter the word")
my_array = []
a = int(input("Size of array:"))
for i in range(a):
    my_array.append(input("Element:"))
my_array = np.array(my_array)
print("Original Array:",my_array)
capitalized_case = np.char.capitalize(my_array)
print("Characterised word:",capitalized_case)
