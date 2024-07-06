import pandas as pd

calories = { "day1": 420, "day2": 392, "day3": 200}

ma_var = pd.Series(calories)

print(ma_var)

# Note: The keys of the dictionary become the labels.
print(ma_var["day2"])