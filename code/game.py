import pygame

from code.Const import SCR_WIDTH, SCR_HEIGHT
from code.menu import Menu


# !/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(SCR_WIDTH, SCR_HEIGHT))

    def run(self,):
        while True:
            menu = Menu(self.screen)
            menu.run()
            pass




