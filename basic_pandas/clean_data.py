import numpy as np
import pandas as pd

df = pd.DataFrame({
    'j1': [1, 2, 3, 4, 5, 6, 7],
    'j2': ['j', 'a', 'f', 'l', 'o', 'k', 'a'],
    'j3': ['a', 'l', 'i', 'l', 'o', 'k', 'a'],
    'j4': [1, 2, 3, 4, 5, 6, 7],
})
print(df)
print("\t\t", "-"*15)
# check the duplicated rows only
dDf = df.duplicated()
print(dDf)
print("\t\t", "+"*15)
# display only the result after droping the duplicates
print(df.drop_duplicates())
print("\t\t", "="*15)
