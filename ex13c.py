#!/usr/bin/env python

from sys import argv

le_input, la_first, la_second, da_gruben, los_argumentus = argv

print "This program is called: ", le_input
print "The first argument is: ", la_first
print "The second argument is: ", la_second
print "The third argumet is: ", da_gruben
print "The final countdown: ", los_argumentus

years_it = raw_input("How many years have you been in IT?: ")

print """
So, you have been in IT for %r years, and you have chosen the following
arguments for this script:

This script: %r
Your first argument:%r
Your second argument:%r
Your third argument%r
Your fourth and final argument:%r
""" % (years_it, le_input, la_first, la_second, da_gruben, los_argumentus)
