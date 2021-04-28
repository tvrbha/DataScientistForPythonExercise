import numpy as np

'''
Exercise 1: NumPy: Create an array with values ranging from 12 to 38
'''

array_range = np.arange(12, 38)
print(array_range)

'''
Exercise 2: Add a border around an existing array
'''

array_ones = np.ones((3, 3))
print(array_ones)
array_ones_border = np.pad(array_ones, pad_width=1)
print(array_ones_border)

'''
Exercise 3: Convert a list and tuple into arrays
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(my_list)
print("List to array: ")
print(np.asarray(my_list))

my_tuple = ([8, 4, 6], [1, 2, 3])
print("Tuple to array: ")
print(np.asarray(my_tuple))

'''
Exercise 4: Convert the values of Centigrade degrees into Fahrenheit degrees
'''
val_in_fahrenheit = np.array([0., 12., 45.21, 34., 99.91])
print(val_in_fahrenheit)

val_in_celcius = (val_in_fahrenheit - 32) / 1.8
print(val_in_celcius)


'''
Exercise 5: Write a NumPy program 
to find the number of elements of an array, 
length of one array element in bytes and total bytes consumed by the elements.
'''

array_range = np.arange(12, 38)
print(f"Number of elements of an array {array_range.size}")
print(f"length of one array element in bytes {array_range.itemsize}")
print(f"total bytes consumed by the elements {array_range.nbytes}")
print(f"total bytes consumed by the elements {array_range.dtype}")


'''
Exercise 6: Get the unique elements of an array
'''

x = np.array([10, 10, 20, 20, 30, 30])
print(np.unique(x))

x = np.array([[1, 1], [2, 3]])
print(np.unique(x))


'''
Exercise 7: Change the dimension of an array
'''

original_array = np.array([1,2,3,4,5,6,7,8,9])
print(original_array)

new_array_shape = original_array.reshape(3,3)
print(new_array_shape)


'''
Exercise 8: Create a 1-D array of 30 evenly spaced elements between 2.5. and 6.5, inclusive
'''

evenly_array_1d_30 = np.linspace(2.5, 6.5, 30)
print(evenly_array_1d_30)

'''
Exercise 9: Convert 1-D arrays as columns into a 2-D array
'''

a = np.array((10,20,30))
b = np.array((40,50,60))

c = np.column_stack((a, b))
print(c)

d = np.row_stack((a,b))
print(d)

'''
Exercise 10: Create a 5x5 matrix with row values ranging from 0 to 4
'''
x = np.zeros((5,5))

#x += np.arange(5)

x[::] = [0,1,2,3,4]

print(x)


'''
Exercise 11: Sum of all the multiples of 3 or 5 below 100
'''

x = np.arange(1,100)
print(x)

n = x [(x%3==0) | (x%5 == 0)]
print(n.sum())



'''
Exercise 12: Combine a one and a two dimensional array together and display their elements
'''

x = np.arange(4)
print("One dimensional array:")
print(x)
y = np.arange(8).reshape(2,4)
print("Two dimensional array:")
print(y)
for a, b in np.nditer([x,y]):
    print(f"{a}:{b}")

'''
Exercise 13: Write a NumPy program to replace all elements of NumPy array that are greater than specified array.
'''
x = np.array([[ 0.42436315, 0.48558583, 0.32924763], [ 0.7439979,0.58220701,0.38213418], [ 0.5097581,0.34528799,0.1563123 ]])
print("Original array:")
print(x)
print("Replace all elements of the said array with .5 which are greater than .5")
x[x > .5] = .5
print(x)

'''
Exercise 14: Add a new row to an empty numpy array
'''

arr = np.empty((0,3), int)
print("Empty array:")
print(arr)
arr = np.append(arr, np.array([[10,20,30]]), axis=0)
arr = np.append(arr, np.array([[40,50,60]]), axis=0)
print("After adding two new arrays:")
print(arr)


'''
Exercise 15: Write a NumPy program to join a sequence of arrays along a new axis.
'''

x = np.array([1, 2, 3])
y = np.array([2, 3, 4])
print("Original arrays:")
print(x)
print(y)
print("Sequence of arrays along a new axis:")
print(np.vstack((x, y)))
x = np.array([[1], [2], [3]])
y = np.array([[2], [3], [4]])
print("\nOriginal arrays:")
print(x)
print()
print(y)
print("Sequence of arrays along a new axis:")
print(np.vstack((x, y)))