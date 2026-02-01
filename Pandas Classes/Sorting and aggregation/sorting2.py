import pandas as pd

# step 1 - Sample data frame
data ={
    "Name" : ["Atyant" , "Aditya" , "Asmit" , "Prabhav" , "Farhan"] ,
    "Age" : [20 , 21 , 19 , 18, 22] ,
    "Salary" : [50000 , 40000 , 30000 , 70000 , 80000],
    "Performance Score" : [85 , 90 , 75 , 99 , 80],
}

df = pd.DataFrame(data)
print(df)

print()

#df.sort_values(by=["Age", "Salary"], ascending=True, inplace=True) -> for sorting multiple columns
df.sort_values(by=["Age", "Salary"] , ascending=[True,True] , inplace=True)
print("Sorting ultiple columns in ascending order")
print(df)