import numpy as np

# 1. Write a Python program to convert a list of numeric value into a one-dimensional NumPy array.
original_list = [12.23, 13.32, 100, 36.32]
numpy_array = np.array(original_list)

print("Original List:", original_list)
print("One-dimensional numpy array:", numpy_array)


# 2. Create a 3x3 matrix with values ranging from 2 to 10.
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)


# 3. Write a Python program to create a null vector of size 10 and update sixth value to 11.
null_vector = np.zeros(10)
print(null_vector)

print("Update sixth value to 11")
null_vector[6] = 11
print(null_vector)


# 4. Write a Python program to reverse an array (first element becomes last).
original_array = np.arange(12, 38)
reversed_array = original_array[::-1]

print("Original array:")
print(original_array)
print("Reverse array:")
print(reversed_array)


# 5. Write a Python program to create a 2d array with 1 on the border and 0 inside.
original_array = np.ones((5, 5))
print("Original array:")
print(original_array)

inside_zeros = original_array.copy()
inside_zeros[1:-1, 1:-1] = 0

print("\n1 on the border and 0 inside in the array")
print(inside_zeros)


# 6. Write a Python program to add a border (filled with 0's) around an existing array.
original_array = np.ones((3, 3))
print("Original array:")
print(original_array)

bordered_array = np.zeros((5, 5))
bordered_array[1:-1, 1:-1] = original_array

print("1 on the border and 0 inside in the array")
print(bordered_array)


# 7. Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern.
checkerboard = np.zeros((8, 8), dtype=int)
checkerboard[1::2, 0::2] = 1
checkerboard[0::2, 1::2] = 1

print("Checkerboard pattern:")
print(checkerboard)


# 8. Write a Python program to convert a list and tuple into arrays.
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])

list_array = np.array(my_list)
tuple_array = np.array(my_tuple)

print("List to array:")
print(list_array)
print("Tuple to array:")
print(tuple_array)


# 9. Write a Python program to append values to the end of an array.
original_array = np.array([10, 20, 30])
print("Original array:")
print(original_array)

appended_array = np.append(original_array, [40, 50, 60, 70, 80, 90])
print("\nAfter append values to the end of the array:")
print(appended_array)


# 10. Write a Python program to find the real and imaginary parts of an array of complex numbers.
complex_array = np.array([1.00000000+0.j, 0.70710678+0.70710678j])
print("Original array", complex_array)

real_part = np.real(complex_array)
print("Real part of the array:")
print(real_part)

imaginary_part = np.imag(complex_array)
print("Imaginary part of the array:")
print(imaginary_part)


# 11. Write a Python program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements.
sample_array = np.array([1, 2, 3], dtype=np.float64)

array_size = sample_array.size
element_bytes = sample_array.itemsize
total_bytes = sample_array.nbytes

print("Size of the array:", array_size)
print("Length of one array element in bytes:", element_bytes)
print("Total bytes consumed by the elements of the array:", total_bytes)


# 12. Write a Python program to find common values between two arrays.
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([10, 30, 40])

print("Array1:", array1)
print("Array2:", array2)

common_values = np.intersect1d(array1, array2)
print("Common values between two arrays:")
print(common_values)


# 13. Write a Python program to find the set difference of two arrays. The set difference will return the sorted, unique values in array1 that are not in array2.
array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70, 90])

print("Array1:", array1)
print("Array2:", array2)

set_difference = np.setdiff1d(array1, array2)
print("Set difference between two arrays:")
print(set_difference)


# 14. Write a Python program to find the set exclusive-or of two arrays. Set exclusive-or will return the sorted, unique values that are in only one (not both) of the input arrays.
array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70])

print("Array1:", array1)
print("Array2:", array2)

exclusive_or = np.setxor1d(array1, array2)
print("Unique values that are in only one (not both) of the input arrays:")
print(exclusive_or)


