#!/usr/bin/python
import pygame
from pygame.locals import *
import sys
import os

class Game():
    def main(self, screen):
        clock = pygame.time.Clock()
        self.FPS = 60
        background = pygame.Surface(screen.get_size())
        background.fill((24, 24, 24))

        self.WINWIDTH, self.WINHEIGHT = screen.get_size()

        while True:
            dt = clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
