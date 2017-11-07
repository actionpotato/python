#!/usr/bin/env python

from sys import argv

############################################################################
# The reason you need "script, filename" before the = argv is because you  #
# are executing this on the command line. The first argument "0" is the    #
# SCRIPT ITSELF! That is, ex16a1.py -- THIS FILE YOU ARE READING NOW       #
# So, you specify argument "0" then argument "1". This script was failing  #
# because I had not specified the first argument!                          #
############################################################################

# Old Error Example Below:
#
############################################################################
#Traceback (most recent call last):
# File "./ex16a1.py", line 19, in <module>
#    target_file = open(filename)
#TypeError: coercing to Unicode: need string or buffer, list found
###########################################################################

script, filename = argv

# Don't need below, argv pulls from command line
# print "Enter filename to read"
# raw_input("> ")


target_file = open(filename)
print "reading file %r" % filename
print "printing file %r" % filename
print """



"""

print target_file.read()
target_file.close()
