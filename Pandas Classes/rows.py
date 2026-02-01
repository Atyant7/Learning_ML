# head() tail()
# head(n) -> give you first n of rows and if n is not given then by default it will give you 5 rows
# tail(n) -> give you last n of rows and if n is not given then by default it will give you 5 rows from the last

import pandas as pd

df = pd.read_json("pseudo_data.json")

print("Display 10 rows of first")
print(df.head(10))
print()
print("Display 10 rows of last")
print(df.tail(10))

print()

print("Display by default 5 rows of first")
print(df.head())
print()
print("Display by default 5 rows of last")
print(df.tail())