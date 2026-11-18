# Reflection 1: A boolean filter filters data that meets specific criteria.
# Reflection 2: A series is one dimensional, while a dataframe is two dimensional.
#               df[revenue] returns a series, while df[['revenue']] returns a dataframe.
# Reflection 3: Pandas make it easier to organize and filter large data sets compared to 
#               doing it manually in Excel.

import pandas as pd

print("--- Exercise 1 ---")

df = pd.read_csv("data/retail_sales.csv")

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("--- Exercise 2 ---")
south = df[df['region'] == 'South']

print(len(south))
print(south.head())

print("--- Exercise 3 ---")
top5 = df.sort_values('revenue', ascending=False).head(5)

print(top5)

print("--- Exercise 4 ---")

big_south = df[(df['region'] == 'South') & (df['revenue'] > 10000)]

print(len(big_south))
print(big_south.head())

print("--- Exercise 5 ---")

df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())
print(df['per_unit'].mean())

print("--- Exercise 6 ---")

print(df['region'].unique())
print(df['region'].value_counts())

print("--- Exercise 7 ---")

subset = df[['region', 'product', 'revenue']]

print(subset.shape)

print("--- Exercise 8 ---")

df.to_csv('data/explored.csv', index=False)

print("File saved successfully!")