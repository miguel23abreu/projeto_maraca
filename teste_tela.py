import pygame
import time
pygame.init()
display_x = 500
display_y = 200
display = pygame.display.set_mode((display_x, display_y))
clock = pygame.time.Clock()
maraca = pygame.image.load('teste_pygame/maraca_02_per.png')
maraca_ani = pygame.image.load('teste_pygame/maraca_03_red.png')
running = True
x = display_x/2
y = display_y/2
x_change = 0
y_change = 0
dt = 0
maraca_x = 50
maraca_y = 101

#player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_width / 2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display.fill("purple")
    display.blit(maraca, (x, y))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_change = 0
        maraca_left = pygame.transform.rotozoom(maraca_ani, -0.9, 1.0)
        display.blit(maraca_left, (x, y))
    elif keys[pygame.K_RIGHT]:
        x_change = display_x - maraca_x
        maraca_right = pygame.transform.rotozoom(maraca_ani, 0.9, 1.0)
        display.blit(maraca_right, (x, y))
    elif keys[pygame.K_SPACE]:
        x_change = display_x / 2 - maraca_x/2
        maraca_center = pygame.transform.rotozoom(maraca_ani, 0, 1.0)
        display.blit(maraca_center, (x, y))
    x = x_change
    #x = display_x / 2
    #y = y_change
    #x_change = 0
    pygame.display.flip()
    clock.tick(60)


pygame.quit()