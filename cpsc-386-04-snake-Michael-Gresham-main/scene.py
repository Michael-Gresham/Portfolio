"""scene.py module"""
# Michael Gresham
# CPSC 386-01
# 2021-11-29
# greshammichael@csu.fullerton.edu
# @Michael-Gresham
#
# Lab 03-00
#
# My scene class
# Holds all the scenes that are present in snek game.
import pygame
from pygame.constants import SCRAP_SELECTION
from random import randint
import os
import pickle
from datetime import datetime


class Scene:
    """General Scene class that's inherited by all other Scene types."""

    def __init__(self, screen, clock, background_color=(0, 0, 0)):
        self._is_valid = True
        self._frame_rate = 60
        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background_color = background_color
        self._background.fill(self._background_color)
        self._clock = clock

    def is_valid(self):
        """If game state is valid return true."""
        return self._is_valid

    def frame_rate(self):
        """return the frame rate of the game."""
        return self._frame_rate

    def start_scene(self):
        """method driver for the class"""
        pass

    def end_scene(self):
        """Does nothing here but meant to return next scene."""
        pass

    def update(self):
        """update the display of the scene."""
        pygame.display.update()

    def draw(self):
        """Display the screen background onto the screen."""
        self._screen.blit(self._background, (0, 0))

    def process_event(self, event):
        """Handles all the events at the particular scene."""
        if event.type == pygame.QUIT:
            self._is_valid = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("Good bye!")
            self._is_valid = False


