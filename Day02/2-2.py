# Get the data
data = open("fulldata.txt")

# Split it into lines - each game is a game
lines = data.readlines()

# Set the variable for the total
power_tot = 0

# Go through each game in turn
for game in lines:

    print("New game!")

    # Split the game into the game ID and the draws
    game_id, draws = game.strip().split(": ")

    # Get the game number alone
    game_id = int(game_id.split(" ")[1])

    # Split the draws into separate items
    draws = draws.split("; ")

    # Set up the variables to hold the local maximum for this game
    redmax = 0
    greenmax = 0
    bluemax = 0

    # Go through each set of plays
    for playset in draws:

        # Split them into individual plays
        plays = playset.split(", ")

        # Go through each play individually
        for play in plays:

            # Split the play into the number and color of the blocks involved
            play_num = int(play.split(" ")[0])
            play_col = play.split(" ")[1]

            # Check each play to see if the number of blocks is larger than
            # the current local max for that color, and reset it if so
            if play_col == "red" and play_num > redmax:
                redmax = play_num
            if play_col == "green" and play_num > greenmax:
                greenmax = play_num
            if play_col == "blue" and play_num > bluemax:
                bluemax = play_num

    # Calculate the "game power" by multiplying the local max values
    # together, then add it to the running game total
    game_power = redmax * bluemax * greenmax
    power_tot += game_power

# Print the final total
print(power_tot)