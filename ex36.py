#!/usr/bin/env python

from random import randint
from sys import exit

# This is how I will calculate the D20 values:
dice_roll = (randint(1,20))
d20 = int(dice_roll)

# while True

print "You rolled %d "% dice_roll

if d20 == 1:
    print "CRITICAL FAILURE! Talk about whiffing it!"
    #dead()
if d20 < 5:
    print "Wow, talk about a miss!"
    #dragon()
if d20 < 10:
    print "you missed, but barely stay upright."
    #dragon()
if d20 <= 15:
    print "Hit! you do damage!"
    #dragon()
if d20 <= 19:
    print "You hit HARD!"

if d20 == 20:
    print "Natural 20? instant kill!!!"
else:
    print "That isn't supposed to happen... You find a glorkum.s"
    exit(0)
#
