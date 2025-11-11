import numpy as np
import pandas as pd

# Creating a Series data
series = pd.Series([1, 2, 3, 4, 5, np.nan, 6, 7])
print(series)
print("\t\t", '-' * 15)
dSeries = pd.Series({ 'a': 1.0, 'l': 2.0, 'o': 3.0, 'k': 4.0, 'a-02': 5.0})
print(dSeries)
print("\t\t", '-' * 15)

# Creating Data Frame
# here the arrays must be the same length, else ValueError
df = pd.DataFrame({ 'j': [1.0, 2.0], 'loka': [3.0, 4.0], 'loka-02': [5.0, 6.0]})
print(df)
print("\t\t", '-' * 15)
# Also we can use dot, like: df.j, df.loka
print(df['j'])
print("\t\t", '-' * 15)
print(df['loka'])
print("\t\t", '-' * 15)
print(df['loka-02'])
print("\t\t", '*' * 15)
df.index = ['j1', 'j2'] # type: ignore
print(df.loc['j1', 'j'])
print("\t\t", '+' * 15)
print(df.loc['j1'])
print("\t\t", '=' * 15)
print(df.iloc[0:2, 1])
print("\t\t", '=-' * 15)
# boolean indexing where select the first row: j1
print(df[df['j'] > 1])
print("\t\t", '=+' * 15)
