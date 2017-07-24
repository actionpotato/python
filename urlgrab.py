#!/usr/bin/env python
# from sys import argv

# workfile = argv
# print "Enter filename to write:"

# raw_input("?")


###########################################################
# Tying this as a way to keep my printer awake on the LAN #
###########################################################
import urllib

# Change link to 192.168.1.100 when printer is up.
link = "https://www.google.com"

file_in = urllib.urlopen(link)
myfile = file_in.read()
print myfile

# Trying to write to file instead of stdout (it isn't working)
# target = open(workfile, 'w')
# target.write(myfile)
# target.close()
