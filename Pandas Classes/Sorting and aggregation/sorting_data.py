#Sorting data
#sorting data 1 column sort_values()
#df.sort_values(by="Column_Name", True / False, inplace=True) #True -> for ascending order.  False -> for descending order.
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

df.sort_values(by="Age" , ascending=False  , inplace=True)
print("Sorting Age in descending order")
print(df)
