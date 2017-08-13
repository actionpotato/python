#!/usr/bin/env python

from random import randint
import time

dragon_damage = 0
d20 = 0

def fight_monster():
    """This function is for a fight with a monster - it is D20 based"""
    dice_roll = (randint(1,20))
    d20 = int(dice_roll)

    print "Inside the fight_monster function, d20 is: %d" % d20
    return d20


def fight_dragon():

    global dragon_damage
    global d20

    print "Here is the first test of dragon_damage: %d" % dragon_damage
# This is how I will calcudice_roll = (randint(1,20))
#    dragon_damage = 0
# Start the dragon with no damage
    # fight_monster(d20)
    # dragon_damage = starter
    while dragon_damage <= 7:
        # fight_monster()
    #    dice_roll = (randint(1,20))
    #    d20 = int(dice_roll)
    #    fight_monster(dice_roll)

        #print "You rolled %d "% d20
        #print "Dragon Damage is %d" % dragon_damage

        if d20 == 1:
            print "CRITICAL FAILURE! Talk about whiffing it!"
            time.sleep(1)
            print "You stumble... and the dragon eats you."
            dragon_damage = dragon_damage
            print "Dragon Damage is %d" % dragon_damage
            dead()

        if d20 < 5:
            print "Wow, talk about a miss!"
            time.sleep(1)
            print "Dragon Damage is %d" % dragon_damage
            dragon_damage = dragon_damage
            fight_dragon()

        if d20 < 10:
            print "you missed, but barely stay upright."
            time.sleep(1)
            dragon_damage = dragon_damage
            print "Dragon Damage is %d" % dragon_damage
            fight_dragon()

        if d20 <= 15:
            print "Hit! you do damage!"
            time.sleep(1)
            dragon_damage = dragon_damage + 1
            print "Dragon Damage is %d" % dragon_damage
            fight_dragon()

        if d20 <= 18:
            print "You hit HARD!"
            time.sleep(1)
            dragon_damage = dragon_damage + 3
            print "Dragon Damage is %d" % dragon_damage
            fight_dragon()

        if d20 == 20:
            print "Natural 20? instant kill!!!"
            dragon_damage = dragon_damage + 10
            print "Dragon Damage is %d" % dragon_damage
            print "You won!"
            exit(0)

        else:
            print "That isn't supposed to happen... You find a glorkum.s"
            exit(0)

        return dragon_damage

def dead():
    exit(0)

#fight_monster()
fight_dragon()
