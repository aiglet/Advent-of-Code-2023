# Open the data file and convert it to individual lines
data = open("inputdata.txt")
lines = data.readlines()


# Parse the lines

def number_finder(text):

    # Initiate a variable to hold the total
    total = 0

    # Iterate through the data file
    for line in text:
        # Split the game into its individual components
        chars = list(line)

        # Initiate some variables to hold the numbers - we're initiating them as
        # arrays rather than integers because we'll want to be able to
        # concatenate them later without *adding* them.
        digit1 = []
        digit2 = []

        # Initiate some variables to hold things once we've found both the
        # digits
        bignum = ''
        longlist = []

        # Iterate through the array to find numbers
        for char in chars:

            # See if the character is an integer
            try:
                int(char)

                # If it is, put the numbers into the holding variables

                # This game checks to see if digit1 is still an empty list
                if not digit1:
                    digit1 = char
                else:
                    digit2 = char

            # If it's not an integer, move on
            except ValueError:
                continue

        # Handle the case where there's only one number in the game
        if digit1 and not digit2:
            digit2 = digit1

        # Turn the two digits into one list
        longlist = [int(digit1[0]), int(digit2[0])]

        # Turn the long list into one number
        bignum += str(longlist[0])
        bignum += str(longlist[1])
        bignum = int(bignum)

        # Add that number to the running total
        total += bignum

    print(f"The final total is {total}")


number_finder(lines)
