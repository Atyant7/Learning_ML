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

#.loc[] -> can access and modify specific cell
#df.loc[row_index , "Column_name"] = new_value
df.loc[0 , "Salary"] = 55000
print(df)