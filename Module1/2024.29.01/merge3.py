import pandas as pd

data1 = {
    "name": ["Max", "Aray", "Yerbol", "Aray"],
    "age": [12, 20, 35, 99],

}

data2 = {
    "first_name": ["Sasha", "Aray", "Yerbol", "Olya"],
    "gender": ["Male", "Female", "Male", "Female"],
}


df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("=== df1 =============================================")
print(df1)
print("=== df2 =============================================")
print(df2)


res = pd.merge(df1, df2, left_on="name", right_on="first_name", how='outer', indicator=True, validate='m:m')

print("=== res =============================================")
print(res)



# print("=== res2 =============================================")
# print(res2)
# print(res.loc[:, ['name', 'age', 'gender']])