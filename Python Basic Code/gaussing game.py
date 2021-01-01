from random import randint
gassnumber=int(input("enter gauss between from 1 to 5:"))
randnum=randint(1,5)
if gassnumber==randnum:
    print("you have won")
else:
    print("you have loss")
    print("random number was",randnum)