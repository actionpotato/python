#!/usr/bin/env python

import time

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print "All the animals are:"

time.sleep(1)

for number in animals:
    print "The %s." % number
    time.sleep(0.5)


print "The animal at 1, cardinal is the 2nd animal, ordinal: %s" % animals[1]
