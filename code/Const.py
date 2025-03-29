import pygame

# CORES
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 249, 109)
COLOR_BLUE = (0, 0, 109)
COLOR_ORANGE = (255, 111, 0)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)
COLOR_RED = (255, 0, 0)

# DISTANCIA DOS JOGADORES
DISTANCIA_JOGADORES = 100

# VELOCIDADE
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1BG0': 0,
    'Level1BG1': 1,
    'Level1BG2': 2,
    'Level1BG3': 3,
    'Level1BG4': 4,
    'Level1BG5': 5,
    'Level2BG0': 0,
    'Level2BG1': 1,
    'Level2BG2': 2,
    'Level2BG3': 3,
    'Level2BG4': 4,
    'Player1': 3,
    'Player1Shot': 1,
    'Player2': 3,
    'Player2Shot': 3,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 2,
}

ENTITY_HEALTH = {
    'Level1BG0': 999,
    'Level1BG1': 999,
    'Level1BG2': 999,
    'Level1BG3': 999,
    'Level1BG4': 999,
    'Level1BG5': 999,
    'Level2BG0': 999,
    'Level2BG1': 999,
    'Level2BG2': 999,
    'Level2BG3': 999,
    'Level2BG4': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,

}

ENTITY_DAMAGE = {
    'Level1BG0': 0,
    'Level1BG1': 0,
    'Level1BG2': 0,
    'Level1BG3': 0,
    'Level1BG4': 0,
    'Level1BG5': 0,
    'Level2BG0': 0,
    'Level2BG1': 0,
    'Level2BG2': 0,
    'Level2BG3': 0,
    'Level2BG4': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
}

ENTITY_SCORE = {
    'Level1BG0': 0,
    'Level1BG1': 0,
    'Level1BG2': 0,
    'Level1BG3': 0,
    'Level1BG4': 0,
    'Level1BG5': 0,
    'Level2BG0': 0,
    'Level2BG1': 0,
    'Level2BG2': 0,
    'Level2BG3': 0,
    'Level2BG4': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200,
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
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RSHIFT,
                    'Player2': pygame.K_LSHIFT}

# S
SPAWN_TIME = 3000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000

# TAMANHO E ALTURA
SCR_WIDTH = 576
SCR_HEIGHT = 324
