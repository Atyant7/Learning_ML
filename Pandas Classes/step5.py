import pandas as pd

data ={
    "Name" : ["Atyant" , "Aditya" , "Asmit" , "Prabhav" , "Farhan"] ,
    "Age" : [20 , 21 , 21 , 21, 22] ,
    "Salary" : [50000 , 40000 , 30000 , 70000 , 80000],
    "Performance Score" : [85 , 90 , 78 , 99 , 80],
}

df = pd.DataFrame(data)

#display the data frame
print("Sample Dataframe")
print(df)

print()

print("Names (single column returns series)")
name = df["Name"]
print(name)

print()

subset = df[["Name" , "Salary"]]
print("Subset with Name and Salary")
print(subset)

print()

