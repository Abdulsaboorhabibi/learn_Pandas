# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
#
# Series is like a column, a DataFrame is the whole table.

import pandas as pd

data = {
    "calories": [450, 320, 129],
    "durations": [9, 8, 20]
}

my_var = pd.DataFrame(data)

print(my_var)

# A Pandas DataFrame is a 2-dimensional data structure, like a 2-dimensional array, or a table with rows and columns.

# Pandas use the loc attribute to return one or more specified row(s)

df = my_var
print("+++++++++++++++++ using loc ++++++++++++++++++++++++++++")
print(df.loc[0])
print(df.loc[[0]])  # when using [] the result is dataframe
print(df.loc[[0, 1]])

indexed_df = pd.DataFrame(data, index=["day1", "day2", 'day3'])

print(indexed_df)

# show with the help of loc
print(indexed_df.loc['day1'])
print(indexed_df.loc[['day2', 'day3']])

# load file into dataframe
file_df = pd.read_csv("data.csv")
print(file_df)

