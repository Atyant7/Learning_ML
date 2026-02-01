#pd.merge(df1,df2,on="Column_name", how="type_of_join")
import pandas as pd

#Custome dataframe
df_customer = pd.DataFrame({
    'Customer_ID':[1,2,3],
    'Customer_Name':['Ramesh', ' Suresh' , 'Kalpesh']
})

#Order dataframe
df_orders = pd.DataFrame({
    'Customer_ID':[1,2,4],
    'Order_Amount':[250 , 350 , 450]
})

#merge
df_merge = pd.merge(df_customer , df_orders , on="Customer_ID" , how="inner") #inner -> intersection
print("Inner join")
print(df_merge)

print()

df_merge = pd.merge(df_customer , df_orders , on="Customer_ID" , how="outer") #outer -> union and if the value not found then it will fill it with NaN
print("Outer join")
print(df_merge)

print()


df_merge = pd.merge(df_customer , df_orders , on="Customer_ID" , how="left") #left -> jitni bhi left wale dataframe mein values hai sab rakhega aur missing wali par NaN likh dega 3right -> same waise hi kaam karta hai jaise left krta.
print("Left join")
print(df_merge)

print()

#cross -> cartesian product of dataFrame