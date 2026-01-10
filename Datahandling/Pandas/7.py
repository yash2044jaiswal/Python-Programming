import pandas as pd
df = pd.DataFrame({'Name':['A','B','C'], 'Score':[90,85,88]})
df.set_index('Name', inplace=True) 
print(df)
