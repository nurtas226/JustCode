import pandas as pd

data1 = {
    "name": ["Max", "ZAray", "Yerbol"],
    "age": [12, 20, 35],
    "test": [1, 1, 1]

}

data2 = {
    "first_name": ["Sasha", "ZAray", "Yerbol", "Olya"],
    "gender": ["Male", "Female", "Male", "Female"],
    "test": [2, 2, 2, 2]
}


df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("=== df1 =============================================")
print(df1)
print("=== df2 =============================================")
print(df2)


res = pd.merge(df1, df2, left_on="name", right_on="first_name", how='left', sort=False, suffixes=("_mkldf", "_qqq"))
# res2 = pd.merge(df1, df2, left_on="name", right_on="first_name", how='right', sort=True)

print("=== res =============================================")
print(res)



# print("=== res2 =============================================")
# print(res2)
# print(res.loc[:, ['name', 'age', 'gender']])