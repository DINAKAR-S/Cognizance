import numpy as np
print("First array:")
my_array = []
a = int(input("Size of array:"))
for i in range(a):
    my_array.append(float(input("Element:")))
my_array = np.array(my_array)
print(np.floor(my_array))
print("Second array")
my_array1 = []
a = int(input("Size of array:"))
for i in range(a):
    my_array1.append(float(input("Element:")))
my_array1 = np.array(my_array1)
print(np.floor(my_array1))

print("Test above two arrays are equal or not!")
array_equal = np.allclose(np.floor(my_array), np.floor(my_array1))
print(array_equal)