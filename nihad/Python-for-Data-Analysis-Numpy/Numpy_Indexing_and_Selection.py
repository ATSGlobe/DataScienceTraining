import numpy as np

#Creating sample array
arr = np.arange(0,11)
#Show
print(arr)

#Get a value at an index
print(arr[8])

#Get values in a range
print(arr[1:5])

#Get values in a range
print(arr[0:5])

#Setting a value with index range (Broadcasting)
arr[0:5]=100
print(arr)

# Reset array
arr = np.arange(0,11)
print(arr)

#Slices
slice_of_arr = arr[0:6]
print(slice_of_arr)

#Change Slice
slice_of_arr[:]=99
print(slice_of_arr)

print(arr)

#copy
arr_copy = arr.copy()
print(arr_copy)

#Indexing 2D array
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)

#Indexing row
print(arr_2d[1])

# Format is arr_2d[row][col] or arr_2d[row,col]
# Getting individual element value
print(arr_2d[1][0])

# 2D array slicing
#Shape (2,2) from top right corner
print(arr_2d[:2,1:])

#Shape bottom row
print(arr_2d[2,:])

#Set up matrix
arr2d = np.zeros((10,10))
#Length of array
arr_length = arr2d.shape[1]
#Set up array

for i in range(arr_length):
    arr2d[i] = i
    
print(arr2d)

print(arr2d[[2,4,6,8]])

#Allows in any order
print(arr2d[[6,4,2,7]])

#Selection
arr = np.arange(1,11)
print(arr)

print(arr > 4)

bool_arr = arr>4
print(bool_arr)

print(arr[bool_arr])

print(arr[arr>2])

x = 2
print(arr[arr>x])
