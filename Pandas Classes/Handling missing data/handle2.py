import pandas as pd

# step 1 - Sample data frame
data ={
    "Name" : ["Atyant" , "Aditya" , None , "Prabhav" , "Farhan"] ,
    "Age" : [20 , 21 , None , 21, 22] ,
    "Salary" : [50000 , 40000 , None , 70000 , 80000],
    "Performance Score" : [85 , 90 , None , 99 , 80],
}

df = pd.DataFrame(data)
print(df)

print()

#fillna
#fillna(value , inplace=True)

# df.fillna(0 , inplace=True) -> fills 0 in every place
df['Age'].fillna(df["Age"].mean() , inplace=True)
df['Salary'].fillna(df["Salary"].mean() , inplace=True)
print(df)