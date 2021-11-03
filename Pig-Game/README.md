# Pig - A Die Game

The objectives of this exercise are:

* Verify that a student's development environment is set up
* Refresh our memory on how to write a program to a specification
* Improving our programming practices
* Learn about the Python programming language and it's standard library

We shall all write the dice game named [Pig](https://en.wikipedia.org/wiki/Pig_(dice_game)). Pig is a game that is probably quite old and was first described in print by [John Scarne](https://en.wikipedia.org/wiki/John_Scarne) (famous for [Scarne's four aces trick](https://youtu.be/0Zmy2WlbSpg)).

The game uses only one six sided die and is played with 2 or more players. Players take turns rolling the die and tabulating a score according to the rules. The first player to score 100 or more points wins.

In our version of the game, the six-sided die will be simulated by the computer. Additionally, the game can be played against the computer should there only be one player. If there is more than one player, the game is played as a [hotseat](https://en.wikipedia.org/wiki/Hotseat_(multiplayer_mode)) multiplayer game.

## Rules

* There is at least two players playing the game. A two player game may be against another player or against the computer. Three or more player games do not have a computer player to play against.
* There is at most 4 players in a game.
* There is one six-sided die (simulated by the game using a psuedo-random number generator); the faces of the die are numbered 1, 2, 3, 4, 5, and 6. Opposing sides of the die sum to 7 (standard western casino dice).
* The game is turn based. The player who goes first is selected by each player rolling the die once. The players are ordered from in ascending order. If there is a tie between two or more players, the computer can break the tie by arbitrarily assigning that player to a position not less than the position the player rolled.
* Once each player has had a turn in ascending order, the turn returns to the first player.
* Each turn, a player rolls the die.
    * If the player rolls a 1, the player scores nothing that turn and it becomes the next player's turn. The player's overall score does not change because the player has lost the points accrued during their turn.
    * If the player rolls any other number, the value of the die is added to their turn's score as points and the player's turn may continue. The player's overall score does not change until their turn ends.
    * If a player chooses to hold, their turn total is added to their score, and it becomes the next player's turn.
* The play may not choose to hold until after the die has been rolled at least once.
* The game ends when a player ends their turn with a score of 100 points or greater.
* At the beginning of every die roll, the game displays the current player's total score, current turn score, and how many times the player has rolled. Once the die is rolled, the computer displays the value of the die. If it is a 1, the computer ends the current player's turn and moves on to the next player.

## Requirements

The requirements of the program are that the game must play according to the rules given above. If there is any ambiguity of the rules, the the student should discuss the rules with the instructor to clarify the rules.

The game must be written in Python 3. Limit your game to use only what is available in the Python Standard Library. Do not use additional Python modules that are outside of the Python Standard Library.

The game should take advantage of object oriented design. At a minimum, the following objects must be defined:
* A 6 sided die object shall be defined in a file named `die.py`
* A player object shall be defined in a file named `player.py`
* A game object shall be defined in a file named `pig_game.py`

Each object must be defined in it's own file. It is not required to create a Python module. To the best of your ability, attempt to model any additional elements of the game as objects.

The source file that is the main file shall be named `pig.py`, and it shall be executable with a shebang at the top of the file.

The user interface of the game is text. There are no graphics (2D, 3D, sprites, etc.) in this game. Students are encouraged to use [curses](https://docs.python.org/3/library/curses.html?highlight=curses#module-curses) but it is not a requirement.

If you would like to use audio effects or a soundtrack, you may however the program may only use what's available in the Python Standard Library.

The computer player does not need to be a sophisticated machine. You may make the computer player as simple or as sophisticated as you like. However, the computer player should not appear to be unpredictable. The computer player may be defined as a separate class, a sub-class of the player class, or a special case of the player class.

Since this game is a terminal based game, use [sleep](https://docs.python.org/3/library/time.html?highlight=sleep#time.sleep) or other similar mechanism to slow down the game to make the text appear on the screen slowly. Give the player an opportunity to read the text.

## Don't Forget

Please remember that:

* You need to put a header in every file per the [instructions](https://docs.google.com/document/d/1OgC3_82oZHpTvoemGXu84FAdnshve4BCvtwaXZEJ9FY/edit?usp=sharing) shared in Canvas.
* You need to follow [PEP-8](https://www.python.org/dev/peps/pep-0008/); use linters and style checkers such as `pycodestyle`, `pylint`, `pyflakes`, and `flake8`.
* You need to test your program!

# Rubric

This exercise is worth 10 points. There is a total of 10 points possible. Your program must not have any syntax errors before it is graded. Submissions that have a syntax error will be assigned a score of 0.

For each problem:

* Functionality (6 points): Your submission shall be assessed for the appropriate constructs and strategies to address the exercise. A program the passes the instructor's tests completely receives full marks. A program that partially passes the instructors tests receives partial-marks. A program that fails the majority or all the tests receives no marks.
    * A game that does not have a computer player forfeits all marks.
    * A game that is not multiplayer looses 3 points
    * A game that is not defined in separate files per the requirements looses 3 points.
    * A game that does not execute with the command `./pig.py` looses 3 points.
    * A game that does not define classes in individual files looses 4 points.
    * Partial implementation of the rules shall loose 1-5 points depending on the number of requirements not met.
* Format & Readability (4 point): Your submission shall be assessed by checking whether your code passess the style and format check, as well as how well it follows the proper naming conventions, and internal documentation guidelines. Git log messages are an integral part of how readable your project is. Failure to include a header forfeits all marks. Not conforming to PEP-8 forfeits all marks.

