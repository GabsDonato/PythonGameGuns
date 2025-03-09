import pygame

from code.menu import Menu


# !/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(600, 480))

    def run(self,):
        while True:
            menu = Menu(self.screen)
            menu.run()
            pass



    # check for all events
    # for event in pygame.event.get():
    #   if event.type == pygame.QUIT:
    #      pygame.quit()  # close screen
    #     quit()  # End pygame
