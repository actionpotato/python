#!/usr/bin/env python

def function_junction(first_argument, second_argument):
    print "This is the junction of the function: %r" % first_argument
    print "This is the second one: %r" % second_argument

variable_1 = 50
variable_2 = 65

print "So, let's call the function:\n"
function_junction(variable_1,variable_2)


# I can't believe I typed this out without looking, and made no mistakes!
# July 12 2017
# Though, to be fair, I typed /n instead of \n in one place
# I also did not anticipate how the cursor for the user would look
# I printed the cursor before the input line.
# I could probably do better by putting that in the raw input function

print "\n"
print "OK, lets try something new:"
print "Type in the first argument:"
print "> "

first_input_from_user = raw_input()

print "OK, you had %r as your first input." % first_input_from_user
print "Let's add a second input, type it in now:"
print "> "

second_input_from_user = raw_input()

print "Alright, your second argument is %r" % second_input_from_user
print "Ok, so let's call the function:"
print "\n"

function_junction(first_input_from_user,second_input_from_user)
