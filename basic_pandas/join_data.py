import pandas as pd

df1 = pd.DataFrame({
    'j1': [1, 2, 3],
    'j2': [1, 2, 3],
    'j3': [1, 2, 3],
    'j4': [1, 2, 3],
})

df2 = pd.DataFrame({
    'j1': [1, 2, 7],
    'j2': [4, 5, 6],
    'j3': [4, 5, 6],
    'j5': [4, 5, 7],
})
# concat the rows
print(pd.concat([df1, df2], axis=0)) # type: ignore
print("\t\t", "-"*15)
#concat teh cols
print(pd.concat([df1, df2], axis=1)) # type: ignore
print("\t\t", "+"*15)
# join the same cols only, the outer will be dropped
df_join = pd.merge(df1, df2, how='inner', on='j1')
print(df_join)
print("\t\t", "="*15)
df_join = pd.merge(df1, df2, how='left', on='j1')
print(df_join)
print("\t\t", "*"*15)
df_join = pd.merge(df1, df2, how='right', on='j1')
print(df_join)
print("\t\t", "=-"*15)
df_join = pd.merge(df1, df2, how='outer', on='j1')
print(df_join)
print("\t\t", "=+"*15)