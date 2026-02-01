import pandas as pd

# step 1 - Sample data frame
data ={
    "Name" : ["Atyant" , "Aditya" , 'Asmit' , "Prabhav" , "Farhan"] ,
    "Age" : [20 , 21 , None , 21, 22] ,
    "Salary" : [50000 , 40000 , None , 70000 , 80000],
    "Performance Score" : [85 , 90 , None , 99 , 80],
}

df = pd.DataFrame(data)
print(df)

print()

df.interpolate(method="linear", axis = 0, inplace=True)

