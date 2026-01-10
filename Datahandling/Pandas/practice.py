# create dataframe by using dictionary

import pandas as pd
data={
    'Name':["Yash","Harh","shiv"],
    'roll':[101,102,103],
    'Age':[18,19,20]
}
df=pd.DataFrame(data)
print(df)



# creating dataframe by using array
# import pandas as pd
# data=[
#     ['Yash',13,14],
#     ['Harsh',12,23],
#     ['Shiv',20,15]
# ]
# df=pd.DataFrame(data,columns=['Name','Age','Marks'])
# print(df)


# creating dataframe of list of dictionari

# import pandas as pd
# data=[
#     {'Name':'Yash','Age':34,'Marks':152},
#     {'Name':'Harsh','Age':4,'Marks':142},
#     {'Name':'SHiv','Age':24,'Marks':132 }
# ]
# df=pd.DataFrame(data)
# print(df)




# by numpy
# import numpy as np
# import pandas as pd
# data=np.array([
#     [102,12000],
#     [103,20000],
#     [103,90000]
# ])
# df=pd.DataFrame(data,columns=['EmpID','Salery'])
# print(df)




