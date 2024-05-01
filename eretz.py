import random

letters = ['A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
score = 0
start_game = input("Start or End? ")

while start_game != "end":

    if start_game == "start":
        print("AAAAALEFFFFFFF")
        user_stop = input("")
        while user_stop != "stop":
            user_stop = input("")   
        random_letter = random.choice(letters)
        city_name = input(f"Write a city that starts with {random_letter}: ")
        if city_name.upper().startswith(random_letter):
            print("You did it!")
            score+=1
        else:
            print("Try again...")
            
    start_game = input("Start or End? ")

print(f"Game Over!")
print(f"Score: {score}")