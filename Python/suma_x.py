import pandas as pd

data=pd.read_csv("data.csv", chunksize=500)
result=[]
for chunk in data:
   result.append(sum(chunk["x"]))

print(sum(result))

