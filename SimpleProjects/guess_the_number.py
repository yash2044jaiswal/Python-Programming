import random

randNum=random.randint(1,1000)

while True:
    usernumber=eval(input("guess the number: or Quit:"))
    if(usernumber=="Quit"):
        break
    if(usernumber==randNum):
        print("success:correct Guess!!")
        break
    elif(usernumber>randNum):
        print("your number was too big,take a smaller guess..")
    elif(usernumber<randNum):
        print("your number was too small,take a bigger guess.. ")
    else:
        print("invailed input")
print("--GAME OVER---")