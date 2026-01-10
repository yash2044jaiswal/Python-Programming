import pandas as pd
data={'Name':['yash','joy','mohan'],
      'Age':[12,23,24],
      'subject':['Math','phy','chem']
      }
df=pd.DataFrame(data)
print(df.head(2))