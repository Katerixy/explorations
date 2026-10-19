import random
def main():
    print("--Guessing Game-- \nI picked a number between 1 and 100. Input your guess!")
    number = random.randint(1, 100)
    guess_amount = 0
    true_guess_amount = 0
    answer = ""
    while not answer == "Correct!":
        guess = input()
        check = checker(number, guess)
        answer = check[0]
        valid_guess = check[1]
        guess_amount += 1
        if valid_guess:
            true_guess_amount += 1
        print(answer)
    print(f"It took you: {guess_amount} guesses (or {true_guess_amount} real guesses)")
def checker(number, guess):
    try:
        guess = int(guess)
    except:
        answer = "That's not a valid number... try again"
        valid_guess = False
    else:
        valid_guess = True
        if guess == number:
            answer = "Correct!"
        elif guess < number:
            answer = "Too low! Try again."
        elif guess > number:
            answer = "Too high! Try again."
    return (answer, valid_guess)

main()



