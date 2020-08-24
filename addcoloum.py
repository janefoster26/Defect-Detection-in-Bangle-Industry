import pandas as pd


data =pd.read_csv("dataset.csv")

Type=pd.Series([])
for i in range(len(data)):
    if(i<1292):
        Type[i]=2
    elif(i<2513):
        Type[i]=1
    else:
        Type[i]=0
data.insert(0,"",Type)
data.to_csv("dataset.csv")