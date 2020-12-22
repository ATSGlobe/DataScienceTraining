## Using NumPy
import numpy as np

# Numpy Arrays
## Creating NumPy Arrays

### From a Python List
my_list = [1,2,3]
print(my_list)

print(np.array(my_list))

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(my_matrix)

print(np.array(my_matrix))

## Built-in Methods
### arange
print(np.arange(0,10))

print(np.arange(0,11,2))

### zeros and ones
print(np.zeros(3))

print(np.zeros((5,5)))

print(np.ones(3))

print(np.ones((3,3)))

### linspace
print(np.linspace(0,10,3))

print(np.linspace(0,10,50))

## eye
print(np.eye(4))

## Random 
### rand
print(np.random.rand(2))

print(np.random.rand(5,5))

### randn
print(np.random.randn(2))

print(np.random.randn(5,5))

### randint
print(np.random.randint(1,100))

print(np.random.randint(1,100,10))

## Array Attributes and Methods
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)

print(arr)

print(ranarr)

## Reshape
print(arr.reshape(5,5))

### max,min,argmax,argmin
print(ranarr)

print(ranarr.max())

print(ranarr.argmax())

print(ranarr.min())

print(ranarr.argmin())

## Shape
# Vector
print(arr.shape)

# Notice the two sets of brackets
print(arr.reshape(1,25))

print(arr.reshape(1,25).shape)

print(arr.reshape(25,1))

print(arr.reshape(25,1).shape)

### dtype
print(arr.dtype)
