from random import randint

# Ali Alzurufi
# This program will imitate rock , paper, scissors

def main():
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    wins = 0
    losses = 0

    while True:

        try:
            # Get user Input
            userInput = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors, or 4 to Exit: "))
            print()

            # allow user to exit
            if userInput == 4:
                break

            # Assign random number between 1-3 to the computer
            compChoice = randint(1, 3)

            #print out choices
            print(f"Your choice: {choices[userInput]} \nComputer choice: {choices[compChoice]}")
            print()

            # notify if there is a draw 
            if userInput == compChoice:
                print("It's a draw! Starting again.")
                print()

            # Check who wins and increment
            elif str(userInput) + str(compChoice) in ["13", "21", "32"]:
                print("You Win!")
                print()
                wins += 1

            else:
                print("You Lose.")
                print()
                losses += 1

            # exception when there is invalid input
        except:
            print("Invalid choice. Try again")
            continue

    # print out results
    print()
    print(f"Number of wins: {wins}")
    print(f"Number of losses: {losses}")
    print()
    print("Thanks for playing.")


main()