import pandas as pd
data=pd.DataFrame({
    'A':[12,13,14],
    'B':[14,15,16]
})
print(data.apply(sum,axis=0))
