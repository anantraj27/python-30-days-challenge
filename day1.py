import random
guess_number=random.randint(1,11)
while True:
    
    num =int(input("enter a number from 1 to 10 : "))
    if (guess_number==num):
        print("the door is open")
     
        break
    else:
        if (guess_number < num):
            print("input number is heigher than  Guess_number")
        else:
            print("enput number is lower")    
        print("wait for your luck")
        
print("you are a lucky man!....😁")


