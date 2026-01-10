with open("one.txt","r")as f:
     data=f.read()
     print(data)

with open("one.txt","w")as f:
     f.write("new data")
         