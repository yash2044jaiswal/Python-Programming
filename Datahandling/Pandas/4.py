import pandas as pd 
df = pd.DataFrame({'A':[10,20,30,40], 'B':[5,10,15,20]})
print(df[df['A'] > 20])
