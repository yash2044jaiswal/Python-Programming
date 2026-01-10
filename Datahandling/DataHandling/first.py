import pandas as pd
data=[
    ['DEV','MUMBAI','27','89.5'],
    ['ANIL','KOLKATA',21,87.9],
    ['KRITI','DELHI',21,78.9],
]
DT=pd.DataFrame(data,columns=['NAME','CITY','AGE','PERCENT'])
print(DT)