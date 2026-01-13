import random,math

num = int(random.random())


while True : #bro here you always want to get the input when number is not correct and you cannot put num !=n because you dont have the n 
    n = int(input("Guess the number :"))
    if n == num:
        print(f"Bravo!!!You guessed it {num} is the number")
    elif n > num :
        print("guess was too big")
    else:
        print("Guess was too small")




    