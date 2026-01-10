import pandas as pd 
data = {'x':[1,2,3,4], 'y':[5,6,7,8]} 
df = pd.DataFrame(data)
df['sum'] = df['x'] + df['y']
print(df)
