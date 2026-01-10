import pandas as pd 
df = pd.DataFrame({'A':[10,20,30], 'B':[15,25,35],'C':[5,10,15]}) 
print(df.apply(sum, axis=0))
