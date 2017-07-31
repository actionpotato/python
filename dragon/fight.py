from random import randint
from sys import exit
import time
import os

def first_view():
    """This is the first area that the user encounters."""
    os.system('clear')
    print "You stand in a grassy field. There is a hole in the ground in front of you."
    print "Options are, look, down, or leave."

    enter_dungeon = False

    while True:
        user_input = raw_input("> ")
        if user_input == "look":
            os.system('clear')
            print "It is a bright sunny day blue skies... and a dark and dreary hole in the ground lies before you."
            time.sleep(4)
            first_view()
        if user_input == "leave":
            print "You flee quickly!"
            exit (0)
        if user_input == "down":
            print "You climb down into the hole and find..."
            first_room()
        if user_input == "exit":
            exit(0)
        else:
            print "Command not understood."
            first_view()

def first_room():
    print "You are standing in a square room."
    print "Exits are North, up."
    enter_dungeon = False

    while True:
        user_input = raw_input("> ")
        if user_input == "look":
            first_room()
        if user_input == "North":
            fight_dragon()
        if user_input == "up":
            first_view()
        if user_input == "exit":
            exit(0)
        else:
            print "Command not understood."
            first_room()

def fight_monster(dice_roll):
    """This function is for a fight with a monster - it is D20 based"""
    # This is how I will calculate the D20 values:
    # This should actually be a generic....
    # dice_roll(randint(1,20))
    # d20 = int(dice_roll)
    # return d20

def fight_dragon():
# This is how I will calcudice_roll = (randint(1,20))

    dragon_damage = 0
# Start the dragon with no damage


    while dragon_damage <= 7:

        dice_roll = (randint(1,20))
        d20 = int(dice_roll)
        fight_monster(dice_roll)
        print "You rolled %d "% dice_roll
        print "Dragon Damage is %d" % dragon_damage

        if d20 == 1:
            print "CRITICAL FAILURE! Talk about whiffing it!"
            time.sleep(1)
            print "You stumble... and the dragon eats you."
            dragon_damage = dragon_damage
            print "Dragon Damage is %d" % dragon_damage
            exit(0)

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
