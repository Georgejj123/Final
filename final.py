# This program rolls two dices and prints what you got

# We set two variables (min and max) , lowest and highest number of the dice. 
import random
min = 1
max = 6


roll_again = "yes"
# We then use a while loop, so that the user can roll the dice again. 
while roll_again == "yes" or roll_again == "y":
    print "Rolling the dices:"
    print "The values are:"
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll the dices again?")
