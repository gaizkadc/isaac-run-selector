#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports
import random

# Mode selector
def select_mode ():
    mode = {
        1: "Normal Run",
        2: "Challenge"
    }
    mode_key = random.randint(1,2)
    print mode[mode_key]
    return mode_key

# Character selector
def select_character ():
    character = {
        1: "Isaac",
        2: "Magdalene",
        3: "Cain",
        4: "Judas",
        5: "???",
        6: "Eve",
        7: "Samson",
        8: "Azazel",
        9: "Lazarus",
        10: "Eden",
        11: "Lilith",
        12: "Apollyon"
    }
    character_key = random.randint(1,12)
    print "├─ "+character[character_key]

# Difficulty selector
def select_difficulty():
    difficulty = {
        1: "Normal",
        2: "Hard",
        3: "Greed"
    }
    difficulty_key = random.randint(1,3)
    print "└── "+difficulty[difficulty_key]

# Select challenge
def select_challenge ():
    challenge = {
        1: "Pitch Black",
        2: "High Brow",
        3: "Head Trauma",
        4: "Darkness Falls",
        5: "The Tank",
        6: "Solar System",
        7: "Suicide King",
        8: "Cat Got Your Tongue",
        9: "Demo Man",
        10: "Cursed!",
        11: "Glass Cannon",
        12: "When Life Gives You Lemons",
        13: "Beans!",
        14: "It's In The Cards",
        15: "Slow Roll",
        16: "Computer Savvy",
        17: "Waka Waka",
        18: "The Host",
        19: "The Family Man",
        20: "Purist",
        21: "XXXXXXXXL",
        22: "SPEED!",
        23: "Blue Bomber",
        24: "PAY TO PLAY",
        25: "Have a Heart",
        26: "I RULE!",
        27: "BRAINS!",
        28: "PRIDE DAY!",
        29: "Onan's Streak",
        30: "The Guardian",
        31: "Backasswards",
        32: "Aprils Fool",
        33: "Pokey Mans",
        34: "Ultra Hard",
        35: "Pong"
    }
    challenge_key = random.randint(1,35)
    print "└─ "+challenge[challenge_key]

# Main
mode = select_mode()
if mode == 1:
    select_character()
    select_difficulty()
else:
    select_challenge()
print "\nHave fun!"