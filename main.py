import random
# MOVIE NAME
movies=['anand','drishyam','golamal','kgf','jersy','dangal','nayak','beast','interseller',"avatar", "titanic", "star wars", "jurassic park", "the lion king"]
def guess_movie():
    pl1 = input( 'ENTER YOUR NAME').upper()
    # Pick a random movie from the list
    movie = random.choice(movies)
    # Create a list of underscores to represent the movie name
    blanks = ["_"] * len(movie)
    # Keep track of guessed letters
    guessed_letters = []
    # Set the number of allowed guesses
    num_guesses = 8

    while num_guesses > 0:
        # Print the current status of the game
        print('You have predicted till now - '," ".join(blanks))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Guesses left: {num_guesses}")

        # Get a letter from the player
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in movie:
            # Update the blanks list with the guessed letter
            for i in range(len(movie)):
                if movie[i] == guess:
                    blanks[i] = guess
            print(" ".join(blanks))
            print("Correct!")
            # Check if the player has won
            if "_" not in blanks:
                print(f"Congratulations {pl1}, you guessed the movie!")
                return
        else:
            print("Incorrect.")
            num_guesses -= 1

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

    print(f"Sorry {pl1}, you ran out of guesses. The movie was {movie}.")




guess_movie()
