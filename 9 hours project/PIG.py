import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

while True:
    players = input("Enter the number of players(2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]
'''
above is a list, an array to store the player scores. It puts "0" for every single player. "_" doesnt matter, a variable is needed there.
"range" will loop "the no. of players" time(s) that we have.
'''

while max(player_scores) < max_score:

    for player_idx in range(players):
        # "player_idx" represents the current player. In this for loop, we simulate one player's turn till it ends.
        print("\nPlayer", player_idx + 1, " your turn has just started!")
        # "\n" is for a line break so there a bit of a separation when te turn starts.
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0
        # The above code basically let's starts the turn of the player. Then below, the turn is simulated.

        while True:
            should_roll = input("Would you like to roll? (y)? ")
            if should_roll.lower() != "y":
                break
                # Above, the player chooses to roll or not.

            value = roll()
            if value == 1:
                print("You rolled 1! Turn done!")
                current_score = 0
                break
                # Above is what happens if they roll a one.
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)
            # Above, if they roll any number but one.
            # The player is told the value rolled & the total sum as the value is added to their current score.
            # We get out the while loop when player refuses to roll or gets 1.

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])
        # Here, we print out the total score at the end of the loop(a turn)

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)
# Here once a player gets to 50, we make it so everyone ends the round. Whoever has the highest number wins.