import random

def get_difficulty():
    while True:
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
        if difficulty == "easy":
            return 10
        elif difficulty == "medium":
            return 7
        elif difficulty == "hard":
            return 5
        else:
            print("Invalid input. Please enter 'easy', 'medium', or 'hard'.")

def get_guess():
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_game():
    attempts_allowed = get_difficulty()
    target_number = random.randint(1, 100)
    attempts_left = attempts_allowed
    
    while attempts_left > 0:
        guess = get_guess()
        if guess < target_number:
            print(f"Too low! You have {attempts_left - 1} attempts left.")
        elif guess > target_number:
            print(f"Too high! You have {attempts_left - 1} attempts left.")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly.")
            break
        attempts_left -= 1

    if attempts_left == 0:
        print(f"Sorry, you've run out of attempts. The number was {target_number}.")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
