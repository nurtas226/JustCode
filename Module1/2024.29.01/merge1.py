import pandas as pd

data1 = {
    "name": ["Max", "Aray", "Yerbol"],
    "age": [12, 20, 35]

}

data2 = {
    "name": ["Sasha", "Aray", "Yerbol", "Olya"],
    "gender": ["Male", "Female", "Male", "Female"]
}


df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("=== df1 =============================================")
print(df1)
print("=== df2 =============================================")
print(df2)


res = pd.merge(df1, df2, on='name', how='outer')

# res = pd.merge(df1, df2, how='cross')

print("=== res =============================================")
print(res)