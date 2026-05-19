num=int(input("Enter a number:"))
for i in range(2,num):
    if(num%i==0):
        print("is not prime")
        break
else:
    print("prime")
