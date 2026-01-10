import pandas as pd
data=[
    ['yash',45,67],
    ['harsh',45,22],
    ['shiv',67,12]
]
df=pd.DataFrame(data, columns=['Name' ,'Marks1' ,'Marks2'])
print(df)
