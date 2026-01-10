# operating data from using of numpy array
import pandas as pd
import numpy as np
npArray=np.array(
    [
        ['dev','anil','yash'],
        ['Delhi','vns','ayodhya'],
        [23,23,25],
        [86.5,90.5,95.7]
    ]
)
data={
    'name':npArray[0],
    'city':npArray[1],
    'age':npArray[2],
    'percentage':npArray[3]

}
df=pd.DataFrame(data)
print(df)