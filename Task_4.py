import pandas as pd


df=pd.read_csv("D:/data/Task_4.csv")
print(df.head())

pivot_table = pd.pivot_table(df, values='SalePrice', index=['Street', 'LotShape'], columns='SaleCondition', aggfunc='mean')

print(pivot_table)

