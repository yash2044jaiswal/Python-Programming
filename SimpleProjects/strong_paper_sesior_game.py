import random

computer=random.SystemRandom("r","p","s")
while True:
    user=input("enter your charecter:")
    if(computer==user):
        print("draw")
        break
    elif(computer=="r" and user=="p"):
        print("user winn!!")
    elif(computer=="r" and user=="s"):
        print("user win")
    elif(computer=="s" and user=="p"):
        print("computer winner!!")
print("GAME OVER!!")
    
