#exercise 1
import pandas as pd
df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

#Exercise 2

south = df[df['Region'] == 'South']

print(len(south))
print(south.head())

#Exercise 3

top_5 = df.sort_values('revenue', ascending=False).head(5)
print(top_5)

#exercise 4

big_south = df[(df['Region'] == 'South') & (df['revenue'] > 1000)]

#exercise 5

df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())

#exercise 6

print(df['Region'].unique())
print(df['Region'].value_counts())

#exercise 7

df_subset = df[['Region', 'Product', 'Revenue']]

print(df_subset.shape)

#exercise 8

df.to_csv('data/explored.csv', index=False)


