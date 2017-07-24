from sys import argv

##
# Testing example 4, page 80
#
# Commenting out lines 10-15 causes the program
# to read in results, and then exit
#
##

##
# Testing example 5, raw_input only....
##
script, filename = argv

txt = raw_input(filename)

##
# This method works, but you have to keep hitting enter as an end user, to
# promt the next step - in the original verison, using "open" did not
# require you to do this.
##

print "Here's your file %r:" % filename
print filename



print "Type the filename again:"
file_again = raw_input("> ")

txt_again = raw_input(file_again)

print file_again
