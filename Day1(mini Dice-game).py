import random

#Function to generate a random number between 1 and 6, simulating a dice roll
def roll():                                       
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

#Loop to decide the number of players, ensuring it is between 2 and 4
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)      #converts string to int
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50           # The score needed to win the game
player_scores = [0 for _ in range(players)]   # Initialize player scores to 0

# Main game loop, continues until a player reaches the max_score
while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        #Loop for rolling the dice during a player's turn
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:          #If the player rolls a 1, their turn ends
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])
#Determine the winner
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)