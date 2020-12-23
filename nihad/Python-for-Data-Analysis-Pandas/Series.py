import numpy as np
import pandas as pd

#Series
labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}

#Lists

print(pd.Series(data=my_list))

print(pd.Series(data=my_list,index=labels))

print(pd.Series(my_list,labels))

#NumPy Arrays 

print(pd.Series(arr))

print(pd.Series(arr,labels))

#Dictionary

print(pd.Series(d))

# Data in a Series
print(pd.Series(data=labels))

# Even functions 
print(pd.Series([sum,print,len]))

## Using an Index

ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])                                   

print(ser1)

ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])                                   

print(ser2)

print(ser1['USA'])

#Operations are then also done based off of index

print(ser1 + ser2)

