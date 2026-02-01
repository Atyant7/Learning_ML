# 1- How big is your data set?
# 2- Names of the columns?
# shape -> is an attribute and return tupples with 2 values first one is no. of rows and second one is no. of columns
# columns -> return name of the column and can also change any column name.

import pandas as pd

data ={
    "Name" : ["Atyant" , "Aditya" , "Asmit" , "Prabhav" , "Farhan"] ,
    "Age" : [20 , 21 , 21 , 21, 22] ,
    "Salary" : [50000 , 40000 , 30000 , 70000 , 80000],
    "Performance Score" : [85 , 90 , 78 , 99 , 80],
}
df = pd.DataFrame(data)
print(f'Shape: {df.shape}')
print(f'Column Names: {df.columns}')