"""
combining dataframe either vertically(row-wise) or horizontally(col-wise)
pd.concate([df1,df2], axis=0, ignore_index=True)
axis = 0 -> means row wise
axis = 1 -> means column wise
ignore_index=True -> reset the index of combined dataframe
"""

import pandas as pd

df_Region1 = pd.DataFrame({
    'Customer_ID':[1,2],
    'Name':['Gopal','Raju']
})

df_Region2 = pd.DataFrame({
    'Customer_ID':[3,4],
    'Name':['Shyam','Baburai']
})

#Concatinate vertically(row-wise)
df_concat = pd.concat([df_Region1 , df_Region2] , ignore_index=True)
print("Concatinate vertically")
print(df_concat)

print()

df_concat = pd.concat([df_Region1 , df_Region2] ,axis = 1 , ignore_index=True)
print("Concatinate Horizontally")
print(df_concat)