"""Pig_game.py module"""
# Michael Gresham
# CPSC 386-01
# 2021-10-10
# greshammichael@csu.fullerton.edu
# @Michael-Gresham
#
# Lab 02-00
#
# My pig_game_class
#
import time
import die
import player


class PigGame:
    """A pig game class that can run the pig dice game."""

    def __init__(self):
        # pig_game class constructor
        self.dice = die.Die()
        self.player_list = []

    def check_victory_condition(self, c_player):
        """
        checks to see if selected player fufills the victory condition
        of reaching 100 total points.
        """
        if c_player.total_score >= 100:
            return True
        return False

    def win(self, c_player):
        """This displays text declaring who won the game."""
        time.sleep(1)
        print(c_player.get_player_name() + " wins the game!")
        time.sleep(1)
        print("Thank you for playing the game and see you next time!")

    def start_up(self):
        """
        Starts up the class by having players select between ai or multiplayer
        and depending on the choice it switches to the appropriate function.
        """
        time.sleep(1)
        print("Welcome to my Pig game!")
        time.sleep(1)
        game_type = input("Do you want to play against an Ai? (yes/no): ")
        # input checking to make sure the user only enters a valid response.
        while (
            game_type != "yes"
            and game_type != "no"
            and game_type != "Yes"
            and game_type != "No"
            and game_type != "y"
            and game_type != "n"
        ):
            time.sleep(1)
            print("Error incorrect response! Please try again!")
            time.sleep(1)
            game_type = input("Do you want to play against an Ai? (yes/no)")
        time.sleep(1)
        print("Thank you for your response now starting game!")
        # If its an ai game there's only going to be 2 players as represented below
        if game_type == "yes" or game_type == "y" or game_type == "Yes":
            num_players = 2
            name = input("Please enter your name: ")
            c_player = player.Player(name, False)
            self.player_list.append(c_player)
            name = input("Please enter the name of the ai: ")
            a_player = player.Player(name, True)
            self.player_list.append(a_player)
        else:
            time.sleep(1)
            num_players = int(
                input(
                    "Please enter the number of players"
                    + "who will be playing the game (at least 2): "
                )
            )
            # This is making sure that the user inputs a valid number as
            # you can't have negative players or below two players in a multiplayer game.
            while num_players < 2:
                time.sleep(1)
                num_players = int(
                    input(
                        "Please enter the number of players"
                        + " who will be playing the game (at least 2): "
                    )
                )
            # This will iterate through the number of players
            # and assigne each a name and add it to pig_games list of players.
            for i in range(0, num_players):
                time.sleep(1)
                player_name = input(
                    "Please enter the " + str(i + 1) + " player's name: "
                )
                current_player = player.Player(player_name, False)
                self.player_list.append(current_player)
        time.sleep(1)
        print("Now we need to roll for turn order.")
        # This function serves to decide turn by asking each player
        # to roll the dice, and it automatically calculates the ai roll.
        for i in range(0, num_players):
            if self.player_list[i].is_human():
                time.sleep(1)
                response = input(
                    self.player_list[i].get_player_name()
                    + " please enter \"roll\" to figure out your turn order: "
                )
                while response != "roll":
                    time.sleep(1)
                    print(
                        "Error please specifically enter roll"
                        + " and make sure it's completely lowercase!"
                    )
                    response = input(
                        self.player_list[i].get_player_name()
                        + " please enter \"roll\" to figure out your turn order: "
                    )

                roll = self.dice.get_roll1d6()
                time.sleep(1)
                print(
                    self.player_list[i].get_player_name()
                    + " rolled a "
                    + str(roll)
                )
                self.player_list[i].turn_order = roll
            else:
                roll = self.dice.get_roll1d6()
                time.sleep(1)
                print(
                    self.player_list[i].get_player_name()
                    + " rolled a "
                    + str(roll)
                )
                self.player_list[i].turn_order = roll
        # This function call essentially sorts the list by the turn
        # order that each player rolled. reverse = False says that it will be a increasing list.
        self.player_list.sort(key=lambda x: x.get_turn_order(), reverse=False)

        round_number = 0
        player_total = 0
        victory = False
        # Essentially the game will run until someone wins.
        while not victory:
            round_number += 1
            time.sleep(1)
            print()
            time.sleep(1)
            print("Starting Round " + str(round_number))
            # This will list through each player and allow each to perform their turn.
            for c_player in self.player_list:
                c_player.times_rolled = 0
                time.sleep(1)
                print("It's " + c_player.get_player_name() + " turn.")
                turn = True
                # This while loop lasts until the player finishes their turn by saying that they
                # no longer wish to roll anymore dice.
                while turn:
                    # Checks if the player or ai wishes to continue
                    # and the logic is implemented in player class.
                    if c_player.should_continue(player_total):
                        c_player.times_rolled += 1
                        roll = self.dice.get_roll1d6()
                        time.sleep(1)
                        print(
                            c_player.get_player_name()
                            + " has rolled a "
                            + str(roll)
                        )
                        # roll = 1 in pig basically means that the players scores no points and their
                        # turn ends.
                        if roll == 1:
                            time.sleep(1)
                            print(
                                c_player.get_player_name()
                                + " turn is now over and no points are added!"
                            )
                            c_player.set_turn_score(0)
                            turn = False
                        else:
                            c_player.set_turn_score(
                                c_player.get_turn_score() + roll
                            )
                            time.sleep(1)
                            print(
                                c_player.get_player_name()
                                + " Turn Score: "
                                + str(c_player.get_turn_score())
                                + " Total Score: "
                                + str(c_player.get_total_score())
                            )
                    # In the case the player ends their turn their accrued points for
                    # that turn is added to their total score.
                    else:
                        time.sleep(1)
                        print(
                            str(c_player.get_turn_score())
                            + " has been added to total score!"
                        )
                        c_player.set_total_score(
                            c_player.get_total_score()
                            + c_player.get_turn_score()
                        )
                        c_player.set_turn_score(0)
                        time.sleep(1)
                        print(
                            c_player.get_player_name()
                            + "'s total score is "
                            + str(c_player.get_total_score())
                        )
                        turn = False
                        c_player.times_rolled = 0
                        # Checks if a player won when their points are added
                        # and if they did it displays a victory message
                        # and sets victory to false to break out of the first while loop.
                        if self.check_victory_condition(c_player):
                            self.win(c_player)
                            victory = True
                time.sleep(1)
                print()
                player_total = c_player.get_total_score()
                if victory is True:
                    break
