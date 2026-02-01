import pandas as pd

# step 1 - Sample data frame
data ={
    "Name" : ["Atyant" , "Aditya" , "Asmit" , "Prabhav" , "Farhan"] ,
    "Age" : [22 , 21 , 21 , 18, 22] ,
    "Salary" : [50000 , 40000 , 30000 , 70000 , 80000],
    "Performance Score" : [85 , 90 , 75 , 99 , 80],
}

df = pd.DataFrame(data)
print(df)

print()

grouped = df.groupby("Age")["Salary"].sum()
print(grouped)