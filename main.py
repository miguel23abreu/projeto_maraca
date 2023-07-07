import serial
import soundfile as sf #biblioteca utilizada para manipular o audio
import sounddevice as sd #bibiioteca utilizada para reproduzir o audio
import pygame
import random
import numpy as np
pygame.init()
pygame.mixer.init(frequency=44100, channels=2, buffer=2**12)
while True:
    try:
        arduino = serial.Serial('COM6', 115200)
        print('Arduino conectado')
        break
    except:
        pass
display_x = 500
display_y = 200
display = pygame.display.set_mode((display_x, display_y))
clock = pygame.time.Clock()
maraca = pygame.image.load('teste_pygame/maraca_02_per.png')
maraca_ani = pygame.image.load('teste_pygame/maraca_03_red.png')
Running = True
x = display_x/2
y = display_y/2
x_change = 0
y_change = 0
maraca_x = 57
maraca_y = 86
cont = 0 #contador para evitar que o primeiro valor lido na variavel seja validado
frequencia = 0 #frequencia
channel1 = pygame.mixer.Channel(0) # argument must be int
channel2 = pygame.mixer.Channel(1)
print( 'aquii')
leitura = '30 20 20'
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    print( 'aquiii')
    leitura = str(arduino.readline())
    print( 'aquuiiiiiii')
    print('valor recebido ' + leitura)
    cont += 1
    numRandom = random.randint(0, 80)
    if(cont > 1):
        display.fill("purple")
        frequencia = int(leitura[2])
        print(frequencia)
        print(numRandom)
        #definindo o tempo do audio de acordo com a frequencia
        if(frequencia % 4 == 0):
            som = pygame.mixer.Sound('som/audio4.mp3')
        elif(frequencia % 3 == 0):
            som = pygame.mixer.Sound('som/audio3.mp3')
        elif (frequencia % 2 == 0):
            som = pygame.mixer.Sound('som/audio2.mp3')
        elif (frequencia % 1 == 0):
            som = pygame.mixer.Sound('som/audio1.mp3')
        if (numRandom > 72):
            channel1.play(som)
            channel2.play(som)
            x_change = display_x / 2 - maraca_x / 2
            maraca_center = pygame.transform.rotozoom(maraca_ani, 0, 1.0)
            display.blit(maraca_center, (x, y))
        elif (numRandom < 40):
            canal = channel1
            canal.play(som)
            x_change = 0
            maraca_left = pygame.transform.rotozoom(maraca_ani, -0.9, 1.0)
            display.blit(maraca_left, (x, y))
        else:
            canal = channel2
            canal.play(som)
            x_change = display_x - maraca_x
            maraca_right = pygame.transform.rotozoom(maraca_ani, 0.9, 1.0)
            display.blit(maraca_right, (x, y))
        x = x_change
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)