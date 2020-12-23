import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())

#Info on Unique Values

print(df['col2'].unique())

print(df['col2'].nunique())

print(df['col2'].value_counts())

### Selecting Data

#Select from DataFrame using criteria from multiple columns
newdf = df[(df['col1']>2) & (df['col2']==444)]
print(newdf)

### Applying Functions

def times2(x):
    return x*2

print(df['col1'].apply(times2))

print(df['col3'].apply(len))

print(df['col1'].sum())

#Permanently Removing a Column

del df['col1']
print(df)

#Get column and index names

print(df.columns)

print(df.index)

#Sorting and Ordering a DataFrame

print(df)

print(df.sort_values(by='col2'))

#Find Null Values or Check for Null Values

print(df.isnull())

# Drop rows with NaN Values
df.dropna()

#Filling in NaN values with something else

import numpy as np

df = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
print(df.head())

print(df.fillna('FILL'))

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)

print(df)

print(df.pivot_table(values='D',index=['A', 'B'],columns=['C']))
