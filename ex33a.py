#!/usr/bin/env python

# Study drill for exercise 33

def function_junction(funky):
    """This function does some counting"""
    interval = 0
    numbers = []

    while interval < 101:
        print "The number is %d" % interval
        numbers.append(interval)

        interval = interval + 1
        print "Moving on"
    return funky

print "Ok, here we go:"
funkadelic = 0
function_junction(funkadelic)
