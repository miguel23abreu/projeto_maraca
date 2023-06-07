import serial
import soundfile as sf #biblioteca utilizada para manipular o audio
import sounddevice as sd #bibiioteca utilizada para reproduzir o audio
import pygame
cont = 0 #contador para evitar que o primeiro valor lido na variavel seja validado
frequencia = 0 #frequencia
pygame.init()
pygame.mixer.init()
while True:
    try:
        arduino = serial.Serial('COM6', 9600)
        print('Arduino conectado')
        break
    except:
        pass
while True:
    leitura = str(arduino.readline())
    print('valor recebido ' + leitura)
    cont += 1
    if(cont > 1):
        frequencia = int(leitura[2])
        print(frequencia)
        #definindo o tempo do audio de acordo com a frequencia
        if(frequencia % 4 == 0):
            pygame.mixer.music.load('som/audio4.mp3')
            pygame.mixer.music.play()
            #break
        elif(frequencia % 3 == 0):
            pygame.mixer.music.load('som/audio3.mp3')
            pygame.mixer.music.play()
            #break
        elif (frequencia % 2 == 0):
            pygame.mixer.music.load('som/audio2.mp3')
            pygame.mixer.music.play()
            #break
        elif (frequencia % 1 == 0):
            pygame.mixer.music.load('som/audio1.mp3')
            pygame.mixer.music.play()
            #break