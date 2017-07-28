#!/usr/bin/env python

from random import randint
from sys import exit

import time
from ex36_fight import fight_dragon

dice_roll = (randint(1,20))
d20 = int(dice_roll)

while True:
    fight_dragon()
