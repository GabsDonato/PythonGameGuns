import pygame

from code.Const import SCR_WIDTH, SCR_HEIGHT, MENU_OPTION
from code.Score import Score
from code.level import Level
from code.menu import Menu


# !/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(SCR_WIDTH, SCR_HEIGHT))

    def run(self, ):
        while True:
            score = Score(self.screen)
            menu = Menu(self.screen)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]
                level = Level(self.screen, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.screen, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass
