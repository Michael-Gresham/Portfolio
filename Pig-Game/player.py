"""This is the player.py module"""
# Michael Gresham
# CPSC 386-01
# 2021-10-10
# greshammichael@csu.fullerton.edu
# @Michael-Gresham
#
# Lab 02-00
#
# My player class
#

import time


class Player:
    """
    Player class holds all objects a player needs to function
    This includes an attribute to check if a player is an ai.
    """

    # The player class constructor is expected
    # to take in player name and whether its
    # an ai.
    def __init__(self, name, ai):
        self.player_name = name
        self.total_score = 0
        self.turn_score = 0
        self.times_rolled = 0
        self.turn_order = 0
        self._ai = ai

    def is_human(self):
        """Checks if player is human or not"""
        if self._ai is False:
            return True
        return False

    def get_player_name(self):
        """This function returns the players name"""
        return self.player_name

    def set_turn_order(self, value):
        """sets order of players on who goes first."""
        self.turn_order = value

    def get_turn_order(self):
        """returns what order number a player is."""
        return self.turn_order

    def set_total_score(self, value):
        """sets the total score of the player"""
        self.total_score = value

    def set_turn_score(self, value):
        """sets the score the player has for this turn."""
        self.turn_score = value

    def get_turn_score(self):
        """return the number of points player has this turn."""
        return self.turn_score

    def get_total_score(self):
        """returns the total number of points a player has"""
        return self.total_score

    def should_continue(self, player_total_score):
        """
        This function determines whether the ai should roll again
        it takes in the user's total score to help determine the
        decision.
        """
        if self._ai is True:
            if self.total_score + self.turn_score >= 100:
                # If ai can currently win just end his turn.
                return False
            time.sleep(1)
            print(
                self.player_name
                + " has rolled the dice "
                + str(self.times_rolled)
                + " times this turn."
            )
            difference = self.total_score - player_total_score
            # If the user has less then a 10 point lead then play safer.
            if difference >= -10:
                if self.turn_score <= 15 and self.times_rolled <= 3:
                    return True
            # Else if the user has more than that than play riskier.
            if (
                difference < -10
                and self.turn_score <= 20
                and self.times_rolled <= 4
            ):
                return True
            return False
        else:
            time.sleep(1)
            print(
                self.player_name
                + " have rolled the dice "
                + str(self.times_rolled)
                + " times this turn."
            )
            response = input(
                "Do you wish to roll your dice or end your turn. (roll/end): "
            )
            # This checks for proper user input.
            while response != "roll" and response != "end":
                time.sleep(1)
                print("invalid input please try again!")
                time.sleep(1)
                response = input(
                    "Do you wish to roll your dice or end your turn. (roll/end): "
                )
            # Returns true or false depending if the player still wants
            # to player
            if response == "roll":
                return True
            if response == "end":
                return False
        return False
