import pandas as pd 

df= pd.read_csv("data/CSO.3.1.csv")
for index,data in df.iteritems():
    print(index)
    df[index]=df[index].str.replace("<","")
    df[index]=df[index].str.replace(">","")
df.to_csv("data/newData.csv")

