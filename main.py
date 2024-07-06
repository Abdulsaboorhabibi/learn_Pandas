import sys

import pandas as pd
from pandas import Series

# pd series: A Pandas Series is like a column in a table.

a = [1, 7, 2]
series = pd.Series(a)
print(series)
# get series with labels
print(series[0])

# create labels: customized
customized_series: Series = pd.Series(a, index=["x", "y", "z"])
print(customized_series)

# When you have created labels, you can access an item by referring to the label.
print(customized_series["z"])

# check pd versions
# print(pd.__version__)
# print(sys.version)
# first program
# my_data_set = {
#     "cars": ["BMW", "Volvo", "Ford"],
#     "passings": [3, 7, 2]
#     }
# my_var = pd.DataFrame(my_data_set)
# print(my_var)