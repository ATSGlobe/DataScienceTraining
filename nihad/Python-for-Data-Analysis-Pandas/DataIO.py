import numpy as np
import pandas as pd

df = pd.read_csv('example')
print(df)

#CSV Output

print(df.to_csv('example',index=False))

## Excel
ex = pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')
print(ex)
### Excel Output

print(df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1'))

## HTML

df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')

print(df[0])
