# def break_words(stuff):
#    """This function will break up words for us."""
#    words = stuff.split(' ')
#    return words

def fight_dragon():
    """This function is for the fight with the Dragon"""
    # This is how I will calculate the D20 values:
        dice_roll = (randint(1,20))
        d20 = int(dice_roll)
        return dice_roll


def dragon_room():
    """This function contains actions for the dragon room""""
    # don't let player exit north unless dragon is defeated
    print "You head North, and are confronted with a large dragon!"
    print "Possible exits are South, North (blocked)"
    print "What do you do?"

    player_choice = raw_input("> ")

    if player_choice == "South"
        lurker_room()
    if player_choice == "Fight"
        fight_dragon()
    else:
        "Not understood. Possible options are: South, Fight."
