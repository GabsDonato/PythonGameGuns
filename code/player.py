#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import SCR_WIDTH, SCR_HEIGHT, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SPACE, PLAYER_KEY_SHOOT, \
    ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    # Movimento do Player
    def move(self):
        pressed_key = pygame.key.get_pressed()
        # Movimento horizontal (esquerda e direita)
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= 5  # Mover para a esquerda
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < SCR_WIDTH:
            self.rect.centerx += 5  # Mover para a direita
        # Pulo
        if pressed_key[PLAYER_KEY_SPACE[self.name]] and self.rect.bottom >= SCR_HEIGHT:
            self.rect.centery -= 150
        self.rect.centery += 0
        # Manter o jogador no chão
        if self.rect.bottom < SCR_HEIGHT:
            self.rect.centery += 5
        # Garantir que o jogador não passe do chão
        if self.rect.bottom >= SCR_HEIGHT:
            self.rect.bottom = SCR_HEIGHT

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:

                if self.name == 'Player1' or self.name == 'Player2':
                    position = (self.rect.centerx + 10, self.rect.centery)
                else:
                    position = (self.rect.centerx - 10, self.rect.centery)
                return PlayerShot(name=f'{self.name}Shot', position=position)
