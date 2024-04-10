import random

score=0
tries=0

def create_ex():
    global score
    global tries
    tries +=1
    num1=random.randint(0,10)
    num2=random.randint(0,10)
    sum=num1+num2
    answer = int(input(f"{num1}+{num2}= "))
    if answer == sum:
        score+=1
        print(f"SCORE: {score}")
    else:
        print("Sorry...")

while score <10:
    create_ex()

print(f"YOU DID IT in {tries} TRIES!")

