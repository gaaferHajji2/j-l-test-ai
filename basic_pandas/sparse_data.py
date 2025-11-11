import numpy as np
import pandas as pd

df = pd.DataFrame({
    'j1': [1, 2, 3, np.nan, 5, 6],
    'j2': [1, np.nan, 3, 4, 5, 6],
    'j3': [1, 2, 3, 4, np.nan, 6]
})

print("The original data is: ", df)
print("\t\t", "-"*15)
print(df.isna().sum())
print("\t\t", "="*15)
print(df.isna())
print("\t\t", "*"*15)
df_new = df.fillna(7.0)
print(df_new)
print("\t\t", "\\"*15)
df_new_02 = df.dropna()
print(df_new_02)
print("\t\t", "/"*15)
# droping the cols that contains na
df_new_03 = df.dropna(axis=1) # empty data, all cols contains na
print(df_new_03)
print("\t\t", "=-"*15)