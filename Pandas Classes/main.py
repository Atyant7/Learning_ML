import pandas as pd

# Read data from CSV file into a dataframe
df = pd.read_csv("pseudo_data.csv" , encoding = "latin1") # any encoding can be passed    1. utf-8   2. latin1 . Mera without encoding pass kiye bhi chal gya tha

print(df)

print()

# Read data from CSV file into a dataframe
ed = pd.read_excel("pseudo_data.xlsx")

print(ed)

print()

# Read data from json file into a dataframe
jd = pd.read_json("pseudo_data.json")

print(jd)

#gcsfs -> library helps in reading data from google cloud