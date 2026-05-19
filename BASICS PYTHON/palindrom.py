num=int(input("Enter a number:"))
rev=0
orignal=num
while(num >0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)
if(rev==orignal):
    print("Is palindrom")
else:
    print("not palindrom")
