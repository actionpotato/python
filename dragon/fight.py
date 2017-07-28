from random import randint

def fight_monster(dice_roll):
    """This function is for a fight with a monster - it is D20 based"""
    # This is how I will calculate the D20 values:
    # This should actually be a generic....
    dice_roll(randint(1,20))
    d20 = int(dice_roll)
    return d20

def break_words(stuff):
    """see if this imports properly"""
    words = stuff.split(' ')
    return words

def fight_dragon():
# This is how I will calcudice_roll = (randint(1,20))
    dice_roll = (randint(1,20))
    d20 = int(dice_roll)
    print "You rolled %d "% dice_roll
# Start the dragon with no damage
    dragon_damage = 0
    if d20 == 1:
        print "CRITICAL FAILURE! Talk about whiffing it!"
    #dead()
        print dragon_damage
        # exit(0)
    if d20 < 5:
        print "Wow, talk about a miss!"
    #dragon()
        print dragon_damage
        # exit(0)
    if d20 < 10:
        print "you missed, but barely stay upright."
    #dragon()
        print dragon_damage
        # exit(0)
    if d20 <= 15:
        print "Hit! you do damage!"
    #dragon() ++dragon_damage
        dragon_damage += 1
        print dragon_damage
        if dragon_damage > 4:
            #win()
            print "You won!"
            exit(0)
        else:
            print "You ready yourself again:"
    if d20 <= 19:
        print "You hit HARD!"
    #dragon() ++dragon_damage X3
        dragon_damage += 3
        print dragon_damage
        if dragon_damage > 4:
            #win()
            print "You won!"
        else:
            print "Get ready."
        # exit(0)
    if d20 == 20:
        print "Natural 20? instant kill!!!"
    #killed_dragon()
        dragon_damage = 10
        print dragon_damage
        print "You won!"
        exit(0)
    else:
        print "That isn't supposed to happen... You find a glorkum.s"
        exit(0)
#
