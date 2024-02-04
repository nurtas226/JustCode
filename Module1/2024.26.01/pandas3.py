# import pandas as pd

# df = pd.read_csv(r'Module1/2024.26.01/data/people1.csv')

# print(df)


import pandas as pd

df = pd.read_csv(
     r'Module1/2024.26.01/data/people1.csv',
     header = None,
     names=['n1', 'n2', 'n3', 'n4',]
)

print(df)