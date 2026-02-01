import pandas as pd

# step 1 - Sample data frame
data ={
    "Name" : ["Atyant" , "Aditya" , "Asmit" , "Prabhav" , "Farhan"] ,
    "Age" : [20 , 21 , 21 , 21, 22] ,
    "Salary" : [50000 , 40000 , 30000 , 70000 , 80000],
    "Performance Score" : [85 , 90 , 78 , 99 , 80],
}

df = pd.DataFrame(data)

high_salary = df[df["Salary"] > 50000]
print("Employee with salary greater than 50000")
print(high_salary)

print()

#filtering rows salary>50k and age>21
filtered = df[(df['Age'] > 21) & (df['Salary'] > 50000)]
print("Employee with age > 21 and salary > 50000")
print(filtered)

print()

#using or condition
fil = df[(df['Age'] > 20) | (df['Performance Score'] > 80)]
print("Employees older than 20 and performance score > 80")
print(fil)