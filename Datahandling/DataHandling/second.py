import pandas as pd;
data={
    'name':['yash','shiv','jhon'],
    'city':['varanasi','varanasi','varanasi'],
    'age':[12,45,23],
    'percent':[45,67,87]
}
dt=pd.DataFrame(data)
print(dt)