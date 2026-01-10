import pandas as pd
import numpy as np

data=np.array([
    [102,34000],
    [103,89000],
    [104,89000]
])
df=pd.DataFrame(data,columns=['EmpId','Salery'])
print(df)