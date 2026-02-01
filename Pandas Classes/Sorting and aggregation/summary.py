#df["Salary"].mean()
#df["Salary"].sum()
#df["Salary"].max()
#df["Salary"].min()
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

avg_salary = df["Salary"].mean()
total_salary = df["Salary"].sum()
max_salary = df["Salary"].max()
min_salary = df["Salary"].min()
print("Average salary: " , avg_salary)
print("Total salary: " , total_salary)
print("Max salary: " , max_salary)
print("Min salary: " , min_salary)