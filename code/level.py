#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code import EntityFactory
from code.Const import SCR_HEIGHT, COLOR_WHITE, MENU_OPTION, SPAWN_TIME, COLOR_GREEN, COLOR_CYAN, \
    EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL, SCR_WIDTH, COLOR_RED
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.Entity import Entity
from code.EntityMediator import EntityMediator
from code.player import Player


class Level:
    def __init__(self, screen: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL  # 20 segundos
        self.screen = screen
        self.window = screen
        self.name = name
        self.game_mode = game_mode  # modo do jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'BG'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)

        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)

        self.last_enemy_time = pygame.time.get_ticks()
        self.enemy_interval = SPAWN_TIME

        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # 100ms

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}Music.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', COLOR_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', COLOR_CYAN, (10, 45))

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
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    self.game_over(player_score)
                    return False

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, SCR_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, SCR_HEIGHT - 20))
            pygame.display.flip()
            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            # life
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def game_over(self, player_score: list[int]):
        """Exibe a tela de Game Over"""
        pygame.mixer_music.stop()
        pygame.mixer.music.load('./asset/game_over_music.wav')
        pygame.mixer.music.play()

        font = pygame.font.SysFont('Arial', 40)
        text_game_over = font.render("GAME OVER", True, COLOR_RED)
        text_rect = text_game_over.get_rect(center=(SCR_WIDTH // 2, SCR_HEIGHT // 2 - 50))
        self.screen.blit(text_game_over, text_rect)

        retry_text = pygame.font.SysFont('Arial', 15).render("Pressione ESC para voltar ao menu", True, COLOR_WHITE)
        retry_rect = retry_text.get_rect(center=(SCR_WIDTH // 2, SCR_HEIGHT // 2 + 80))
        self.screen.blit(retry_text, retry_rect)

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Se pressionar ESC, volta para o menu
                        waiting = False
                        return
