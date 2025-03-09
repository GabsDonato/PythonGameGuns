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
        pygame.mixer_music.load('./asset/BossMain.wav')
        pygame.mixer_music.play(-1)


        while True:
            menu = Menu(self.screen)
            menu.run()
            pass



    # check for all events
    # for event in pygame.event.get():
    #   if event.type == pygame.QUIT:
    #      pygame.quit()  # close screen
    #     quit()  # End pygame
