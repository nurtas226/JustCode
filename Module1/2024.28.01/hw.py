import pandas as pd


df = pd.read_csv(
     r'Module1/2024.28.01/sales.csv',
)

sales = len(df)
print(sales)

# total_income =  (df['Quantity'] * df['Price']).sum()
# print(total_income)

# avg_price = df["Price"].mean() 
# print(avg_price)