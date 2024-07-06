import pandas as pd

my_data = pd.read_csv("data.csv")
print(my_data.to_string()) # .to_string() is used to print the entire dataframe
# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
print("====================================================")
my_large_date = pd.read_csv("largDate.csv")
print(my_large_date)
print("====================================================")

# if you want to print all the date
print("====================================================")
# print(my_large_date.to_string())
