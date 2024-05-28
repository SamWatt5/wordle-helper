file = open("../wordle-answers-alphabetical.txt", "r")
solutions = []
for line in file:
    #print(line.strip())
    solutions.append(line.strip())


def instructions():
    print("To use this wordle solver, please enter each guess and how close you got, using 'g' for a green letter,")
    print("'y' for a yellow letter letter, or 'b' for a black letter,")
    print("i.e. if the final word was 'nicer' and you guessed 'tacit', you would enter 'tacit' then 'bbgyb'.")


def getGuesses():
    userGuesses = []
    i = 0
    while i < 5:
        curGuess = input("Please enter your guess " + str(i + 1) + ", or leave blank if entered all guesses:")

        while len(curGuess) < 5 or len(curGuess) > 5:
            curGuess = input("Please enter your guess " + str(i + 1) + ", or leave blank if entered all guesses:")

        if curGuess == "":
            break

        userGuesses.append(curGuess)
        i += 1

    

    return userGuesses


instructions()
guesses = getGuesses()
