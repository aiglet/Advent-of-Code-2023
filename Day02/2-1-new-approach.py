# Get the data
data = open("fulldata.txt")

# Split it into lines - each game is a game
lines = data.readlines()

# Set the comparisons

redmax = 12
greenmax = 13
bluemax = 14
game_tot = 0

for game in lines:

    # Is the game possible to play?
    game_poss = True

    # Split the game into the game ID and the draws
    game_id, draws = game.strip().split(": ")

    # Get the game number alone
    game_id = int(game_id.split(" ")[1])

    # Split the draws into separate items
    draws = draws.split("; ")

    # Go through each set of plays
    for playset in draws:

        # Can we do this set of plays?
        plays_poss = True

        # Split them into individual plays
        plays = playset.split(", ")

        # Go through each play individually
        for play in plays:

            # Split the play into the number and color of the blocks involved
             play_num = int(play.split(" ")[0])
             play_col = play.split(" ")[1]

            # If any of the plays are impossible, set the play to impossible
             if play_col == "red" and play_num > redmax:
                 plays_poss = False
             elif play_col == "blue" and play_num > bluemax:
                 plays_poss = False
             elif play_col == "green" and play_num > greenmax:
                 plays_poss = False

        # If any of the plays are impossible, set the game to impossible
        if plays_poss == False:
            game_poss = False

    # If the game is possible, add its ID to the total of possible IDs
    if game_poss == True:
        game_tot += game_id

# Print the total
print(game_tot)