# 15. Write a Python program compare two arrays using numpy.
a = np.array([1, 2])
b = np.array([4, 5])

print("Array a:", a)
print("Array b:", b)

print("a > b")
print(a > b)
print("a >= b")
print(a >= b)
print("a < b")
print(a < b)
print("a <= b")
print(a <= b)


# 16. Write a Python program to save a NumPy array to a text file.
sample_array = np.array([1, 2, 3, 4, 5])
np.savetxt('sample_array.txt', sample_array)
print("Array saved to 'sample_array.txt'")


# 17. Write a Python program to create a contiguous flattened array.
original_array = np.array([[10, 20, 30], [20, 40, 50]])
print("Original array:")
print(original_array)

flattened_array = np.ravel(original_array)
print("New flattened array:")
print(flattened_array)


# 18. Write a Python program to change the data type of an array.
x = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print(x)
print("Data type of the array x is:", x.dtype)

print("New Type: float64")
y = x.astype(np.float64)
print(y)


# 19. Write a Python program to create a 3-D array with ones on a diagonal and zeros elsewhere.
identity_3d = np.eye(3)
print(identity_3d)


# 20. Write a Python program to create an array which looks like below array.
# Expected Output:
# [[ 0. 0. 0.]
#  [ 1. 0. 0.]
#  [ 1. 1. 0.]
#  [ 1. 1. 1.]]
custom_array = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 1]
], dtype=float)
print(custom_array)


# 21. Write a Python program to concatenate two 2-dimensional arrays.
array1 = np.array([[0, 1, 3], [5, 7, 9]])
array2 = np.array([[0, 2, 4], [6, 8, 10]])
print("Sample arrays:", (array1.tolist(), array2.tolist()))

concatenated_array = np.hstack((array1, array2))
print("Expected Output:")
print(concatenated_array)


# 22. Write a Python program to make an array immutable (read-only).
x = np.zeros(5)
x.flags.writeable = False
print("Test the array is read-only or not:")
print("Try to change the value of the first element:")
try:
    x[0] = 1
    print("Array is not read-only")
except ValueError as e:
    print("ValueError:", e)


# 23. Write a Python program to create an array of (3, 4) shape, multiply every element value by 3 and display the new array.
original_array = np.arange(12).reshape(3, 4)
print("Original array elements:")
print(original_array)

multiplied_array = original_array * 3
print("New array elements:")
print(multiplied_array)


# 24. Write a Python program to convert a NumPy array into Python list structure.
original_array = np.arange(6).reshape(3, 2)
print("Original array elements:")
print(original_array)

array_to_list = original_array.tolist()
print("Array to list:")
print(array_to_list)


# 25. Write a Python program to print array values with precision 3.
original_array = np.array([0.26153123, 0.52760141, 0.5718299, 0.5927067, 
                           0.7831874, 0.69746349, 0.35399976, 0.99469633, 
                           0.0694458, 0.54711478])
print("Original array elements:")
print(original_array)

np.set_printoptions(precision=3)
print("Print array values with precision 3:")
print(original_array)


# 26. Write a Python program to suppresses the use of scientific notation for small numbers in numpy array.
original_array = np.array([1.60000000e-10, 1.60000000e+00, 1.20000000e+03, 2.35000000e-01])
print("Original array elements:")
print(original_array)

np.set_printoptions(suppress=True, precision=3)
print("Print array values with precision 3:")
print(original_array)


# 27. Write a Python program to how to add an extra column to an numpy array.
original_array = np.array([[10, 20, 30], [40, 50, 60]])
new_column = np.array([[100], [200]])

result_array = np.hstack((original_array, new_column))
print(result_array)


# 28. Write a Python program to remove specific elements in a numpy array.
original_array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Original array:")
print(original_array)

indices_to_delete = np.array([0, 3, 4])
result_array = np.delete(original_array, indices_to_delete)
print("Delete first, fourth and fifth elements:")
print(result_array)
