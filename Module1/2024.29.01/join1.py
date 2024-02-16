import pandas as pd

data1 = {
    "name": ["Max", "Aray", "Yerbol"],
    "age": [12, 20, 35]

}

data2 = {
    "first_name": ["Sasha", "Aray", "Yerbol", "Olya"],
    "gender": ["Male", "Female", "Male", "Female"]
}


df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df1.set_index('name', inplace=True)
df2.set_index('first_name', inplace=True)

print("=== df1 =============================================")
print(df1)
print("=== df2 =============================================")
print(df2)


res = df1.join(df2, how='cross')

print("=== res =============================================")
print(res)