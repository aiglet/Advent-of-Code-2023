data = open("fulldata.txt")
lines = data.readlines()


def game_checker(games):

    # Define the variables we'll need to do the final sums
    game_sum = 0
    red_total = 12
    green_total = 13
    blue_total = 14

    # Iterate through the set of games
    for game in games:

        # Set up the variables for counting the block totals in each game
        red = 0
        green = 0
        blue = 0

        # Clean up the game and split it into the game number and the moves
        game = game.strip()
        split1 = game.split(": ")

        # Pull the game number out of the split and get the actual number of
        # the game (this is long because it has to handle two-digit numbers)
        game_num = split1[0]
        game_num = game_num[4:]
        game_num = game_num.strip()
        game_num = int(game_num)

        # Pull the cubes out of the game and split them into the individual
        # games
        cubes = split1[1]
        cubes = cubes.split("; ")

        # Go through each game and split it into moves
        for cube in cubes:
            cube = cube.split(", ")

            # Iterate through the moves of each game
            for move in cube:

                # Split out the number of cubes (which is either a
                # one digit number and a space or a two digit number) and
                # remove any extra spaces
                cube_number = move[:2]
                cube_number = cube_number.strip()

                # Pull out the color of the cubes and remove any extra spaces
                color = move[2:]
                color = color.strip()

                # Check the color of the cubes and add it to the current
                # game's total
                if color[0] == 'b':
                    blue += int(cube_number)
                elif color[0] == 'g':
                    green += int(cube_number)
                elif color[0] == 'r':
                    red += int(cube_number)

        # If the current game is possible, add the number of the game to the
        # total sum of game numbers
        if red <= red_total and blue <= blue_total and green <= green_total:
            game_sum += game_num

    print(game_sum)


game_checker(lines)
