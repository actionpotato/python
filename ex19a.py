#!/usr/bin/env python

# First, we define the function, and what it does
# The function name is cheese_and_crackers, it takes the arguments
# cheese_count and boxes_of_crackers - in that order
# it then prints out the amount of each - using the arguments as
# variables to populate the print output:
# However, the function just sits there, because we have not called it yet

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# This is the first time we actually call the function.
# We print, then call the function, passing the arguments 20 and 30
# Those arguments map to cheese_count and boxes_of_crackers
#

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# This time, we print, then call the function using variables
# First, we define the variables amount_of_cheese and amount_of_crackers
# and the numerical amount of each
# Then, we call the function, using the variables in the correct order
# The variables pass the number values to the function and it runs

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Now, here we print, and then call the function with math
# Inside the arguments for the function, we do math, and pass the
# result to the funciton. Note, there is still a comma between the
# values

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Finally, we print, demonstrating variables AND math
# using the variables amount_of_cheese and amount_of_crackers
# from the example above (because we only defined the variables once)
# we pass the value of the variables to the function *AND* we add
# the value of 100 to the variabes, so the total gets passed to the function

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)
