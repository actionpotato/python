# set variable -- 1 string in string
x = "There are %d types of people." % 10
# define new variables called by y
binary = "binary"
do_not = "don't"
# strings entered here, counts as 1, or 2, depending how you count
# when counting total strings
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# Here, we put a string in a string, counts as 1
# However, we are pulling in a variable, not a string, so it also
# Has strings in the string it is calling!
print "I said: %r." % x
print "I also said: '%s'." % y

# define two variables, note one expects a varible inside itself
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Here we call the joke_evaluation variable, and follow it with the
# hilarious variable, as the joke_evaluation needs input
# I tried commenting out the 'hilarous' variable and it printed
# joke_evaluation EXACTLY as shown above, without an error
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# I don't think this is a string in a string, rather a concatination
print w + e
