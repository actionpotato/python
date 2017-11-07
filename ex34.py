#!/usr/bin/env python

import time

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print "All the animals are:"

time.sleep(1)

for number in animals:
    print "The %s." % number
    time.sleep(0.5)

print "OK, now we know what is in the list, lets look at the individual parts."
print "\n"

time.sleep(2)

print "The animal at 1, is a %s" % animals[1]
time.sleep(1)

print "The third (3rd) animal is at 2 and is %s" % animals[2]
time.sleep(1)

print "The first (1st) animal is at 0, and it is a %s" % animals[0]
time.sleep(1)

print "The animal at 3, is a %s" % animals[3]
time.sleep(1)

print "The fifth (5th) animal is at 4 and is a %s" % animals[4]
time.sleep(1)

print "the animal at 2 is at 2, and is a %s" % animals[2]
time.sleep(1)

print "The animal at 4, is at the fourth place and is a %s" % animals[4]
time.sleep(1)

print "\n"
print "\n"

print "Done!"
