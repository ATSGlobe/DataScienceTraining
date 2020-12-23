import pandas as pd
import numpy as np

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())

print(df)

## Selection and Indexing

print(df['W'])

# Pass a list of column names
print(df[['W','Z']])

# SQL Syntax (NOT RECOMMENDED!)
print(df.W)

print(type(df['W']))

#Creating a new column

df['new'] = df['W'] + df['Y']

print(df)

#Removing Columns

print(df.drop('new',axis=1))

# Not inplace unless specified!
print(df)

df.drop('new',axis=1,inplace=True)

print(df)

#Drop rows

print(df.drop('E',axis=0))

#Selecting Rows

print(df.loc['A'])

#select based off of position instead of label 

print(df.iloc[2])

#subset of rows and columns

print(df.loc['B','Y'])

print(df.loc[['A','B'],['W','Y']])

### Conditional Selection
print(df)

print(df>0)

print(df[df>0])

print(df[df['W']>0])

print(df[df['W']>0]['Y'])

print(df[df['W']>0][['Y','X']])

#For two conditions you can use | and & with parenthesis

print(df[(df['W']>0) & (df['Y'] > 1)])

## More Index Details
print(df)

# Reset to default 0,1...n index
print(df.reset_index())

newind = 'CA NY WY OR CO'.split()
df['States'] = newind
print(df)

print(df.set_index('States'))

print(df)

df.set_index('States',inplace=True)
print(df)

## Multi-Index and Index Hierarchy
# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

print(hier_index)

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
print(df)

print(df.loc['G1'])

print(df.loc['G1'].loc[1])

print(df.index.names)

df.index.names = ['Group','Num']
print(df)

print(df.xs('G1'))

print(df.xs(['G1',1]))

print(df.xs(1,level='Num'))

