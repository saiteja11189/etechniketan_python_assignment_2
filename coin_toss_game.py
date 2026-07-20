import random

print("Welcome to the Simple Coin Toss Game!")

while True:
    guess = input("Guess 'heads' or 'tails': ").strip().lower()
    
    # Input validation
    while guess not in ["heads", "tails"]:
        print("Error: Invalid choice! Please type 'heads' or 'tails'.")
        guess = input("Guess 'heads' or 'tails': ").strip().lower()
        
    # Simulate coin toss
    coin_result = random.choice(["heads", "tails"])
    print(f"Coin shows: {coin_result}")
    
    # Check guess
    if guess == coin_result:
        print("You guessed it right!")
    else:
        print("Wrong guess!")
        
    # Ask if user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
