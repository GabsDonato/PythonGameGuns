#!/usr/bin/python
# -*- coding: utf-8 -*-


from code.Const import SCR_WIDTH, SCR_HEIGHT, DISTANCIA_JOGADORES
from code.Enemy import Enemy
from code.background import Background
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1BG':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1BG{i}', (0, 0)))
                    list_bg.append(Background(f'Level1BG{i}', (SCR_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (4, SCR_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (4 + DISTANCIA_JOGADORES, SCR_HEIGHT / 2 - 30))
            case 'Enemy1':
                return Enemy('Enemy1', (SCR_WIDTH + 80, 405 / 2 - 10))
            case 'Enemy2':
                return Enemy('Enemy1', (SCR_WIDTH + 10, 405 / 2 - 10))
