from sys import argv

##
# Example 7 - use close on this program to close the open files
# Closing a file after using it is best practice!
##


script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

txt.close()
# This line should generate an error
# print txt.read()

## And indeed it did!
## Here is the output:

# george@linux-laptop:~/programming$ python ex15d.py ex15_sample.txt
# Here's your file 'ex15_sample.txt':
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.
#
# Traceback (most recent call last):
# File "ex15d.py", line 18, in <module>
#     print txt.read()
# ValueError: I/O operation on closed file





print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()
