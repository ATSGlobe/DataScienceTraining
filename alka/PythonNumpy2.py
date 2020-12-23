import numpy as np

#Creating sample array
arr = np.arange(0,11)
print(arr)


#Get a value at an index
print(arr[8])

#Get values in a range
print(arr[1:5])

#Get values in a range
print(arr[0:5])

#Setting a value with index range (Broadcasting)
arr[0:5]=100
#Show
print(arr)

# Reset array, we'll see why I had to reset in  a moment
arr = np.arange(0,11)
#Show
print(arr)

#Important notes on Slices
slice_of_arr = arr[0:6]
#Show slice
print(slice_of_arr)

#Change Slice
slice_of_arr[:]=99
#Show Slice again
print(slice_of_arr)

print(arr)

#To get a copy, need to be explicit
arr_copy = arr.copy()
print(arr_copy)

arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
#Show
print(arr_2d)

#Indexing row
print(arr_2d[1])

# Format is arr_2d[row][col] or arr_2d[row,col]
# Getting individual element value
print(arr_2d[1][0])

# Getting individual element value
print(arr_2d[1,0])

# 2D array slicing
#Shape (2,2) from top right corner
print(arr_2d[:2,1:])

#Shape bottom row
print(arr_2d[2])

#Shape bottom row
print(arr_2d[2,:])

#Set up matrix
print(arr2d = np.zeros((10,10)))

#Length of array
print(arr_length = arr2d.shape[1])

#Set up array
for i in range(arr_length):
    arr2d[i] = i
    print(arr2d)

print(arr2d[[2,4,6,8]])

#Allows in any order
print(arr2d[[6,4,2,7]])

arr = np.arange(1,11)
print(arr)

print(arr > 4)

print(bool_arr = arr>4)

print(bool_arr)

print(arr[bool_arr])

print(arr[arr>2])

x = 2
print(arr[arr>x])


