# question 1- A boolean filter checks specific condition agienst every row in a dataframe and returns a series of True or False values. It is used to filter data based on certain criteria.
#question 2- df['revenue'] returns a 1-dimensional pandas series and df[['revenue']] returns a 2-dimensional pandas dataframe. The difference is that the first one is a series and the second one is a dataframe.
#question 3- instead of manually clicking through data filters, formulas and pivot tables, pandas allows you to perform data manipulation and analysis programmatically, which is faster, more efficient, and reproducible.

#exercise 1
import pandas as pd
df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

#Exercise 2

south = df[df['region'] == 'South']

print(len(south))
print(south.head())

#Exercise 3

top_5 = df.sort_values('revenue', ascending=False).head(5)
print(top_5)

#exercise 4

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

#exercise 5

df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())

#exercise 6

print(df['region'].unique())
print(df['region'].value_counts())

#exercise 7

df_subset = df[['region', 'product', 'revenue']]

print(df_subset.shape)

#exercise 8

df.to_csv('data/explored.csv', index=False)


