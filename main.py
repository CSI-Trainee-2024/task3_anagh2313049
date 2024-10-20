import pygame
from sys import exit

class Game:
    def __init__(self):
        pass

    def __init__(self):
        pass




if __name__ == '__main__':
    pygame.init
    # screen setup
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width,screen_height))

    clock = pygame.time.Clock()
    game = Game()

    # gmae runs until condition is true
    while True():

        # quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((30,30,30))
        game.run()

        pygame.display.flip()
        clock.tick(60) # 60 frames per second
