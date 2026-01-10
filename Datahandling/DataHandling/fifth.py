# import pandas as pd
# data={'Name':pd.Series(['dev','jay','kriti','raj','neha'],index=['first','second','third','fourth','fifth'],),
#        'Age':pd.Series([12,22,22,22,22] ,index=['first','second','third','forth','fifth'],),
#        'city':pd.Series(['vns','delhi','mumbai','kolkata','lukhnow'],index=['first','second','third','forth','fifth'])
#       }
# df=pd.DataFrame(data)
# print(df)



#for missing and cases
import pandas as pd
data={'Name':pd.Series(['dev','jay','kriti','raj','neha'],index=['seventh','second','third','fourth','fifth'],),
       'Age':pd.Series([12,22,25,26,45] ,index=['first','second','third','forth','fifth'],),
       'city':pd.Series(['vns','delhi','mumbai','kolkata','lukhnow'],index=['first','second','third','forth','fifth'])
      }
df=pd.DataFrame(data)

colom=df.columns.tolist()
# print(colom)

print(df.head)

missing=df.isnull().sum()
print(missing)


avg=df['Age'].mean()
print("average of age is:",avg)