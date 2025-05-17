import pygame
import soundfile as sf
import numpy as np
import serial
import random
import socket

cont = 0  # contador para evitar que o primeiro valor lido na variavel seja validado
frequencia = 0  # frequencia
soundoutput = 0

# Inicializar o mixer do pygame
pygame.init()
pygame.mixer.init(frequency=44100, channels=2, buffer=2**12)

# Configurar os canais de áudio
left_channel = pygame.mixer.Channel(0)
right_channel = pygame.mixer.Channel(1)

UDP_IP = "0.0.0.0"  # Escuta em todas as interfaces
UDP_PORT = 5006    # Porta UDP

# Função para carregar e reproduzir um áudio em um canal específico
def play_sound(channel, filename):
    sound = pygame.mixer.Sound(filename)

    if channel == 0:
        left_channel.set_volume(1.0, 0.0)  # Atribui o canal esquerdo
    elif channel == 1:
        right_channel.set_volume(0.0, 1.0)  # Atribui o canal direito
    else:
        left_channel.set_volume(1.0, 1.0)  # Reproduz nos dois canais (estéreo)

    left_channel.play(filename  )

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Escutando na porta {UDP_PORT}...")

# Reprodução dos sons em canais específicos
while True:
    try:
        data, addr = serial.Serial('COM1', 115200)
        print('Arduino conectado')
        break
    except:
        pass

while True:
    leitura = str(data.readline())
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
            som = 'som/audio_4_gonza_rec.mp3'
        elif frequencia % 3 == 0:
            som = 'som/audio_3_gonza_rec.mp3'
        elif frequencia % 2 == 0:
            som = 'som/audio_2_gonza_rec.mp3'
        elif frequencia % 1 == 0:
            som = 'som/audio_1_gonza_rec.mp3'

        # Reproduz o novo áudio no canal especificado
        play_sound(soundoutput, som)
