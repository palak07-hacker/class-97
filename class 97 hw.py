import random
print("NUMBER GUESSING GAME")

number = random.randint(1,9)

chances = 0
print("guess a number between 1 to 9")

while chances < 5:
    guess = int(input("enter your guess:-"))

    if guess == number:
        print("Congratulations!! U Won")
        break

    elif guess < number:
        print("Ur guess was too low:guess a number higher than", guess)

    else:
        print("Ur guess was too high:guess a number lower than", guess)

    chances = chances + 1

if not chances < 5:
    print("U LOSE. The number is", number)
