import pandas as pd

df1 = pd.read_csv('data/sales_2021.csv').iloc[:3]
df2 = pd.read_csv('data/sales_2022.csv').iloc[:4]
df3 = pd.read_csv('data/sales_2022.csv').iloc[15:17]

print("=== df1 =============================================")
print(df1)
print("=== df2 =============================================")
print(df2)
print("=== df3 =============================================")
print(df2)


# res = df1.join(df2, how='cross')
# res = pd.concat([df1, df2], ignore_index=True)
# res = pd.concat([df1, df2], ignore_index=False)
res = pd.concat([df1, df2, df3], ignore_index=False)

print("=== res =============================================")
print(res)