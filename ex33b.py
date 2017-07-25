#!/usr/bin/env python

import time

# Study drill for exercise 33

def function_junction(funky):
    """This function does some counting"""
    interval = 0
    the_nom = 101
    numbers = []

    while interval < the_nom:
        print "The number is %d" % interval
        numbers.append(interval)

        time.sleep(0.1)

        interval = interval + 1
        print "Moving on"
    return funky

print "Ok, here we go:"
funkadelic = 0
function_junction(funkadelic)

print "The end."