class TitleScene(Scene):
    """Class which handles the title screen of snake."""

    def __init__(self, screen, clock, title_size, background_color=(0, 0, 0)):
        # class initializer. Initializes basic displays.
        super().__init__(screen, clock, background_color)
        (w, h) = self._screen.get_size()
        self._speed = [0.5, 1, 2]
        self._title_name = "Snek Game"
        self._title_size = title_size
        self._title_color = [50, 50, 50]
        title_font = pygame.font.Font(
            pygame.font.get_default_font(), self._title_size
        )
        self._title = title_font.render(
            self._title_name, True, self._title_color
        )
        self._title_pos = self._title.get_rect(center=(w // 2, h // 4))
        instruction_name = "Press any key to continue"
        self._instruction_size = title_size // 4
        print(str(self._instruction_size))
        instruction_font = pygame.font.Font(
            pygame.font.get_default_font(), self._instruction_size
        )
        self._instruction = instruction_font.render(
            instruction_name, True, (255, 255, 0)
        )
        self._instruction_pos = self._instruction.get_rect(
            center=(w // 2, h // 2 + h // 4)
        )
        self._reverse = False

    def start_scene(self):
        """Method driver of the class. Calls other method in order to run the scene."""
        while True:
            self.draw()

            self.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return self.end_scene()
                self.process_event(event)
        pass

    def draw(self):
        """redraws the background, title name, and instructions and updates screen."""
        super().draw()
        self._screen.blit(self._title, self._title_pos)
        self._screen.blit(self._instruction, self._instruction_pos)
        self.display_rules()
        pygame.display.update()

    def display_rules(self):
        """Displays the instructions for Snake Game."""
        instructions = [
            "Press arrow keys to change the direction of the snake.",
            "Goal of game is to survive and eat as many apples as possible.",
            "Every apple you eat extends the length of the snake.",
            "Try not to hit yourself or hit into a wall or its game over.",
            "Overall score is based off time survived and apples eaten",
            "Good Luck!",
        ]

        (w, h) = self._screen.get_size()
        height = (h // 4) + 100
        width = w // 4
        count = 0
        for instruction in instructions:
            instruction_font = pygame.font.Font(
                pygame.font.get_default_font(), 15
            )
            instruction_render = instruction_font.render(
                instruction, True, (255, 255, 255)
            )
            if count == 5:
                self._screen.blit(instruction_render, (w // 2 - 50, height))
            else:
                self._screen.blit(instruction_render, (width, height))

            height += 50
            count += 1

    def update(self):
        """Updates the color of title text and updates background."""
        super().update()

        for x in range(3):
            self._title_color[x] += 1 * self._speed[x]
            if self._title_color[x] <= 0 or self._title_color[x] >= 255:
                self._reverse = not self._reverse
                self._speed[x] *= -1
                if self._title_color[x] > 255:
                    self._title_color[x] = 255
                if self._title_color[x] < 0:
                    self._title_color[x] = 0
        title_font = pygame.font.Font(
            pygame.font.get_default_font(), self._title_size
        )
        self._title = title_font.render(
            self._title_name, True, self._title_color
        )

    def end_scene(self):
        """returns the next scene."""
        return "Level1"
        pass

    def process_event(self, event):
        """handles the exit button."""
        if event.type == pygame.QUIT:
            print("Goodbye!")
            pygame.quit()


class GameScene(Scene):
    """Start of the GameScene Class"""

    def __init__(self, screen, clock, background_color=(0, 0, 0)):
        """
        This function initializes the GameScene class setting
        the snake game board and the display as well.
        """
        super().__init__(screen, clock, background_color)
        # sets the board and initializes location of snake and apple.
        self.direction = None
        self.start_ticks = pygame.time.get_ticks()
        self.score = 0
        self.time = 0
        self.snake_size = 1
        self.snake = []
        # self.player = player
        self.offset = 100
        (w, h) = self._screen.get_size()
        self.board = []
        for x in range(0, ((h - 100) // 20)):
            row = []
            for y in range(0, (w // 20)):
                if (
                    x == 0
                    or y == 0
                    or y == (w // 20) - 1
                    or x == ((h - 100) // 20) - 1
                ):
                    row.append("border")
                elif x == ((h - 100) // 20) // 2 and y == (w // 20) // 2:
                    row.append("snek")
                    self.snake.append((x, y))
                elif (
                    x == ((((h - 100) // 20) // 2) + (((h - 100) // 20) // 4))
                    and y == (w // 20) // 2
                ):
                    row.append("apple")
                else:
                    row.append("empty")
            self.board.append(row)
        self.timer = "Timer: " + str(self.time)
        title_font = pygame.font.Font(pygame.font.get_default_font(), 25)
        self._title_time = title_font.render(self.timer, True, (255, 255, 255))
        self._timer_pos = self._title_time.get_rect(
            center=(w // 4, self.offset // 2)
        )
        self.title_score = "Score: " + str(self.score)
        self._title_score = title_font.render(
            self.title_score, True, (255, 255, 255)
        )
        self._score_pos = self._title_score.get_rect(
            center=(w // 2 + w // 4, self.offset // 2)
        )

    def start_scene(self):
        """method driver that drives the game logic."""
        self.__init__(self._screen, self._clock)
        while True:
            # gets the time in game in miliseconds.
            miliseconds = pygame.time.get_ticks() - self.start_ticks
            exit = self.move()
            if exit != None:
                return exit
            self.draw()
            self.update(miliseconds)
            for event in pygame.event.get():
                self.process_event(event)
        pass

    def update(self, miliseconds):
        """handles updating the timer, background, and score."""
        if (miliseconds // 1000) > self.time:
            self.time = miliseconds // 1000
            self.timer = "Timer: " + str(self.time)
            title_font = pygame.font.Font(pygame.font.get_default_font(), 25)
            self._title_time = title_font.render(
                self.timer, True, (255, 255, 255)
            )
            if (self.time % 3) == 0 and self.time != 0:
                self.score += 1
        self.title_score = "Score: " + str(self.score)
        title_font = pygame.font.Font(pygame.font.get_default_font(), 25)
        self._title_score = title_font.render(
            self.title_score, True, (255, 255, 255)
        )
        pygame.display.update()
        pass

    def create_apple(self):
        """Handles the logic that places a new apple when one is eaten."""
        valid = False
        while valid == False:
            row = randint(1, len(self.board) - 1)
            column = randint(1, len(self.board[0]) - 1)
            if self.board[row][column] == "empty":
                self.board[row][column] = "apple"
                valid = True
        pass

    def move(self):
        """Handles the movement logic of the snake. and loss conditions."""
        if self.direction == None:
            pass
        else:
            row = self.snake[0][0]
            column = self.snake[0][1]
            added = False
            if self.direction == "up":
                row -= 1
            elif self.direction == "down":
                row += 1
            elif self.direction == "left":
                column -= 1
            elif self.direction == "right":
                column += 1

            if (
                self.board[row][column] == "border"
                or self.board[row][column] == "snek"
            ):
                return self.end_scene()
            if (
                self.board[row][column] != "border"
                and self.board[row][column] != "apple"
            ):
                self.board[row][column] = "snek"
                self.snake.insert(0, (row, column))
            if self.board[row][column] == "apple":
                print("hello World")
                added = True
                self.score += 10
                self.create_apple()
                self.board[row][column] = "snek"
                self.snake.insert(0, (row, column))
                miliseconds = pygame.time.get_ticks() - self.start_ticks
                self.draw()
                self.update(miliseconds)
            if added == False:
                (x, y) = self.snake.pop()
                self.board[x][y] = "empty"
            self._clock.tick(10)
        pass

    def end_scene(self):
        """returns next scene which is end scene."""
        print(str(self.score))
        print(str(self.time))
        return "End Scene"

    def draw(self):
        """displays the score, time, and the game screen on pygame display."""
        super().draw()
        self._screen.blit(self._title_score, self._score_pos)
        self._screen.blit(self._title_time, self._timer_pos)
        for x in range(0, len(self.board)):
            for y in range(0, len(self.board[0])):
                if self.board[x][y] == "border":
                    pygame.draw.rect(
                        self._screen,
                        (164, 116, 73),
                        pygame.Rect((y * 20), (x * 20) + self.offset, 20, 20),
                    )
                elif self.board[x][y] == "empty":
                    pygame.draw.rect(
                        self._screen,
                        (0, 154, 23),
                        pygame.Rect((y * 20), (x * 20) + self.offset, 20, 20),
                    )
                elif self.board[x][y] == "apple":
                    pygame.draw.rect(
                        self._screen,
                        (0, 154, 23),
                        pygame.Rect((y * 20), (x * 20) + self.offset, 20, 20),
                    )
                    pygame.draw.circle(
                        self._screen,
                        (255, 0, 0),
                        ((y * 20) + 10, (x * 20) + 10 + self.offset),
                        10,
                    )
                elif self.board[x][y] == "snek":
                    pygame.draw.rect(
                        self._screen,
                        (0, 0, 255),
                        pygame.Rect((y * 20), (x * 20) + self.offset, 20, 20),
                    )
        pass

    def process_event(self, event):
        """handle various events in game: movement and exit button."""
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.direction != "down":
                self.direction = "up"
            if event.key == pygame.K_DOWN and self.direction != "up":
                self.direction = "down"
            if event.key == pygame.K_LEFT and self.direction != "right":
                self.direction = "left"
            if event.key == pygame.K_RIGHT and self.direction != "left":
                self.direction = "right"


class End_Scene(Scene):
    """The end screen of snake, handles leader board and reset logic."""

    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, "data")

    def __init__(self, screen, clock, background_color=(0, 0, 0)):
        """
        This function initializes the end scene by setting
        up visual text and visual instructions.
        """
        super().__init__(screen, clock, background_color)
        self.player_score = 0
        self.player_time = 0
        (w, h) = self._screen.get_size()
        self.leaderboard = []
        # code for Game over screen.
        self._title_name = "Leader Board"
        self._title_size = 60
        self._title_color = [255, 255, 255]
        title_font = pygame.font.Font(
            pygame.font.get_default_font(), self._title_size
        )
        self._title = title_font.render(
            self._title_name, True, self._title_color
        )
        self._title_pos = self._title.get_rect(center=(w // 2, h // 8))

        self._score_name = "        Date                            Score                           Time"
        self._score_size = 30
        self._score_color = [255, 255, 255]
        title_font = pygame.font.Font(
            pygame.font.get_default_font(), self._score_size
        )
        self._score = title_font.render(
            self._score_name, True, self._score_color
        )
        self._score_pos = self._title.get_rect(center=(w // 4, h // 4))
        pass

    def draw(self):
        """draws the leaderboard and options onto the screen."""
        super().draw()
        self._screen.blit(self._score, self._score_pos)
        self._screen.blit(self._title, self._title_pos)
        count = 10
        if 10 > len(self.leaderboard):
            count = len(self.leaderboard)

        for x in range(0, count):
            (w, h) = self._screen.get_size()
            date = self.leaderboard[x][2].strftime("%d/%m/%Y %H:%M:%S")
            record_name = "{0:<2} {1:<10}  {2:<10}          {3:<30}".format(
                str(x + 1), date, self.leaderboard[x][0], self.leaderboard[x][1]
            )
            print(record_name)
            record_size = 25
            record_color = (255, 255, 255)
            record_font = pygame.font.SysFont("couriernew", record_size, 1, 0)
            record = record_font.render(record_name, True, record_color)
            record_pos = self._title.get_rect(
                center=(w // 4 + 10, h // 4 + (30 * (x + 1)))
            )
            self._screen.blit(record, record_pos)
        restart_title = "Press Space to play again!"
        restart_size = 20
        restart_color = (255, 255, 255)
        restart_font = pygame.font.Font(
            pygame.font.get_default_font(), restart_size
        )
        restart = restart_font.render(restart_title, True, restart_color)
        restart_pos = record_pos = self._title.get_rect(
            center=(w // 2, h // 2 + h // 4)
        )
        self._screen.blit(restart, restart_pos)

        restart_title = "Press Escape to exit the game!"
        restart_size = 20
        restart_color = (255, 255, 255)
        restart_font = pygame.font.Font(
            pygame.font.get_default_font(), restart_size
        )
        restart = restart_font.render(restart_title, True, restart_color)
        restart_pos = record_pos = self._title.get_rect(
            center=(w // 2, h // 2 + h // 4 + 50)
        )
        self._screen.blit(restart, restart_pos)

    def pickle_in_player(self):
        """takes player game records and puts it in pickle file."""
        game_record = []
        game_date = datetime.now()
        game_record.append(self.player_score)
        game_record.append(self.player_time)
        game_record.append(game_date)
        with open(self.data_dir + "/leaderboard.pickle", "ab") as fh:
            pickle.dump(game_record, fh, pickle.HIGHEST_PROTOCOL)

    def load_in(self):
        """loads in all game records."""
        with open(self.data_dir + "/leaderboard.pickle", "rb") as fh:
            while True:
                try:
                    yield pickle.load(fh)
                except EOFError:
                    break

    def start_scene(self, score, time):
        """method driver that handles End Scene logic."""
        print(pygame.font.get_fonts())
        print(score)
        print(time)
        self.player_score = score
        self.player_time = time
        self.pickle_in_player()
        self.leaderboard = list(self.load_in())
        self.leaderboard.sort(key=lambda l: l[0], reverse=True)
        self.draw()
        self.update()
        print(self.leaderboard)
        while True:
            for event in pygame.event.get():
                next_scene = self.process_event(event)
                if next_scene != None:
                    return next_scene

        pass

    def process_event(self, event):
        """handles the event in end screen: new game and exit game."""
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "exit"
            if event.key == pygame.K_SPACE:
                return "Title"
