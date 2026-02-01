import pandas as pd

df = pd.read_json("pseudo_data.json")

print("Display the info of data set")
print(df.info())

print()

data ={
    "Name" : ["Atyant" , "Aditya" , "Asmit" , "Prabhav" , "Farhan"] ,
    "Age" : [20 , 21 , 21 , 21, 22] ,
    "City" : ["Prayagraj" , "Prayagraj" , "Prayagraj" , "Prayagraj" , "Prayagraj"]
}

dataf = pd.DataFrame(data)

print("Analysing small data set")
print(dataf.info())