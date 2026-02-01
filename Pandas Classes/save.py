import pandas as pd

data ={
    "Name" : ["Atyant" , "Aditya" , "Asmit" , "Prabhav" , "Farhan"] ,
    "Age" : [20 , 21 , 21 , 21, 22] ,
    "City" : ["Prayagraj" , "Prayagraj" , "Prayagraj" , "Prayagraj" , "Prayagraj"]
}

df = pd.DataFrame(data) # .DataFrame -> creates a dataframe and stored in df . Aur print kroge to dekhoge indexing bhi de dega jo ki humne mention nhi kiya hai data mein.Usko hatane ka bhi jugaad hai
print(df)

df.to_csv("Created.csv" , index = False) # .to_csv -> convert any file format into csv file and make a new csv file whose name is mentioned between the brackets . index = Flase -> remove the index from the file

df.to_excel("Created.xlsx" , index = False) # .to_excel -> convert any file format into excel file and make a new excel file whose name is mentioned between the brackets . index = Flase -> remove the index from the file

df.to_json("Created.json" , index = False) # .to_json -> convert any file format into json file and make a new json file whose name is mentioned between the brackets . index = Flase -> remove the index from the file