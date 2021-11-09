# Guessing Game with While loop, if and else loop and variables

secret_word = "february"  # This will store the correct answer
guess = ""  # This will store the user input
guess_count = 1  # This will store the number of used guesses
guess_limit = 4  # This will store the total number of try user can have
out_of_guess = False  # This will tell if user still has guesses left

print("All has 30 or 31 but only I don't")
while guess != secret_word and not (out_of_guess):  # This is the condition to run the loop
    print("Guesses left= " + str(guess_limit - guess_count))  # This will show the number of guesses left
    if guess_count < guess_limit:  # This will check of Guesses are left or not
        guess = input("Enter your guess number " + str(guess_count) + ": ")  # This will take the ueser guess and store it in the guess variable
        guess_count = guess_count + 1  # This will give the guess count left
    else:
        out_of_guess = True  # This will execute if all guesses are used

if out_of_guess:
    print("Out of Guesses, You Lost the game!!!")
else:
    print("You won the game!!!")
