import pandas as pd 
 

di={
    "name":["arul","john","priya"],
    "city":["ch","hyd","bnglor"],
    "role":["dev","HR","test"]
}

li=[["arul","dev","chnai"],["john","test","hyd"]]
df=pd.Dataframe(di) # df=pd.DataFrame(li,columns=["name","city","role"])
print(df)