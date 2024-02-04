import pandas as pd

data = {
    "key": ["value", "value2", "value3",],
    "name": ["Nurtas", "Max", "Mati"],
    "surname": ["Muka", "Cesasz", "Bober"],
    "age": [19, 20, 24]
}

df = pd.DataFrame(data)

# df = df.set_index(df.name)

print(df)
