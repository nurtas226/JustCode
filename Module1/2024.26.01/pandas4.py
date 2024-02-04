import pandas as pd

df = pd.read_csv(
     r'Module1/2024.26.01/data/people1.csv',
)

# print(df.shape)   #
# print(df.head())  #first five
 
# print(df.iloc[:3])  
# print(df.iloc[2])  
# print(df.iloc[0:3, 0])  
# print(df.iloc[:, 0])

# df = df.set_index(df.Name)  
# print(df)

# df = pd.set_index(df.Name)

# res = df.loc[df["Age"] > 30]
# res = df.loc[df["Gender"] == "Male"]
# res = df.loc[df["Name"].str.contains("l")]
# res = df.loc[df["Gender"].str.startswith("F")]
res = df.loc[df["Gender"].str.endswith("ale")]
print(res)