#!/usr/bin/env python3
# Michael Gresham
# CPSC 386-01
# 2021-11-29
# greshammichael@csu.fullerton.edu
# @Michael-Gresham
#
# Lab 03-00
#
# This is my pig game program. Essentially through text it
# will simulate the dice game called pig.

from snakegame import SnakeGame
import sys


def main():
    """
    This is the driver for the snake program.
    Essentially this will call and run snake game.
    and exit the program when the user exits the game.
    """
    snek = SnakeGame()
    sys.exit(snek.run())


if __name__ == "__main__":
    main()
