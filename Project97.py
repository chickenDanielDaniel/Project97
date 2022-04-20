import random 
r = random.randint(1,100)
print("Guessing Game!")
chances = 0
while chances < 5:
    guess = int(input("Guess the number:"))
    if guess == r:
        print("Congratulations! You've guess the right number.")
        break
    elif guess < r:
        print("You've guessed a smaller number")
        chances+=1
    elif guess > r:
        print("You've guessed a bigger number.")
        chances+=1
if chances > 5:
    print("You lost, the number is", r)