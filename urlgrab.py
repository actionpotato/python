#!/usr/bin/env python
# from sys import argv

# workfile = argv
# print "Enter filename to write:"

# raw_input("?")


###########################################################
# Tying this as a way to keep my printer awake on the LAN #
###########################################################
import urllib

link = "http://192.168.1.101"

file_in = urllib.urlopen(link)
myfile = file_in.read()
print myfile

# Trying to write to file instead of stdout (it isn't working)
# target = open(workfile, 'w')
# target.write(myfile)
# target.close()
