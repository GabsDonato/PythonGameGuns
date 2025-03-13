#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, SCR_HEIGHT, SCR_WIDTH
from code.entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self, ): #movimento do jogador
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name] #Subir player
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < SCR_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name] #descer player
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0: # frente player
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < SCR_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]  # atrás player
        pass
