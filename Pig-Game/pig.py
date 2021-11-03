#!/usr/bin/env python3
# Michael Gresham
# CPSC 386-01
# 2021-10-10
# greshammichael@csu.fullerton.edu
# @Michael-Gresham
#
# Lab 02-00
#
# This is my pig game program. Essentially through text it
# will simulate the dice game called pig.

import sys
import pig_game


def main():
    """
    The purpose of this function is to initiate the pig_game
    object and to start the game.
    """
    game = pig_game.PigGame()
    sys.exit(game.start_up())


if __name__ == '__main__':
    main()
