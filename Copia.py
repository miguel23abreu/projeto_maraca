import soundfile as sf
import sounddevice as sd
import pygame
import random
import socket

pygame.init()
pygame.mixer.init(frequency=44100, channels=2, buffer=2**12)

UDP_IP = "0.0.0.0"  # Escuta em todas as interfaces
UDP_PORT = 12345    # Porta UDP

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

display_x = 500
display_y = 200
#display = pygame.display.set_mode((display_x, display_y))
clock = pygame.time.Clock
#maraca = pygame.image.load('teste_pygame/maraca_02_per.png')
#maraca_ani = pygame.image.load('teste_pygame/maraca_03_red.png')

Running = True
x = display_x / 2
y = display_y / 2
x_change = 0
y_change = 0
maraca_x = 57
maraca_y = 86
cont = 0
frequencia = 0
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    data, addr = sock.recvfrom(1024)
    leitura = data.decode().split()  # Divide a mensagem em partes
    frequencia = int(leitura[0])
    Dado_MIDI = int(leitura[1])

    numRandom = random.randint(0, 80)
    #display.fill("purple")

    # Sua lógica de reprodução de som aqui, com base na frequência e nos dados MIDI
    if frequencia % 5 == 0:
        som = pygame.mixer.Sound('som/audio_5_gonza.mp3')
    elif frequencia % 4 == 0:
        som = pygame.mixer.Sound('som/audio_4_gonza.mp3')
    elif frequencia % 3 == 0:
        som = pygame.mixer.Sound('som/audio_3_gonza.mp3')
    elif frequencia % 2 == 0:
        som = pygame.mixer.Sound('som/audio_2_gonza.mp3')
    elif frequencia % 1 == 0:
        som = pygame.mixer.Sound('som/audio_1_gonza.mp3')

    if numRandom > 72:
        channel1.play(som)
        channel2.play(som)
        x_change = display_x / 2 - maraca_x / 2
        #display.blit(maraca_ani, (x, y))
    elif numRandom < 40:
        canal = channel1
        canal.play(som)
        x_change = 0
        #display.blit(maraca_ani, (x, y))
    else:
        canal = channel2
        canal.play(som)
        x_change = display_x - maraca_x
        #display.blit(maraca_ani, (x, y))

    #pygame.display.flip()
    #clock.tick(60)
