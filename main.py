import pygame

print('Setup start')

pygame.init()
screen = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop start')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # close screen
            quit()  # End pygame
