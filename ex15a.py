#!/usr/bin/python env
# get the argv argument function from the sys module (library)
from sys import argv

#the commandline arguments are, script and filename
#we are defining them Here, argv holds on to script and filename
script, filename = argv

#define txt as the function to open a filename
txt = open(filename)

#print file, and the filename you used as a commandline argument
print "Here's your file %r:" % filename
#print the text variable, and then "read" the function - you are
#calling the open(filename) from before
print txt.read()

print "Type the filename again:"
#take file_again as raw_input from user, and print a prompt (in brackets)
#this function is literally taking the path of a file to read in
file_again = raw_input("> ")

#txt_again variable calls "open" which opens file_again - which took raw input
#from the user - this means that we open the file defined by the user
#in the file_again variable
txt_again = open(file_again)

#print the txt_again variable, using the read function.
print txt_again.read()
