import pygame
import Game

if __name__ == '__main__':
    # Call Pygame
    pygame.init()
    # Create Window
    screen = pygame.display.set_mode((640, 480))
    # Call Game
    new = Game.Game()
    new.main(screen)
