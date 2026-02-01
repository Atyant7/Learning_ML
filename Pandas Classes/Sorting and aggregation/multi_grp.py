import pandas as pd

# step 1 - Sample data frame
data ={
    "Name" : ["Atyant" , "Aditya" , "Asmit" , "Prabhav" , "Farhan"] ,
    "Age" : [22 , 21 , 21 , 18, 22] ,
    "Salary" : [70000 , 40000 , 40000 , 70000 , 80000],
    "Performance Score" : [80 , 90 , 75 , 90 , 80],
}

df = pd.DataFrame(data)
print(df)

print()
multi_grp = df.groupby(["Age" , "Performance Score"])["Salary"].sum()
print(multi_grp)