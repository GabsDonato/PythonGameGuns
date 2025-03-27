#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
from typing import Any

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code import EntityFactory
from code.Const import SCR_HEIGHT, COLOR_WHITE, MENU_OPTION, SPAWN_TIME
from code.EntityFactory import EntityFactory
from code.Entity import Entity


class Level:
    def __init__(self, screen, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.screen = screen
        self.window = screen
        self.name = name
        self.game_mode = game_mode  # modo do jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        self.last_enemy_time = pygame.time.get_ticks()
        self.enemy_interval = SPAWN_TIME

    def run(self, ) -> Any:
        pygame.mixer_music.load(f'./asset/Level1Music.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # Verificar se o tempo para criar um novo inimigo passou
            current_time = pygame.time.get_ticks()  # Tempo atual
            if current_time - self.last_enemy_time >= self.enemy_interval:
                # Escolher aleatoriamente entre 'Enemy1' e 'Enemy2'
                enemy_choice = random.choice(['Enemy1', 'Enemy2'])
                self.entity_list.append(EntityFactory.get_entity(enemy_choice))
                self.last_enemy_time = current_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, SCR_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, SCR_HEIGHT - 20))
            pygame.display.flip()

    pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
