# import numpy as np

# n1=np.array([12,23,24])
# n2=np.array([12,23,24])

# # print(np.sum([n1,n2]))

# # print(np.sum([n1,n2],axis=0))

# print(np.sum([n1,n2],axis=1))


# # scaler operation

# # n1=n1+1
# # n1=n1*2
# # n1=n1/2
# n1=n1-2
# print(n1)


import numpy as np
from matplotlib import pyplot as plt
x=np.array([1,2,3,4,5])
y=x*2
plt.plot(x,y,color='blue',linewidth='5',linestyle='-')
plt.show()
# plt.savefig("plot.png")