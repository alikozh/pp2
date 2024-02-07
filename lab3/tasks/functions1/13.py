import random as r

def guess(x, name):
    i=0
    while True:
        i+=1

        print(" ")
        print("Take a guess.")

        a = int(input())

        if a == x:
            print(f"Good job, {name}! You guessed my number in {i} guesses!")
            break

        elif a < x:
            print("Your guess is too low.")

        else:
            print("Your guess is too big.")


name = input("Hello! What is your name? ")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")

x = r.randint(1, 20)
guess(x, name)
