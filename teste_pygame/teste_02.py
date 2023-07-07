import pygame, sys
import time

# Inicializacao pygame
pygame.init()

# Setup da superficie
display_x = 600
display_y = 400

surface = pygame.display.set_mode( (display_x, display_y ) )
surface.fill( [30,150,230] )    # cor de fundo

clock = pygame.time.Clock()

carro_velho = pygame.image.load('carro.png')

def car( x, y ):
    surface.blit( carro_velho, (x,y) )

i = 0
x = 200
y = 200
x_change = 0 #mudanca horizontal
y_change = 0 #mudanca vertical

car_x = 73
car_y = 89

while (True):

   # eventos de saida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();

        if event.type == pygame.KEYDOWN:
	        if event.key == pygame.K_LEFT and x > 0 :
	            x -= 5 #x_change = -5                
	        elif event.key == pygame.K_RIGHT and x < 600-car_x:
		        x += 5 #x_change = 5
                
	        elif event.key == pygame.K_UP and y > 0:
		        y -= 5 #y_change = -5
	        elif event.key == pygame.K_DOWN and y < 300 - car_y:
		        y += 5 #y_change = 20

    # cor de fundo
    color = ( i,2,i )    # fazer testes aqui
    surface.fill( color )    
    i +=1
    if i >= 255: i = 0;

    #x += x_change
    #y += y_change
    print( x, y, x_change, y_change) 

#    x_change = 0 
 #   y_change = 0 

    # atualiza a nova posicao
    car( x, y )

    pygame.display.flip()       # fazer testes aqui
    pygame.display.update()     # fazer testes aqui

    clock.tick(60)

