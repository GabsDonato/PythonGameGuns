#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Const import SCR_WIDTH, SCR_HEIGHT
from code.background import Background
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1BG':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1BG{i}', (0, 0)))
                    list_bg.append(Background(f'Level1BG{i}', (SCR_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (1, SCR_HEIGHT /2))
