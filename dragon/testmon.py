#!/usr/bin/env python

from random import randint

def fight_monster():
    """This function is for a fight with a monster - it is D20 based"""
    dice_roll = (randint(1,20))
    d20 = int(dice_roll)

    print "Inside the function, this is the result: %d" % d20
    return d20


print "Outside the function the result is %d" % fight_monster()
