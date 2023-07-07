import pygame
import soundfile as sf
import numpy as np
import serial
import random

cont = 0  # contador para evitar que o primeiro valor lido na variavel seja validado
frequencia = 0  # frequencia
soundoutput = 0

# Inicializar o mixer do pygame
pygame.mixer.init()

# Configurar os canais de áudio
left_channel = pygame.mixer.Channel(0)
right_channel = pygame.mixer.Channel(1)

# Função para carregar e reproduzir um áudio em um canal específico
def play_sound(channel, filename):
    sound = pygame.mixer.Sound(filename)

    if channel == 0:
        left_channel.play(sound)  # Atribui o canal esquerdo
    elif channel == 1:
        right_channel.play(sound)  # Atribui o canal direito
    else:
        sound.play()  # Reproduz nos dois canais (estéreo)

# Reprodução dos sons em canais específicos
while True:
    try:
        arduino = serial.Serial('COM6', 115200)
        print('Arduino conectado')
        break
    except:
        pass

while True:
    leitura = str(arduino.readline())
    print('valor recebido ' + leitura)
    cont += 1
    numRandom = random.randint(0, 80)
    if cont > 1:
        frequencia = int(leitura[2])
        print(frequencia)
        if numRandom > 72:
            soundoutput = 2
        elif numRandom < 40:
            soundoutput = 0
        else:
            soundoutput = 1

        # Definindo o tempo do audio de acordo com a frequencia
        if frequencia % 4 == 0:
            som = 'som/audio4.wav'
        elif frequencia % 3 == 0:
            som = 'som/audio3.wav'
        elif frequencia % 2 == 0:
            som = 'som/audio2.wav'
        elif frequencia % 1 == 0:
            som = 'som/audio1.wav'

        # Reproduz o novo áudio no canal especificado
        play_sound(soundoutput, som)
