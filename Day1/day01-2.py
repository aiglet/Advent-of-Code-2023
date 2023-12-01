'''
Since there are only nine possible numbers, in theory, we should be able to
do this as a character checker kind of thing, and then do the digit checks.
Do all the checks and then set the proper digit.

How to skip ahead the proper amount in the line? Maybe we can take the first
character off?
'''

# Import the 'regex' and 'word2number' packages we need
import regex as re
from word2number import w2n

# Open the input file
data = open("inputdata.txt")
lines = data.readlines()


def number_finder2(text):
    '''Takes a text file, finds numbers in either integer or string form,
    and returns the sum of the first and last number in each line of
    the file'''

    total = 0

    # Iterate through the file
    for line in text:
        digit1 = []
        digit2 = []
        bignum = ''

        # Find all possible numbers in the line
        possibles = re.findall(r"(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine)",
            line, overlapped=True)

        # Take the first and last numbers found in the line and turn them
        # into actual numbers
        digit1 = w2n.word_to_num(possibles[0])
        digit2 = w2n.word_to_num(possibles[-1])

        # Turn them back into strings so they can be smushed into one number
        # without adding, and then turn that string back into an integer
        bignum = str(digit1) + str(digit2)
        bignum = int(bignum)

        # Add that line's integer total to the running total
        total += bignum

    # Print the final total
    print(f"{total}")

number_finder2(lines)