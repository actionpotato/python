#!/usr/bin/env python

# Ok, lets comment this guy

# import the argv function from sys - so we can use CLI arguments
from sys import argv

# First argument '0' is the script itself, the second is the file we want '1'
script, input_file = argv

# Define the print all function, it should read some contents that we Define
# then print those contents

def print_all(f):
    print f.read()

# Now we define the rewind function - it performs a "seek" on the file
# I am guessing we go back to the beginning of the file with this function
# so we can start printing out the lines again
def rewind(f):
    f.seek(0)


# Here we print the file, but we are usign readline to print each line
# one at a time
def print_a_line(line_count, f):
    print line_count, f.readline()

# define current_file as the user input file and open it
current_file = open(input_file)

print "First let's print the whole file:\n"

# print all of it - calling the print_all function
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# rewind function - go back to the beginning of the file
rewind(current_file)

print "Let's print three lines:"


# Ok, here is were a loop is probably a much better idea...
# We manually define the line, print it with the print_a_line function
# then we pseudo-loop through the file, incrementing the line number each time
# IMO, too much code, and too limited, should be a loop.

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
