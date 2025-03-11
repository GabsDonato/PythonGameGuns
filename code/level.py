#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code import EntityFactory
from code.EntityFactory import EntityFactory
from code.entity import Entity


class Level:
    def __init__(self, screen, name, game_mode):
        self.screen = screen
        self.window = screen
        self.name = name
        self.game_mode = game_mode #modo do jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass
