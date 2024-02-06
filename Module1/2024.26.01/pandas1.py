import pandas as pd

data = {
    "key": ["value", "value2"],
    "name": ["Nurtas", "Max"],
    "surname": ["Muka", "Cesasz"],
    "age": [19, 20]
}

df = pd.DataFrame(data)

print(df)
print("===================================")

s = pd.Series([1,5,23,6])
s = pd.Series(["max", "apple", "banana"])

print(s)
print(type(s))
print("===================================")
print(df.name)
print(type(df.name))