import pygame
import os 
import scenes.export as scenes
from utils import *

"""
    This file handle running the main game
    Class Game function __init__ draw the screen and background
    Function run handle game loop
"""

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.gameSceneManager = scenes.GameSceneManager(
            "start",
            {"scenes": {}},
        )
        playScene = scenes.PlayScene(self.screen, self.gameSceneManager)
        startScene = scenes.StartScene(self.screen, self.gameSceneManager)
        self.gameSceneManager.scenes = {"play": playScene, "start": startScene}
        self.bg = pygame.transform.scale(
            pygame.image.load(os.path.join("data","background.png")), (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

    # This function handle gameloop
    def run(self):
        while True:
            self.screen.blit(self.bg, (0, 0))
            self.gameSceneManager.run()
            pygame.display.update()
            self.clock.tick(FPS)


Game().run()
