#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import SCR_WIDTH, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW, COLOR_BLUE, \
    COLOR_ORANGE


class Menu:
    def __init__(self, screen):
        self.window = screen
        self.surf = pygame.image.load('./asset/backgroundMenu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/BossMain.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Gangsters Vs Soldiers", COLOR_BLUE, ((SCR_WIDTH / 2), 70))
            self.menu_text(50, "The war for gold", COLOR_ORANGE, ((SCR_WIDTH / 2), 110))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((SCR_WIDTH / 2), 200 + 20 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((SCR_WIDTH / 2), 200 + 20 * i))

            pygame.display.flip()

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close screen
                    quit()  # End pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                       if menu_option < len(MENU_OPTION) -1:
                           menu_option += 1
                       else:
                           menu_option = 0
                    if event.key == pygame.K_UP:
                       if menu_option > 0:
                           menu_option -= 1
                       else:
                           menu_option = len(MENU_OPTION) -1
                    if event.key == pygame.K_RETURN: #ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
