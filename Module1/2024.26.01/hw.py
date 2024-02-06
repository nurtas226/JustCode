import pandas as pd

df = pd.read_csv(
     r'Module1/2024.26.01/data/people1.csv',
)

# 1.
# res = df.loc[df["Gender"] == "Male"]
# path = 'C:/Users/nurta/OneDrive/Рабочий стол/education/JustCode/Module1/2024.26.01/data/'
# res.to_csv(path+"male.csv")

# 2.
# res = df.loc[df["Age"] > 30]
# path = 'C:/Users/nurta/OneDrive/Рабочий стол/education/JustCode/Module1/2024.26.01/data/'
# res.to_csv(path+"age.csv")

# 3.
filtered_df = df[["Name", "Age"]]
path = 'C:/Users/nurta/OneDrive/Рабочий стол/education/JustCode/Module1/2024.26.01/data/'
filtered_df.to_csv(path+"filtered.csv")
