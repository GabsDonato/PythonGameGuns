import pygame

# CORES
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 249, 109)
COLOR_BLUE = (0, 0, 109)
COLOR_ORANGE = (255, 111, 0)

# DISTANCIA DOS JOGADORES
DISTANCIA_JOGADORES = 100

# VELOCIDADE
ENTITY_SPEED = {
    'Level1BG0': 0,
    'Level1BG1': 1,
    'Level1BG2': 2,
    'Level1BG3': 3,
    'Level1BG4': 4,
    'Level1BG5': 5,
    'Level1BG6': 6,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 1,
    'Enemy2': 1
}

ENTITY_HEALTH = {
    'Level1BG0': 999,
    'Level1BG1': 999,
    'Level1BG2': 999,
    'Level1BG3': 999,
    'Level1BG4': 999,
    'Level1BG5': 999,
    'Level1BG6': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 50,
    'Enemy2': 60,
}

# MENU
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# PLAYERS MOVE
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SPACE = {'Player1': pygame.K_SPACE,
                    'Player2': pygame.K_s}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# TAMANHO E ALTURA
SCR_WIDTH = 576
SCR_HEIGHT = 324
