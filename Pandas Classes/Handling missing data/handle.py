import pandas as pd

# step 1 - Sample data frame
data ={
    "Name" : ["Atyant" , "Aditya" , None , "Prabhav" , "Farhan"] ,
    "Age" : [20 , 21 , None , 21, 22] ,
    "Salary" : [50000 , 40000 , None , 70000 , 80000],
    "Performance Score" : [85 , 90 , None , 99 , 80],
}

df = pd.DataFrame(data)
print(df)

print()

#dropna() -> kisi bhi column ya row ke missing value ko hta sakte hai means delete klr skte hai
#df.dropna(axis = 0 , inplace=True) #axis = 0 means rows ki values ko udana  aur  axis=1 means column ki values ko udana

df.dropna(inplace=True) #Remove al the value which is None aur NaN
print(df)