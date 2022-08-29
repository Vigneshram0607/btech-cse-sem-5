import random

print("Guess the Number!")
tries = 0

print("\nI'm Thinking of a Number from 1 to 10\n")
random_num = random.randint(1, 10)

is_again = True
while is_again:
    while True:
        your_guess = int(input("Your guess: "))
        tries+=1
        if random_num != your_guess:
            if your_guess > 10:
                print("", "Please Think number between 1 and 10", "", sep="*" * 10)
            elif your_guess > random_num:
                print("Too High")
            elif your_guess < random_num:
                print("Too Low")
        else:
            print(f"You Guessed it in {tries} tries.")
            break
    if input("\nWould you like to Play Again [y/n]: ").lower() == 'n':
        print("\nBye!")
        is_again = False


