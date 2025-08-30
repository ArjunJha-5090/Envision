import random  # Import the random module to let the computer make random choices


# Function to display game instructions for the player
def display_instructions():
    print("Welcome to Rock, Paper, Scissors!")  # Greet the player
    print("Instructions:")  # Tell the player what to do
    print("- Enter 'Rock', 'Paper', or 'Scissors' to play.")  # Your main choices
    print("- Enter 'Exit' to stop playing.")  # How to quit the game
    print("")  # Add a blank line for better readability


# Function to get player's choice with input validation
def get_player_choice():
    valid_choices = ['rock', 'paper', 'scissors', 'exit']  # List of options
    while True:  # Loop until the player enters a valid choice
        choice = input("Enter your choice (Rock, Paper, Scissors) or 'Exit' to quit: ").strip().lower()
        # 'strip().lower()' makes sure we accept input regardless of case or extra spaces
        if choice in valid_choices:  # If the choice is valid
            return choice  # Send it back to the main game loop
        else:
            print("Invalid input. Please enter 'Rock', 'Paper', 'Scissors', or 'Exit'.")  # Warn if invalid


# Function for the computer to randomly pick a move
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])  # Randomly choose one


# Function to decide who wins based on the choices
def determine_winner(player, computer):
    if player == computer:  # If both choices are the same
        return 'Tie'  # It's a tie!
    elif (player == 'rock' and computer == 'scissors') or \
            (player == 'scissors' and computer == 'paper') or \
            (player == 'paper' and computer == 'rock'):
        # These are the conditions where the player wins
        return 'Player'  # Player wins!
    else:
        # All other cases mean the computer wins
        return 'Computer'


# Function to show the results of each round and update scores
def display_results(player_choice, computer_choice, winner, scores):
    print(f"\nYou chose: {player_choice.capitalize()}")  # Show what the player chose
    print(f"Computer chose: {computer_choice.capitalize()}")  # Show computer's choice
    # Check who won and print the result accordingly
    if winner == 'Tie':
        print("It's a tie!")  # Both choices are same
    elif winner == 'Player':
        print("You win this round!")  # Player's choice beats computer's
        scores['player_wins'] += 1  # Increment player's win count
    else:
        print("Computer wins this round!")  # Computer's choice beats player's
        scores['computer_wins'] += 1  # Increment computer’s win count
    # Show current scores after each round
    print(f"Current Scores -> You: {scores['player_wins']} | Computer: {scores['computer_wins']}\n")


# Main game function
def main():
    scores = {'player_wins': 0, 'computer_wins': 0}  # Initialize scores at the start
    display_instructions()  # Show instructions once at the beginning

    while True:  # Keep playing until user chooses to exit
        player_choice = get_player_choice()  # Get the player's choice
        if player_choice == 'exit':  # If player wants to stop
            print("Thanks for playing! Final scores:")  # Farewell message
            print(f"You: {scores['player_wins']}")  # Show total wins
            print(f"Computer: {scores['computer_wins']}")  # Show total losses
            break  # Exit the game loop, ending the game
        computer_choice = get_computer_choice()  # Computer makes a random move
        winner = determine_winner(player_choice, computer_choice)  # Decide who won
        # Show results and update scores
        display_results(player_choice, computer_choice, winner, scores)


# This is needed to run the game if this file is executed directly
if __name__ == "__main__":
    main()
