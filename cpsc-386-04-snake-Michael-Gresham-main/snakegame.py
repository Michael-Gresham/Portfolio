"""snakegame.py module"""
# Michael Gresham
# CPSC 386-01
# 2021-11-29
# greshammichael@csu.fullerton.edu
# @Michael-Gresham
#
# Lab 03-00
#
# My snake_game_class
#
import pygame
import scene

# from scene import TitleScene


class SnakeGame:
    """Snake game class runs the game."""

    def __init__(self):
        pass

    def run(self):
        """Controls the scene change logic."""
        print("hello")
        pygame.init()
        display_size = (800, 800)
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(display_size)
        title = "Snek Game"
        pygame.display.set_caption(title)
        player_score = 0
        player_time = 0
        title = scene.TitleScene(screen, clock, 60)
        game_level = scene.GameScene(screen, clock)
        end_scene = scene.End_Scene(screen, clock)
        dict_scene = {
            "Title": title,
            "Level1": game_level,
            "End Scene": end_scene,
        }

        current_scene = "Title"

        while current_scene != "exit":
            print(current_scene)
            if current_scene == "End Scene":
                current_scene = dict_scene[current_scene].start_scene(
                    player_score, player_time
                )
            else:
                current_scene = dict_scene[current_scene].start_scene()
                if current_scene == "End Scene":
                    player_score = game_level.score
                    player_time = game_level.time
        return None
