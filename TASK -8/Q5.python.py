# Array Re-dimensioning
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4))

# Addition of two arrays in numpy
print("ADDITION OF ARRAYS ")
print("First array")
array = []
a = int(input("Size of array:"))
for i in range(a):
    array.append(float(input("Element:")))
my_array = np.array(array)
print(np.floor(array))
print("Second array")
array1= []
a = int(input("Size of array:"))
for i in range(a):
    array1.append(float(input("Element:")))
my_array = np.array(array1)
print(np.floor(array1))

add_array = np.add(array,array1)
print("Array after addition:",add_array)

