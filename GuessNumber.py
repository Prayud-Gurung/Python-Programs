import random
num = random.randint(0,100)

win = False

print("Can you guess the number?")

while(not win):
    guess = int(input("Your guess: "))
    if(guess > num):
        print("Try Lower")
    elif(guess < num):
        print("Try Higher")
    else:
        win = True

print("The correct answer was: ", num)
print("Congratulations")
      


