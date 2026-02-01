import pandas as pd

# step 1 - Sample data frame
data ={
    "Name" : ["Atyant" , "Aditya" , "Asmit" , "Prabhav" , "Farhan"] ,
    "Age" : [20 , 21 , 21 , 21, 22] ,
    "Salary" : [50000 , 40000 , 30000 , 70000 , 80000],
    "Performance Score" : [85 , 90 , 78 , 99 , 80],
}

df = pd.DataFrame(data)
print(df)

print()

# use square brackets df["Column_name"] = some_data
df["Bonus"] = df["Salary"] * 0.1
print(df)

print()

#using insert()
#df.insert(location , "Column_name" , some_Data)
df.insert(0 , "Employee_ID" , [10,20,30,40,50])
print(df)