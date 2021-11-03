"""This is my die.py module which contains the die class"""
# Michael Gresham
# CPSC 386-01
# 2021-10-10
# greshammichael@csu.fullerton.edu
# @Michael-Gresham
#
# Lab 02-00
#
# My die class
#

# importing randint to represent the random roll of a dice.
from random import randint


class Die:
    """the die class represents the die object"""

    # The constructor will only hold the current score the player has for their turn.
    def __init__(self):
        pass

    # get_roll1d6 returns the randomly generated number 1-6 representing rolling a dice.
    def get_roll1d6(self):
        """returns a random number between 1 and 6."""
        return randint(1, 6)
