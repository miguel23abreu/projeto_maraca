import pygame
import sys

# Inicializacao pygame
pygame.init()

# setup da superficie
surface = pygame.display.set_mode( (600,300) )
surface.fill( [30,150,230] )    # cor de fundo

clock = pygame.time.Clock()

i = 140
j=0
k = -600
m = 0
color = (20,2,10)    # fazer testes aqui
while (True):

   # eventos de saida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();

    # cor de fundo
    color2 = (i,200,i)    # fazer testes aqui
#    i += 1
#    if i >= 255: i = 0;

    surface.fill( color )

#    color2 = (2,i,60)    # fazer testes aqui
    pygame.draw.rect( surface, color2, pygame.Rect(j, 32, 62, 62), 3 ) #testes aqui
    pygame.draw.rect( surface, color2, pygame.Rect(k, 32, 62, 62), 3 ) #testes aqui
    pygame.draw.rect( surface, color2, pygame.Rect(m%600, 192, 2, 50), 1 ) #testes aqui
    pygame.draw.rect( surface, color2, pygame.Rect(k%600+4, 192, 2, 50), 1 ) #testes aqui
    pygame.draw.rect( surface, color2, pygame.Rect(192, 192, 50, 2), 1 ) #testes aqui
    pygame.draw.circle( surface, color2, (50, 200), j%200+1, 2 ) #testes aqui
    j +=1
    k += 1
    m += 1
    if j >= 600: j = -600
    if k >= 600: k = -600


    pygame.display.flip()       # fazer testes aqui
    pygame.display.update()     # fazer testes aqui
    print(m,j,i)

    clock.tick(120)


