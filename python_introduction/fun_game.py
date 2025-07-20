import random #generates a random number

while True:
    secret_number = random.randint(1, 10) #the random ranges between 5 and 10
    guess = int(input("Guess a number between 1 and 10: ")) #prompts the user to guess a number and converts to an interger

    match guess: #matches the guessed number with the secret number
        case n if n == secret_number: 
            print("Congratulations, you guessed it!")
        case n if n > secret_number:
            print("Oops, your guess is a bit high. Try again!")
        case n if n < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")

    play_again = input("Do you want to play again? (yes/no): ").lower() #ask the user if they are willing to continue playing
    if play_again != "yes":
        print("Thanks for playing!")
        break

          




